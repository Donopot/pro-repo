# Bloc 3 — Commercial : Plan d'exécution

> **Objectif :** Créer les outils de prospection et de conformité pour le lancement commercial.
> **Branche :** `agent/freelance/immo-block3`
> **Stratégie :** 4 sprints sur une branche unique, 1 commit par sprint.

---

## Sprint 1 — Liste 100 agences cibles

**Fichier :** `crm/agences-cibles.csv`

Format structuré importable dans un CRM :
- Nom, ville, code postal, département, région
- Taille (estimation nombre d'agents)
- Type (indépendante / réseau / digitale)
- Site web, email générique, téléphone
- Source (PagesJaunes, Google Maps, réseaux)
- Statut prospection (à contacter / contactée / relancée)
- Notes

**Critères de sélection :**
- Agences avec 3 à 30 agents (TPE/PME)
- Présence web active (site + annonces)
- France métropolitaine (hors Corse pour simplicité logistique)
- Mix : Paris/Lyon/Marseille/Bordeaux/Nantes/Lille/Toulouse + villes moyennes
- Indépendantes ET franchises (les franchises ont plus de budget)

**Vérification :** Fichier CSV valide avec exactement 100 lignes, importable dans Sheets/Airtable.

---

## Sprint 2 — Mini-CRM interne

**Fichiers :**
- `crm/crm-modele.csv` — template importable (Airtable/Sheets/Notion)
- `crm/setup-crm.md` — guide de configuration

**Schéma CRM :**
- Colonnes : ID, Nom agence, Ville, Contact principal, Email, Téléphone, Statut pipeline (À contacter → Contactée → Relancée → Démo → Devis → Gagné/Perdu), Date dernier contact, Prochaine action, Assigné à, Notes, Tags

**Guide setup :** Instructions pour importer dans Airtable (gratuit), Google Sheets (gratuit) ou Notion (gratuit). Avec vues filtrées recommandées.

---

## Sprint 3 — Registre de traitements RGPD

**Fichier :** `templates/registre-rgpd.md`

Template au format CNIL (article 30 RGPD) :
- Identité du responsable de traitement (le client)
- Finalités du traitement
- Catégories de données personnelles
- Catégories de personnes concernées
- Destinataires des données
- Durées de conservation
- Mesures de sécurité
- Sous-traitants (Make, Pipedrive, Brevo, Mistral/OpenAI)
- Transferts hors UE

Note : en tant que sous-traitant (article 28), Donopot n'est PAS responsable de traitement. Ce registre est fourni COMME MODÈLE à ses clients, qui sont responsables de traitement.

---

## Sprint 4 — Process onboarding client

**Fichiers :**
- `templates/onboarding-checklist.md` — checklist opérationnelle
- `templates/onboarding-email.md` — email type de bienvenue

**Checklist onboarding :**
- Étapes : signature contrat → acompte → collecte accès → kickoff → audit → validation périmètre → build → recette → go-live → hypercare → facturation solde
- Pour chaque étape : responsable (Donopot / Client), livrable, délai

**Email onboarding :**
- Accusé réception signature + acompte
- Récapitulatif du projet (pack, montant, délai)
- Prochaines étapes immédiates
- Liste des accès à fournir
