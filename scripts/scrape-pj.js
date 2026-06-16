const { chromium } = require("playwright");
const fs = require("fs");

const CITIES = [
  { name: "Issy-les-Moulineaux", cp: "92130", dept: "92" },
  { name: "Évry-Courcouronnes", cp: "91000", dept: "91" },
  { name: "Vitry-sur-Seine", cp: "94400", dept: "94" },
  { name: "Saint-Maur-des-Fossés", cp: "94100", dept: "94" },
  { name: "Palaiseau", cp: "91120", dept: "91" },
];

function extractPhone(body) {
  // Normalize to composed form (NFC) — fixes decomposed accents
  const text = body.normalize("NFC");
  
  // Pattern: "Numéro de Téléphone" followed by a phone number
  const m = text.match(/Numéro\s+de\s+Téléphone\s*\n?\s*(0[1-9](?:\s*\d{2}){4})/);
  if (m) return m[1].replace(/\s/g, "");
  
  // Fallback: any 0x xx xx xx xx pattern after "Contact" section
  const m2 = text.match(/Contact[\s\S]{0,500}?(0[1-9](?:\s*\d{2}){4})/);
  if (m2) return m2[1].replace(/\s/g, "");
  
  return "";
}

function extractAddress(body) {
  const text = body.normalize("NFC");
  const m = text.match(/Localisation\s*\n\s*([^\n]{10,100}?)\s*-?\s*Y aller/);
  if (m) return m[1].trim().replace(/\s+/g, " ");
  
  // Fallback
  const m2 = text.match(/(\d{1,4}\s+(?:rue|avenue|boulevard|place|allée|chemin|route|square|impasse|quai|cours)\s+[^,\n]{5,80}\s*\d{5}\s+\w+)/i);
  if (m2) return m2[1].replace(/\s+/g, " ");
  
  return "";
}

(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    args: ['--disable-blink-features=AutomationControlled','--no-sandbox']
  });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
    viewport: { width: 390, height: 844 },
    locale: 'fr-FR'
  });
  const page = await context.newPage();
  const allResults = [];
  
  for (const city of CITIES) {
    const searchURL = `https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=agence+immobiliere&ou=${city.cp}+${encodeURIComponent(city.name)}`;
    console.log(`\n🔍 ${city.name}...`);
    
    try {
      await page.goto(searchURL, { waitUntil: "networkidle", timeout: 45000 });
      await page.waitForTimeout(3000);
    } catch(e) { console.log(`  ⚠️ Skip`); continue; }
    
    // Collect detail URLs
    const detailURLs = await page.evaluate(() => {
      const urls = new Set();
      document.querySelectorAll("a[href*='/pros/']").forEach(l => {
        if (l.href.match(/\/pros\/\d+/)) urls.add(l.href);
      });
      return [...urls].slice(0, 25);
    });
    
    console.log(`  📋 ${detailURLs.length} fiches`);
    let cityCount = 0;
    
    for (const detailURL of detailURLs) {
      try {
        await page.goto(detailURL, { waitUntil: "networkidle", timeout: 20000 });
        await page.waitForTimeout(2000);
        // Scroll to trigger lazy sections
        await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight / 2));
        await page.waitForTimeout(1500);
      } catch(e) { continue; }
      
      const info = await page.evaluate(() => {
        const body = document.body.innerText;
        const name = document.querySelector("h1")?.textContent?.trim() || "";
        
        // Phone
        let tel = "";
        const text = body.normalize("NFC");
        const m = text.match(/Numéro\s+de\s+Téléphone\s*\n?\s*(0[1-9](?:\s*\d{2}){4})/);
        if (m) tel = m[1].replace(/\s/g, "");
        
        // Address
        let adr = "";
        const m2 = text.match(/Localisation\s*\n\s*([^\n]{10,100}?)\s*-?\s*Y aller/);
        if (m2) adr = m2[1].trim().replace(/\s+/g, " ");
        
        // Website
        let site = "";
        const siteLink = document.querySelector("a[href*='www.']:not([href*='pagesjaunes']):not([href*='google']):not([href*='facebook'])");
        if (siteLink && siteLink.href.startsWith("http")) site = siteLink.href;
        
        return { nom: name, telephone: tel, adresse: adr, site_web: site };
      });
      
      if (info && info.telephone) {
        allResults.push({
          ...info,
          ville: city.name,
          code_postal: city.cp,
          departement: city.dept
        });
        cityCount++;
        process.stdout.write("📞");
      } else {
        process.stdout.write(".");
      }
    }
    
    console.log(`  ✅ ${cityCount} avec téléphone`);
  }
  
  console.log(`\n\n📊 TOTAL: ${allResults.length} agences avec téléphone complet`);
  
  // Save
  const clean = s => (s || "").replace(/[\n\r]+/g, " ").replace(/"/g, '""').trim();
  const csv = "nom,ville,code_postal,departement,adresse,telephone,site_web\n" + 
    allResults.map(r => `"${clean(r.nom)}","${r.ville}","${r.code_postal}","${r.departement}","${clean(r.adresse)}","${r.telephone}","${clean(r.site_web)}"`).join("\n");
  fs.writeFileSync("crm/pj-sud-paris-2.csv", csv);
  
  // Show sample
  console.log("\n--- Échantillon ---");
  allResults.slice(0, 10).forEach((r, i) => 
    console.log(`${i+1}. ${r.nom} | ☎ ${r.telephone} | 📍 ${r.adresse}`)
  );
  
  await browser.close();
})();
