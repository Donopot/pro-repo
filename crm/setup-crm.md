# Guide de configuration — Mini-CRM interne

> **Objectif :** Suivre votre pipeline commercial sans outil payant.
> **Durée de setup :** 15 minutes.

---

## Option recommandée : Google Sheets (gratuit)

### Étape 1 — Créer la feuille

1. Ouvrir [sheets.google.com](https://sheets.google.com)
2. Fichier → Importer → Importer le fichier `crm-modele.csv`
3. Type de séparateur : **Virgule**
4. Cliquer sur « Importer les données »

### Étape 2 — Mise en forme

1. **Figer la ligne 1** (Affichage → Figer → 1 ligne) pour garder l'en-tête visible
2. **Mise en forme conditionnelle** sur la colonne `statut_pipeline` :
   - « À contacter » → fond gris clair
   - « Contactée » → fond bleu clair
   - « Démo programmée » → fond orange clair
   - « Devis envoyé » → fond jaune clair
   - « Gagné » → fond vert clair
   - « Perdu » → fond rouge clair
3. **Validation des données** sur la colonne `statut_pipeline` :
   - Données → Validation des données
   - Critères : Liste d'éléments
   - Valeurs : `À contacter, Contactée, Relancée, Démo programmée, Devis envoyé, Négociation, Gagné, Perdu`

### Étape 3 — Vues filtrées

Créer 3 vues filtrées (Données → Vues filtrées) :

| Vue | Filtre | Usage |
|-----|--------|-------|
| **À faire cette semaine** | `prochaine_action_date` = cette semaine | Planification hebdo |
| **Pipeline actif** | `statut_pipeline` ≠ Gagné, Perdu | Suivi commercial |
| **Relances urgentes** | `statut_pipeline` = Contactée, Relancée ET `date_dernier_contact` > 7 jours | Ne pas perdre le fil |

### Étape 4 — Import du fichier agences-cibles.csv

1. En bas de la feuille, cliquer sur **+** pour ajouter une feuille
2. La renommer « Cibles »
3. Fichier → Importer → `agences-cibles.csv`
4. Sur la feuille « Pipeline », copier les colonnes `nom`, `ville`, `email`, `téléphone` depuis « Cibles » quand un lead entre dans le pipeline

---

## Alternative 1 : Airtable (gratuit jusqu'à 1 000 enregistrements)

1. Créer une base depuis un CSV : **Add a base → Import data → `crm-modele.csv`**
2. Définir le type de chaque colonne :
   - `statut_pipeline` → **Single select** (avec les 8 options ci-dessus)
   - `tags` → **Multiple select**
   - `date_*` → **Date**
3. Créer des vues filtrées :
   - **Kanban** sur `statut_pipeline` (vue par étapes)
   - **Calendar** sur `prochaine_action_date` (vue calendrier)
   - **Grid** filtrée « À contacter cette semaine »

---

## Alternative 2 : Notion (gratuit)

1. Créer une base de données : **/database inline**
2. Colonnes à créer :
   - `Nom` — Title
   - `Ville` — Select
   - `Contact` — Text
   - `Statut` — Select (8 options)
   - `Prochaine action` — Date
   - `Notes` — Text
3. Vues recommandées :
   - **Tableau** principal (tous les leads)
   - **Kanban** groupé par `Statut`
   - **Calendrier** basé sur `Prochaine action`

---

## Pipeline commercial — Définitions des statuts

| Statut | Définition | Action suivante |
|--------|-----------|-----------------|
| **À contacter** | Lead identifié, pas encore contacté | Email froid ou appel dans la semaine |
| **Contactée** | Premier contact établi | Qualifier le besoin, proposer un audit |
| **Relancée** | Relance après premier contact | Si pas de réponse après 2 relances → passer en Perdu |
| **Démo programmée** | Créneau de démonstration fixé | Préparer la démo, envoyer le rappel J-1 |
| **Devis envoyé** | Devis + scope envoyés | Relance à J+3 et J+7 |
| **Négociation** | Discussion active sur le devis | Ajustements, réponses aux objections |
| **Gagné** | Devis signé, acompte reçu | Déclencher l'onboarding |
| **Perdu** | Opportunité fermée sans suite | Noter la raison, archiver après 30 jours |

---

## Routine commerciale recommandée

| Fréquence | Action | Durée |
|-----------|--------|-------|
| **Quotidien** | Vérifier la vue « À faire aujourd'hui » | 5 min |
| **Lundi matin** | Planifier les relances de la semaine | 15 min |
| **Vendredi soir** | Mettre à jour les statuts, noter les apprentissages | 10 min |
| **1er du mois** | Exporter une copie, calculer le taux de conversion | 10 min |

---

## Indicateurs à suivre

- **Taux de réponse** = Contactées / À contacter (cible > 30 %)
- **Taux de démo** = Démo programmée / Contactées (cible > 40 %)
- **Taux de conversion** = Gagné / Contactées (cible > 15 %)
- **Cycle de vente moyen** = délai entre premier contact et Gagné (cible < 30 jours)
