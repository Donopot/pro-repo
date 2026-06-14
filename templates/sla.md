# Annexe 2 — Conditions de maintenance et SLA

> **Annexe au contrat de prestation entre Donopot et [Client].**
> **Date :** [JJ/MM/AAAA]

---

## 1. Périmètre de la maintenance

La maintenance couvre les services suivants pour les automatisations livrées :

| Service | Détail |
|---------|--------|
| **Supervision** | Surveillance quotidienne des workflows (exécutions, erreurs, latence) |
| **Correctif** | Correction des dysfonctionnements et bugs |
| **Ajustement** | Modifications mineures (changement de champ, destinataire, seuil, template) |
| **Support** | Assistance par email, réponse sous 1 jour ouvré |
| **Mise à jour** | Mise à jour des connecteurs et API des outils tiers |
| **Reporting** | Rapport mensuel d'activité (volumes, erreurs, temps économisé) |
| **Optimisation** | 1 à 2 optimisations mineures incluses par mois |

La maintenance ne couvre pas :
- Nouvelles fonctionnalités ou nouveaux flux
- Nouvelles intégrations non prévues au périmètre initial
- Refonte ou migration de plateforme
- Rédaction de contenu

---

## 2. Niveaux de service (SLA)

| Niveau | Définition | Exemple | Engagement |
|--------|------------|---------|------------|
| **P1 — Critique** | Interruption complète d'un workflow bloquant la réception ou le traitement des leads | Plus aucun lead ne remonte dans le CRM | Prise en charge sous **4 heures ouvrées**, résolution sous **8 heures ouvrées** |
| **P2 — Dégradé** | Dysfonctionnement partiel, le service fonctionne mais avec dégradation | Relances automatiques incomplètes, erreur non bloquante | Prise en charge sous **1 jour ouvré**, résolution sous **3 jours ouvrés** |
| **P3 — Mineur** | Ajustement, correction cosmétique ou optimisation | Changement de template, modification de seuil | Planification sous **5 jours ouvrés** |

---

## 3. Conditions d'application du SLA

Le SLA s'entend sous réserve que :

- Le Client fournisse les accès nécessaires dans un délai raisonnable
- L'incident ne provienne pas d'un tiers sur lequel le Prestataire n'a aucun contrôle
  (ex : panne de l'API Pipedrive, interruption de service Brevo)
- Aucune modification non documentée n'ait été réalisée côté Client
- La demande soit transmise par le canal défini (email)

---

## 4. Horaires et canaux

| Élément | Détail |
|---------|--------|
| **Jours ouvrés** | Lundi au vendredi, hors jours fériés français |
| **Heures ouvrées** | 9h00 – 18h00 (heure de Paris) |
| **Canal de support** | Email à donopot@pm.me |
| **Canal d'urgence P1** | Email + SMS (numéro communiqué au Client) |

---

## 5. Process d'incident

```
Détection (Prestataire ou Client)
        ↓
Qualification du niveau P1/P2/P3
        ↓
Accusé de réception (selon délai SLA)
        ↓
Diagnostic + correction
        ↓
Confirmation de résolution
        ↓
Post-mortem si P1 (résumé envoyé sous 48h)
```

---

## 6. Engagement de maintenance

La maintenance est conclue pour une durée initiale de **3 mois**, renouvelable
par tacite reconduction par période de 3 mois. Résiliation par préavis d'**1 mois**.

---

## 7. Tarifs

| Pack | Maintenance mensuelle (HT) |
|------|---------------------------:|
| Pack Réponse Lead | 250 – 600 € |
| Pack Workflows CRM | 400 – 900 € |
| Pack Support Client IA | 700 – 1 500 € |

Le tarif définitif est fixé au contrat en fonction de la complexité du projet.

---

*Cette annexe est signée conjointement avec le contrat principal.*
