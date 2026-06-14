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
   - « Opposition » → fond noir, texte blanc
3. **Validation des données** sur la colonne `statut_pipeline` :
   - Données → Validation des données
   - Critères : Liste d'éléments
   - Valeurs : `À qualifier, À contacter, Contactée, Relancée, Démo programmée, Devis envoyé, Négociation, Gagné, Perdu, Opposition`

### Étape 3 — Vues filtrées

Créer 3 vues filtrées (Données → Vues filtrées) :

| Vue | Filtre | Usage |
|-----|--------|-------|
| **À faire cette semaine** | `prochaine_action_date` = cette semaine | Planification hebdo |
| **Pipeline actif** | `statut_pipeline` ≠ Gagné, Perdu, Opposition ET `ne_plus_contacter` ≠ Oui | Suivi commercial |
| **Relances urgentes** | `statut_pipeline` = Contactée ou Relancée ET `date_dernier_contact` ≤ `AUJOURDHUI()-7` ET `ne_plus_contacter` ≠ Oui | Ne pas perdre le fil |
| **Liste d'opposition** | `ne_plus_contacter` = Oui | Exclure de toute sollicitation |

### Étape 4 — Import du fichier agences-cibles.csv

1. En bas de la feuille, cliquer sur **+** pour ajouter une feuille
2. La renommer « Cibles »
3. Fichier → Importer → `agences-cibles.csv`
4. Ne copier une cible dans « Pipeline » que si `verification_status` vaut `verifie`, que `source_url`, `date_collecte` et `date_verification` sont renseignées, et que `opposition` ne vaut pas `Oui`

### Règles obligatoires avant toute prospection

- Vérifier manuellement l'identité, le domaine, les coordonnées professionnelles et la pertinence du message.
- Conserver l'URL exacte de la source publique et les dates de collecte et de vérification.
- Ne jamais contacter une ligne d'exemple, non vérifiée, ou marquée `opposition` / `ne_plus_contacter`.
- Identifier clairement l'expéditeur et proposer dans chaque sollicitation un moyen simple et gratuit de s'opposer.
- En cas d'opposition, renseigner immédiatement `opposition_date`, `ne_plus_contacter=Oui`, le motif, puis conserver uniquement les informations minimales nécessaires à la liste d'opposition.

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
| **Opposition** | Le destinataire refuse toute prospection | Exclure immédiatement de toutes les campagnes |

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

Calculer les taux sur une cohorte et une période identiques, à partir d'événements datés, pas à partir du stock actuel de chaque statut :

- **Taux de réponse** = nombre de prospects ayant répondu / nombre de prospects contactés
- **Taux de démo** = nombre de démos programmées / nombre de prospects contactés
- **Taux de conversion** = nombre d'opportunités gagnées / nombre de prospects contactés
- **Taux d'opposition** = nombre d'oppositions / nombre de prospects contactés
- **Cycle de vente moyen** = délai entre premier contact et Gagné (cible < 30 jours)
