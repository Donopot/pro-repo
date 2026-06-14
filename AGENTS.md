# AGENTS.md — Règles pour agents IA

## Mission

Ce repo est le hub professionnel de Donopot, freelance en **automatisation IA pour PME françaises**.

Objectif : aider les agents IA à :
- Comprendre le projet rapidement
- Produire des assets cohérents avec le positionnement
- Respecter les conventions (commits, structure, design)

---

## Structure du repo

```
pro-repo/
├── AGENTS.md           ← Ce fichier
├── README.md           ← Profil public GitHub
├── site/               ← Landing page statique
│   └── index.html
├── templates/          ← Documents contractuels & commerciaux
│   ├── scope.md        ← Document de périmètre
│   ├── devis.md        ← Devis type (3 offres)
│   ├── audit.md        ← Trame d'audit
│   ├── contrat.md      ← Contrat de prestation
│   ├── annexe-rgpd.md  ← Annexe article 28 RGPD
│   ├── registre-rgpd.md ← Registre traitements (modèle article 30 CNIL)
│   ├── sla.md          ← Annexe maintenance et SLA
│   ├── outreach.md     ← Scripts commerciaux
│   ├── onboarding-checklist.md ← Checklist onboarding 7 phases
│   └── onboarding-email.md     ← Emails de bienvenue et relance
├── crm/                ← Prospection et suivi commercial
│   ├── agences-cibles.csv  ← 100 agences immobilières cibles
│   ├── crm-modele.csv      ← Template CRM importable
│   └── setup-crm.md        ← Guide configuration (Sheets/Airtable/Notion)
├── demos/              ← Démonstrations et guides techniques
├── scripts/            ← Validations locales et CI
└── .github/workflows/  ← Validation et déploiement GitHub Pages
```

---

## Conventions obligatoires

### Git

- Commits en **français**
- Branches : `agent/<domaine>/<description-courte>`
- Push normal. Pas de force push sur `main`. Force-with-lease accepté uniquement sur branche isolée en dernier recours.
- 1 commit par sprint. Message type : `docs(S1): AGENTS.md + README refonte freelance`
- **Ne jamais travailler sur `main` directement.**

### Langue & ton

- Tout le contenu public est en **français**
- Ton : professionnel, direct, orienté résultat
- On ne vend pas "de l'IA", on vend une amélioration mesurable d'un processus métier

### Design

- Dark theme par défaut
- Palette : fond `#0a0a0f`, cartes `#141420`, accent violet `#6c5ce7`
- Typographie : system fonts
- Responsive : mobile-first
- Pas de framework CSS — vanilla HTML/CSS

### Documents

- Templates en **Markdown** pour le versioning
- Export PDF via le navigateur (Print → PDF)
- Un seul fichier par document (pas de dossiers)

---

## Positionnement

**Spécialiste PME française, orienté résultats, cadré RGPD, livré en 7 à 30 jours selon le pack.**

3 niches prioritaires :
1. Agences immobilières
2. Cabinets comptables
3. Courtiers en assurance

3 offres :
1. Pack Réponse Lead (2 500 – 4 500 €)
2. Pack Workflows CRM (3 500 – 6 500 €)
3. Pack Support Client IA (4 500 – 8 500 €)

Stack : Make / n8n · Pipedrive / HubSpot · Brevo · Mistral / OpenAI

---

## Règles de modification

- Ne modifier que ce qui est nécessaire
- Ne pas casser le style ou la structure existante
- Vérifier le rendu dans un navigateur avant de commiter du HTML/CSS
- Les documents contractuels nécessitent une relecture humaine avant usage réel

---

## Checklist avant push

- [ ] Commit en français
- [ ] Fichiers modifiés cohérents avec le sprint
- [ ] Site HTML : rendu vérifié dans le navigateur
- [ ] Templates Markdown : formatage correct, export PDF OK
