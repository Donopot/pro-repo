# Plan — Bloc 2 : Stack & Démos

> **Branche :** `agent/freelance/immo-block2`
> **Repo :** `Donopot/pro-repo`

**Objectif :** Produire les assets techniques du Bloc 2 : démo scriptée, workflow d'automatisation, template CRM, base documentaire support client.

**Architecture :** Dossier `demos/` pour les scripts et exports de workflow, `templates/` pour les configurations CRM et la FAQ.

---

## 🗺️ Sprints

| Sprint | Contenu | Fichiers |
|--------|---------|----------|
| **S1** | Script de démo Loom "réponse lead immobilier" | `demos/loom-script-reponse-lead.md` |
| **S2** | Workflow Make — réponse lead avec qualification + CRM | `demos/workflow-reponse-lead.json` + documentation |
| **S3** | Template CRM Pipedrive (pipelines, champs, vues) | `templates/crm-pipedrive-setup.md` |
| **S4** | Base documentaire FAQ + runbook support client IA | `templates/faq-support-ia.md` |

---

## Sprint 1 — Script de démo Loom

**Fichier :** `demos/loom-script-reponse-lead.md`

**Objectif :** Script prêt à filmer pour une démo de 5-7 minutes montrant le flux complet.

**Structure du script :**

1. **Hook (0:00-0:30)** — "Voici ce qui arrive quand un prospect remplit un formulaire d'estimation sur le site d'une agence immobilière."
2. **Contexte (0:30-1:00)** — Écran du formulaire, l'agence, le problème actuel
3. **Déclencheur (1:00-1:30)** — Le formulaire est soumis → le lead arrive dans Make
4. **Workflow (1:30-4:00)** — Déroulé pas à pas :
   - Réception et parsing
   - Détection doublon dans Pipedrive
   - Classification du lead (estimation/visite/vente)
   - Création/MAJ contact dans CRM
   - Réponse email personnalisée
   - Assignation au bon agent
   - Proposition de créneau (Calendly)
   - Relance programmée si pas de réponse
5. **Monitoring (4:00-5:00)** — Dashboard Make, logs, alertes
6. **Résultat (5:00-6:00)** — Avant/après : temps de réponse, CRM rempli, agent notifié
7. **CTA (6:00-7:00)** — "Vous voulez la même chose pour votre agence ? Audit offert."

---

## Sprint 2 — Workflow Make

**Fichier :** `demos/workflow-reponse-lead.json` + `demos/workflow-reponse-lead.md`

**Objectif :** Spécification JSON conceptuelle utilisable comme base pour reproduire le workflow dans Make.

**Modules :**

1. **Webhook** — Réception du lead (JSON depuis formulaire)
2. **Variables de qualification** — Catégorie, template et assignation selon le type
3. **Pipedrive → Search persons** — Détection doublon par email
4. **Pipedrive → Create/Update person** — Création ou mise à jour
5. **Pipedrive → Create deal** — Création deal avec étape et valeur
6. **Text parser** — Composition email (template avec variables)
7. **Brevo → Send email** — Envoi réponse personnalisée
8. **Pipedrive → Update deal** — Programmation de la date de relance
9. **Scénario planifié séparé** — Recherche périodique des deals à relancer
10. **Brevo → Send email (relance)** — Relance puis marquage du deal

**Documentation :** `demos/workflow-reponse-lead.md` explique chaque module, les variables, et comment adapter.

---

## Sprint 3 — Template CRM Pipedrive

**Fichier :** `templates/crm-pipedrive-setup.md`

**Objectif :** Guide de configuration Pipedrive pour une agence immobilière.

**Contenu :**

1. **Pipeline "Transactions immobilières"** — Étapes : Nouveau lead → Contacté → Visite planifiée → Offre envoyée → Négociation → Mandat signé / Perdu
2. **Champs personnalisés** — Type de bien, surface, budget, localisation, source du lead, date de visite, urgence
3. **Vues filtrées** — Leads chauds (pas de réponse sous 24h), visites cette semaine, mandats en cours
4. **Activités automatiques** — Tâche "Rappeler" après 48h sans réponse, "Relancer" après visite sans offre
5. **Webhooks** — Configuration pour recevoir les événements depuis Make

---

## Sprint 4 — Base FAQ + Runbook support IA

**Fichier :** `templates/faq-support-ia.md`

**Objectif :** Template de base documentaire pour le Pack Support Client IA.

**Structure :**

1. **FAQ agence immobilière** — 15-20 questions/réponses types (estimation, visite, mandat, frais, financement…)
2. **Arborescence de catégories** — Estimation · Visite · Mandat · Financement · Technique · After-sales
3. **Règles de handoff** — Quand escalader à un humain (score de confiance < 70%, mention "urgence", demande de rendez-vous complexe)
4. **Runbook opérateur** — Procédure quotidienne/hebdo de supervision du support IA
5. **KPIs** — Taux de résolution sans humain, temps moyen de réponse, satisfaction
