#!/usr/bin/env python3
"""Scrape les emails des agences en visitant leurs pages /contact."""
import csv, re, time, urllib.request, urllib.error, ssl

BASE = '/opt/data/workspace/pro-repo'
INPUT = f'{BASE}/crm/pj-sud-paris.csv'
OUTPUT = f'{BASE}/crm/emails.csv'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; Bot/1.0)'})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            return r.read().decode('utf-8', errors='ignore')
    except: return ''

def emails_from(html):
    found = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html))
    bad = ['example','@example','noreply','no-reply','@sentry','@typeform',
           '@sendinblue','@email','@domain','@mail.com','@test','@png','@jpg','@svg','@woff','@gif']
    return [e.lower() for e in found if not any(b in e.lower() for b in bad)]

# Read
agencies = []
with open(INPUT, 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        n = (row.get('nom') or '').strip().strip('"')
        v = (row.get('ville') or '').strip().strip('"')
        s = (row.get('site_web') or '').strip().strip('"')
        if n and s and 'solocal' not in s:
            agencies.append((n, v, s))

print(f"📋 {len(agencies)} sites à scraper\n")

results = []
for i, (nom, ville, site) in enumerate(agencies):
    emails = []
    base = site.rstrip('/')
    for path in [base + '/contact', base + '/nous-contacter']:
        html = fetch(path)
        if html:
            emails = emails_from(html)
            if emails: break
        time.sleep(0.1)
    
    results.append((nom, ville, site, emails))
    em = '📧' if emails else '❌'
    d = emails[0][:40] if emails else '—'
    print(f"  {i+1:3d}/{len(agencies)} {em} {nom[:30]:30s} {d}")

with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['nom','ville','site','emails'])
    for r in results:
        w.writerow([r[0], r[1], r[2], ' | '.join(r[3])])

ok = sum(1 for r in results if r[3])
print(f"\n📊 {ok}/{len(results)} avec email(s) → {OUTPUT}")
