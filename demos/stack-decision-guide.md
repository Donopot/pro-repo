# Guide de décision — Stack technique

> **But :** Aider à choisir la bonne stack outil par outil, selon le contexte client.
> **Principe :** Standardiser pour livrer vite, mais savoir pivoter quand le client a déjà un outil.

---

## 1. Plateforme d'automatisation

| Critère | Make | n8n | Zapier |
|---------|------|-----|--------|
| **Prix démarrage** | 12 $/mois (Core) | Gratuit (self-host) | 19,99 $/mois |
| **Connecteurs** | 2000+ | 400+ | 7000+ |
| **Complexité supportée** | Élevée | Très élevée | Faible à moyenne |
| **Self-host possible** | Non | ✅ Oui (Scaleway, OVH) | Non |
| **Hébergement UE** | Partiel (AWS) | ✅ Oui (Francfort cloud) | Non (US) |
| **Courbe d'apprentissage** | 2-3 jours | 3-5 jours | 1 jour |
| **Idéal pour** | 80% des projets PME | Client exigeant souveraineté ou logique complexe | Projets très simples, client déjà équipé |

### Règle de décision

```
Le client a-t-il une exigence d'hébergement UE stricte ?
  ├── Oui → n8n (cloud Francfort ou self-host Scaleway)
  └── Non → Le client a-t-il déjà Make ou Zapier ?
              ├── Oui → Garder l'existant
              └── Non → Make (plus rapide, plus de connecteurs)
```

---

## 2. CRM

| Critère | Pipedrive | HubSpot |
|---------|-----------|---------|
| **Prix démarrage** | 14 $/poste/mois (Lite) | Gratuit (CRM basique) |
| **Prix pro** | 39 $/poste/mois (Growth) | 18 $/mois (Sales Starter) |
| **Simplicité** | ⭐⭐⭐⭐⭐ Très intuitive | ⭐⭐⭐ Plus chargée |
| **Automatisations natives** | Limitées (Growth+) | Plus riches (Workflows) |
| **API / Webhooks** | ✅ Bonne | ✅ Excellente |
| **Écosystème** | Focalisé vente | Marketing + Service + CMS |
| **Idéal pour** | Agence qui veut un CRM simple, visuel, pipeline | Agence qui veut CRM + marketing + support |

### Règle de décision

```
Le client utilise-t-il déjà un CRM ?
  ├── Oui → S'adapter au CRM existant (intégration API)
  └── Non → Le client veut-il aussi du marketing automation ?
              ├── Oui → HubSpot Starter
              └── Non → Pipedrive Lite
```

---

## 3. Emailing transactionnel & marketing

| Critère | Brevo (ex-Sendinblue) | Mailchimp | SendGrid |
|---------|----------------------|-----------|----------|
| **Prix démarrage** | 7 €/mois (Starter) | Gratuit (500 contacts) | Gratuit (100 emails/j) |
| **Hébergement** | 🇫🇷 France / UE | 🇺🇸 US | 🇺🇸 US |
| **RGPD friendly** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **API** | ✅ Bonne | ✅ OK | ✅ Excellente |
| **Idéal pour** | Projets français, priorité conformité | Campagnes marketing | Volume élevé, API-first |

### Règle de décision

```
Le client envoie-t-il des emails transactionnels en France ?
  ├── Oui → Brevo (hébergement UE, conformité)
  └── Non → Le client a-t-il déjà un outil ?
              ├── Oui → Garder l'existant
              └── Non → Brevo par défaut
```

---

## 4. LLM / IA

| Critère | Mistral (API) | OpenAI (API) |
|---------|---------------|--------------|
| **Prix input** | 0,1 $/M tokens (Small 4) | 0,15 $/M tokens (GPT-4o mini) |
| **Hébergement** | 🇪🇺 UE | 🇺🇸 US |
| **DPA / CCT** | ✅ DPA dispo | ✅ DPA + CCT |
| **Qualité français** | ⭐⭐⭐⭐ Très bon | ⭐⭐⭐⭐⭐ Excellent |
| **Cas d'usage** | Classification, résumé, extraction | Rédaction, conversation, RAG |
| **Opt-out entraînement** | ✅ Par défaut (API) | ✅ Disponible |

### Règle de décision

```
Le projet manipule-t-il des données strictement UE ou le client exige-t-il
la souveraineté ?
  ├── Oui → Mistral
  └── Non → Quelle est la tâche ?
              ├── Rédaction / conversation → OpenAI (GPT-4o mini)
              ├── Classification / extraction → Mistral (Small 4, moins cher)
              └── Les deux → Commencer par Mistral, passer à OpenAI si qualité insuffisante
```

---

## 5. Stack recommandée par pack

| Pack | Automatisation | CRM | Email | LLM | Hébergement |
|------|:---:|:---:|:---:|:---:|:---:|
| **Réponse Lead** | Make | Pipedrive Lite | Brevo | Mistral Small 4 | —
| **Workflows CRM** | Make | Pipedrive Growth | Brevo | Mistral + OpenAI | —
| **Support Client IA** | n8n | HubSpot Service | Brevo | OpenAI | Scaleway DEV1-S |

---

## 6. Checklist technique avant livraison

- [ ] Tous les outils ont un compte séparé ou un espace de travail dédié au client
- [ ] MFA activé sur tous les comptes administrateur
- [ ] Les tokens API ont le scope minimal nécessaire
- [ ] Les webhooks sont sécurisés (validation de signature si disponible)
- [ ] Les secrets sont stockés hors du code (variables d'environnement Make/n8n)
- [ ] Un export des workflows est sauvegardé
- [ ] La documentation de prise en main est livrée
- [ ] Le client a les accès viewer/operator (pas admin)
