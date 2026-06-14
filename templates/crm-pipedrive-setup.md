# Template CRM — Pipedrive pour agence immobilière

> **Plan Pipedrive recommandé :** Professional (39 $/poste/mois) pour les automatisations, webhooks et champs personnalisés illimités.
> **Alternative budget :** Pipedrive Lite (14 $/poste/mois) si champs personnalisés limités acceptables.

---

## 1. Pipeline « Transactions immobilières »

| Ordre | Étape | Description | Action automatique déclenchée |
|-------|-------|-------------|-------------------------------|
| 1 | **Nouveau lead** | Lead entrant, non encore contacté | Réponse auto envoyée (Make) |
| 2 | **Contacté** | Premier contact établi | Tâche « Planifier visite » créée |
| 3 | **Visite planifiée** | Rendez-vous physique ou visio calé | Rappel J-1 par email |
| 4 | **Offre envoyée** | Proposition commerciale transmise | Relance J+3 si pas de réponse |
| 5 | **Négociation** | Discussion active sur le prix/conditions | |
| 6 | **Mandat signé** | ✅ Gagné | Tâche « Onboarding vendeur » |
| 7 | **Perdu** | ❌ Lead perdu ou parti chez concurrent | Email de courtoisie |

---

## 2. Champs personnalisés

### Sur le Deal

| Champ | Type | Valeurs / Exemple | Obligatoire |
|-------|------|-------------------|:----------:|
| `type_bien` | Liste | Appartement, Maison, Terrain, Local commercial, Parking | ✅ |
| `type_demande` | Liste | Estimation, Visite, Vente, Location, Gestion | ✅ |
| `surface` | Numérique | 65 (m²) | |
| `nb_pieces` | Numérique | 3 | |
| `budget` | Monétaire | 350000 | |
| `ville` | Texte | Paris | ✅ |
| `code_postal` | Texte | 75015 | ✅ |
| `source_lead` | Liste | Site web, Portail annonces, Téléphone, Recommandation, Réseaux sociaux | ✅ |
| `urgence` | Liste | 🔴 Chaud (prêt à signer), 🟡 Tiède (en réflexion), 🟢 Froid (simple curiosité) | |
| `date_visite` | Date | 2026-06-20 | |
| `montant_estimation` | Monétaire | 320000 | |
| `concurrent` | Texte | Nom de l'agence concurrente | |

### Sur le Contact

| Champ | Type | Description |
|-------|------|-------------|
| `type_client` | Liste | Vendeur, Acheteur, Locataire, Bailleur |
| `secteur` | Liste | Paris 15, Boulogne, Issy-les-Moulineaux… |
| `date_dernier_contact` | Date | Mise à jour automatique |
| `source_originale` | Texte | Conservé même si le lead revient plus tard |

---

## 3. Vues filtrées

| Vue | Filtre | Usage |
|-----|--------|-------|
| **🔥 Leads chauds** | Étape = Nouveau lead OU Contacté ; urgence = 🔴 | Dashboard quotidien du manager |
| **📅 Visites cette semaine** | date_visite dans les 7 prochains jours | Briefing lundi matin |
| **⏳ Sans réponse > 48h** | Étape = Contacté ; dernière activité > 48h | Relances à faire |
| **💰 Mandats en cours** | Étape = Mandat signé | Suivi des mandats actifs |
| **📊 Mes deals** | Propriétaire = Moi | Vue personnelle par agent |
| **🏠 Par type de bien** | Regroupé par type_bien | Analyse du portefeuille |

---

## 4. Activités automatiques

| Déclencheur | Activité créée | Assignée à | Délai |
|-------------|---------------|------------|-------|
| Deal créé (étape 1) | « Premier contact » | Propriétaire du deal | Immédiat |
| Deal passe étape 2 | « Planifier visite » | Propriétaire du deal | Immédiat |
| Visite programmée (date_visite remplie) | « Rappel J-1 visite » | Propriétaire du deal | J-1 avant date_visite |
| Deal passe étape 4 | « Relance offre J+3 » | Propriétaire du deal | J+3 |
| Deal inactif > 7 jours | « Relance lead inactif » | Propriétaire du deal | J+7 |
| Deal passe étape 6 | « Onboarding vendeur — documents » | Assistant / Admin | Immédiat |
| Deal passe étape 7 | « Email courtoisie perdu » | Automatique (Brevo) | Immédiat |

---

## 5. Configuration Make → Pipedrive

### Webhooks Pipedrive à activer

Dans Pipedrive > Paramètres > Webhooks :

| Événement | URL Make | Usage |
|-----------|----------|-------|
| `deal.updated` | `https://hook.make.com/xxx` | Surveiller les changements d'étape |
| `deal.added` | `https://hook.make.com/xxx` | Notifier d'un nouveau deal créé manuellement |

### Variables d'environnement Make

| Variable | Exemple |
|----------|---------|
| `PIPEDRIVE_API_TOKEN` | `xxx` |
| `PIPEDRIVE_COMPANY_DOMAIN` | `agence-duport` |

> Dans Make, les variables se configurent via l'onglet « Variables » du scénario, pas avec la syntaxe `KEY=VALUE`.

---

## 6. Checklist d'installation chez un client

- [ ] Créer le pipeline « Transactions immobilières » avec les 7 étapes
- [ ] Ajouter les 11 champs personnalisés sur le Deal
- [ ] Ajouter les 4 champs personnalisés sur le Contact
- [ ] Créer les 6 vues filtrées
- [ ] Activer les webhooks Pipedrive
- [ ] Configurer les variables d'environnement dans Make
- [ ] Importer les contacts existants (CSV → Pipedrive)
- [ ] Tester le flux complet : formulaire → deal → email
- [ ] Former les agents (30 min) : comment lire le pipeline, mettre à jour une étape, ajouter une note

---

## 7. Bonnes pratiques

- **Ne pas créer trop d'étapes.** 7 étapes, c'est le bon équilibre entre visibilité et simplicité.
- **Un deal = un bien.** Si un client vend deux biens, créer deux deals distincts.
- **Mettre à jour l'étape manuellement après chaque interaction.** L'automatisation gère l'entrée et le suivi, l'humain gère la progression.
- **Nettoyer les deals perdus une fois par mois.** Les archiver ou les supprimer pour garder le pipeline lisible.
- **Utiliser les notes pour tracer.** Chaque email, appel, visite → une note dans le deal.
