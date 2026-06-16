#!/usr/bin/env python3
"""Génère un mail de prospection personnalisé pour chaque agence."""

import csv, re
from urllib.parse import urlparse
from datetime import datetime

INPUT = '/opt/data/workspace/pro-repo/crm/pj-sud-paris.csv'
OUTPUT = INPUT  # overwrite with new column

def detect_type(nom, site):
    """Detect agency type for personalization."""
    nom_lower = nom.lower()
    site_domain = ''
    try:
        site_domain = urlparse(site).netloc.lower() if site else ''
    except: pass
    
    networks = {
        'orpi': 'réseau ORPI',
        'century 21': 'réseau Century 21',
        'laforêt': 'réseau Laforêt',
        'lafôret': 'réseau Laforêt',
        'guy hoquet': 'réseau Guy Hoquet',
        'foncia': 'réseau Foncia',
        'nestenn': 'réseau Nestenn',
        'era ': 'réseau ERA',
        'citya': 'réseau Citya',
        'nexity': 'réseau Nexity',
        'stéphane plaza': 'réseau Stéphane Plaza',
        'keller williams': 'réseau Keller Williams',
        "l'adresse": "réseau l'Adresse",
        'sergic': 'groupe SERGIC',
    }
    
    for key, val in networks.items():
        if key in nom_lower or key in site_domain:
            return val
    return 'indépendant'

def get_hook(nom, ville, dept, atype):
    """Generate a personalized hook/sentence."""
    ville_upper = ville.upper() if ville else ''
    
    hooks_indep = [
        f"Votre agence {nom} est une référence à {ville}. Votre expertise locale est un vrai atout.",
        f"J'ai parcouru votre site — on sent l'approche de proximité qui fait la différence à {ville}.",
        f"Implanté à {ville}, vous connaissez mieux que personne les attentes des clients du {dept}.",
        f"Votre positionnement local sur {ville} m'a impressionné. C'est exactement le type d'agence avec qui j'aimerais collaborer.",
        f"L'ancrage local de {nom} à {ville} est une force que l'automatisation peut décupler.",
    ]
    
    hooks_reseau = [
        f"En tant qu'agence {atype} sur {ville}, vous combinez la force d'un grand groupe avec la connaissance du terrain.",
        f"Votre agence {atype} de {ville} allie puissance nationale et agilité locale — un combo gagnant.",
        f"J'admire comment les agences {atype} comme la vôtre à {ville} allient process et proximité.",
        f"Le {atype} vous donne une structure solide. L'automatisation peut vous donner un temps d'avance sur {ville}.",
        f"Vous faites partie du {atype} à {ville} — un maillage parfait pour industrialiser la relation client.",
    ]
    
    hooks = hooks_indep if atype == 'indépendant' else hooks_reseau
    import hashlib
    idx = int(hashlib.md5(nom.encode()).hexdigest(), 16) % len(hooks)
    return hooks[idx]

def generate_email(nom, ville, dept, atype, contact_prenom=""):
    """Generate a personalized outreach email."""
    hook = get_hook(nom, ville, dept, atype)
    prenom = f"l'équipe {nom}"
    
    sujet_opts = [
        f"Automatisation sur mesure pour {nom} — {ville}",
        f"{nom} : et si vos leads étaient qualifiés 24h/24 ?",
        f"Proposition IA pour {nom} à {ville}",
        f"Bonjour, une idée pour booster {nom}",
    ]
    import hashlib
    idx_sujet = int(hashlib.md5((nom+'sujet').encode()).hexdigest(), 16) % len(sujet_opts)
    sujet = sujet_opts[idx_sujet]

    email = f"""Objet : {sujet}

Bonjour {prenom},

{hook}

Je suis Donopot, freelance spécialisé en automatisation IA pour les PME françaises — avec une niche dédiée aux agences immobilières.

Concrètement, voici ce que je peux vous apporter :

🔹 Pack Réponse Lead (2 500 – 4 500 €)
Un assistant IA qui qualifie vos leads 24h/24 : réponses personnalisées, prise de rendez-vous, relances automatiques. Vos prospects ne dorment jamais — votre agence non plus.

🔹 Pack Workflows CRM (3 500 – 6 500 €)
J'automatise votre pipeline : synchronisation Pipedrive/HubSpot, attribution des leads, relances programmées, alertes mandats. Du temps libéré pour vos négociateurs.

🔹 Pack Support Client IA (4 500 – 8 500 €)
Chatbot intelligent sur votre site + réponses automatiques aux avis Google/Immodvisor. Disponible 7j/7, il répond comme un membre de votre équipe.

Ma stack : Make / n8n · Pipedrive · Mistral AI · Brevo. 100% RGPD, déployé en 7 à 30 jours selon le pack.

Une question simple : parmi vos défis quotidiens, lequel vous prend le plus de temps — le tri des leads, les relances, ou les tâches administratives ?

Je serais ravi d'en discuter autour d'un café virtuel de 15 minutes cette semaine. Qu'en dites-vous ?

Belle journée,
Donopot
donopot@proton.me
[Site web — bientôt en ligne]

---
P.S. : J'ai déjà préparé une analyse du marché immobilier de {ville} ({dept}). Si ça vous intéresse, je vous l'envoie. 😊
"""
    return email.strip()

# Process
with open(INPUT, 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

print(f"✍️  Génération de {len(rows)} mails personnalisés...")

with open(INPUT, 'w', newline='', encoding='utf-8') as f:
    fields = list(rows[0].keys()) + ['mail_prospection']
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    
    for i, row in enumerate(rows):
        nom = row['nom'].strip()
        ville = row['ville'].strip()
        dept = row.get('departement', '').strip()
        site = row.get('site_web', '')
        
        atype = detect_type(nom, site)
        email_body = generate_email(nom, ville, dept, atype)
        
        row['mail_prospection'] = email_body
        w.writerow(row)
        
        if (i+1) % 25 == 0:
            print(f"  {i+1}/{len(rows)}...")

print(f"✅ {len(rows)} mails générés → {INPUT}")
print(f"   Colonne 'mail_prospection' ajoutée")
