# Registre des activités de traitement — Modèle (Article 30 RGPD)

> **⚠️ IMPORTANT :** Ce document est un **modèle fourni par Donopot à ses clients**.
> Donopot agit en qualité de **sous-traitant** (article 28). Le **responsable de traitement**
> est le Client. C'est au Client qu'incombe l'obligation de tenir ce registre.
>
> Ce modèle couvre les traitements automatisés mis en place par Donopot dans le cadre
> des packs Réponse Lead, Workflows CRM et Support Client IA.
>
> **À personnaliser par le client avant mise en conformité CNIL.**

---

## 1. Identité du responsable de traitement

| Champ | Valeur |
|-------|--------|
| **Raison sociale** | [À compléter] |
| **Forme juridique** | [À compléter] |
| **SIRET** | [À compléter] |
| **Adresse** | [À compléter] |
| **Représentant légal** | [Nom, qualité] |
| **DPO / Référent RGPD** | [Nom/email ou « Non désigné »] — évaluer la désignation selon les critères de l'article 37 RGPD, indépendamment d'un seuil d'effectif |

---

## 2. Traitement n° 1 — Réponse automatique aux leads

### Finalité

Qualifier, affecter et répondre automatiquement aux demandes entrantes
(formulaires web, portails d'annonces, emails) pour les agences immobilières.

### Catégories de données personnelles

| Donnée | Source | Obligatoire ? |
|--------|--------|:---:|
| Nom, prénom | Formulaire de contact | Oui |
| Email | Formulaire de contact | Oui |
| Téléphone | Formulaire de contact | Non |
| Type de bien (appartement, maison) | Formulaire de contact | Non |
| Surface estimée | Formulaire de contact | Non |
| Ville / code postal | Formulaire de contact | Oui |
| Budget estimatif | Formulaire de contact | Non |
| Message libre | Formulaire de contact | Non |
| Date et heure de la demande | Automatique | Oui |
| Historique des relances | Automatique | Oui |

### Catégories de personnes concernées

- Prospects ayant soumis un formulaire de contact ou un email
- Clients existants sollicitant une nouvelle prestation

### Destinataires des données

| Destinataire | Rôle | Données transmises |
|-------------|------|-------------------|
| **Agent commercial assigné** | Interne | Nom, email, téléphone, détails de la demande |
| **Donopot (sous-traitant)** | Maintenance technique | Toutes (accès technique nécessaire) |
| **Make** (sous-traitant ultérieur) | Automatisation | Toutes (transit) |
| **Pipedrive** (sous-traitant ultérieur) | CRM | Nom, email, téléphone, type de bien, ville, surface, historique |
| **Brevo** (sous-traitant ultérieur) | Envoi d'emails | Nom, email |
| **Mistral AI / OpenAI** (sous-traitant ultérieur) | Analyse et qualification | Contenu du message, type de bien, ville |

### Durées de conservation

| Donnée | Durée | Sort |
|--------|-------|------|
| Données des leads | 3 ans après le dernier contact | Suppression |
| Données des clients | 5 ans après la fin de la relation commerciale | Suppression |
| Logs techniques d'automatisation | [Durée configurée et vérifiée dans le contrat/compte] | Suppression ou anonymisation selon la configuration |

### Mesures de sécurité

| Mesure | Détail |
|--------|--------|
| **Authentification** | MFA sur tous les outils (Make, Pipedrive, Brevo) |
| **Chiffrement** | Vérifier et documenter les mécanismes réellement applicables dans les contrats et configurations retenus |
| **Gestion des secrets** | API tokens stockés dans le gestionnaire de variables Make, pas en clair dans le code |
| **Journalisation** | Logs d'exécution Make, logs d'accès Pipedrive |
| **Sauvegarde** | Définir fréquence, périmètre, rétention et test de restauration selon l'offre réellement souscrite |
| **Procédure d'incident** | Notification Client sous 24h, notification CNIL sous 72h si nécessaire |

---

## 3. Traitement n° 2 — Workflows CRM automatisés

### Finalité

Automatiser la création, la mise à jour, le dédoublonnage et le suivi des
fiches contacts et deals dans le CRM.

### Données personnelles supplémentaires (par rapport au traitement n° 1)

| Donnée | Source | Obligatoire ? |
|--------|--------|:---:|
| Historique des transactions | CRM | Oui |
| Étape dans le pipeline | Automatique | Oui |
| Date des relances | Automatique | Oui |
| Notes internes agent | Agent commercial | Non |
| Documents attachés (compromis, diagnostics) | Agent / Client | Non |

### Destinataires supplémentaires (par rapport au traitement n° 1)

| Destinataire | Rôle | Données transmises |
|-------------|------|-------------------|
| **HubSpot** (si alternative CRM) | CRM alternatif | Identiques à Pipedrive |

### Durées de conservation

Identiques au traitement n° 1.

---

## 4. Traitement n° 3 — Support Client IA

### Finalité

Trier, catégoriser et répondre automatiquement aux demandes de support client,
avec transmission à un humain si nécessaire.

### Données personnelles supplémentaires

| Donnée | Source | Obligatoire ? |
|--------|--------|:---:|
| Contenu des demandes de support | Email, formulaire, chat | Oui |
| Historique des échanges | Automatique | Oui |
| Pièces jointes éventuelles | Client | Non |

### Destinataires supplémentaires

| Destinataire | Rôle | Données transmises |
|-------------|------|-------------------|
| **Base de connaissances vectorielle** (Mistral/OpenAI) | Recherche sémantique | Contenu des demandes (anonymisé si possible) |
| **Équipe support client** | Traitement humain | Nom, email, contenu de la demande |

### Durées de conservation

| Donnée | Durée |
|--------|-------|
| Tickets de support | 3 ans après clôture |
| Transcripats de chat | 1 an après clôture |

---

## 5. Sous-traitants ultérieurs — Détail

Conformément à l'article 28.2, le Client documente et autorise uniquement les
sous-traitants réellement utilisés après vérification de leur DPA et de la
configuration souscrite. Ne pas déduire la localisation, les certifications ou
les garanties de transfert du seul nom du fournisseur.

| Sous-traitant / service | Région et configuration retenues | Transfert hors UE | Mécanisme applicable | Preuve et date de vérification |
|-------------------------|----------------------------------|-------------------|----------------------|-------------------------------|
| [À compléter] | [À compléter] | [Oui / Non / À vérifier] | [Adéquation, CCT, autre] | [DPA/contrat/configuration + date] |

> Pour tout nouveau sous-traitant ultérieur, Donopot informe le Client par écrit
> avec un préavis de 15 jours. Le Client peut s'y opposer par écrit motivé.

---

## 6. Transferts hors Union Européenne

Pour chaque outil réellement utilisé, vérifier les flux, la région configurée,
les accès de support, les sous-traitants ultérieurs et le DPA à la date du
déploiement. Documenter le mécanisme applicable à chaque transfert et, si
nécessaire, l'analyse de risque et les mesures supplémentaires. Faire valider
les conclusions par le responsable de traitement ou son conseil.

---

## 7. Exercice des droits des personnes

Le Client, en tant que responsable de traitement, est l'interlocuteur unique des
personnes concernées pour l'exercice de leurs droits (accès, rectification,
opposition, portabilité, effacement, limitation).

Donopot, en tant que sous-traitant, s'engage à :
- Assister le Client pour répondre aux demandes d'exercice des droits
- Fournir les données dans un format structuré (CSV/JSON) sous 48h ouvrées
- Notifier le Client de toute demande reçue directement par erreur

---

## 8. Analyse d'impact (AIPD)

La nécessité d'une AIPD doit être évaluée pour chaque traitement réel, avant
mise en production et à chaque évolution importante. Documenter notamment :

- l'évaluation ou le scoring, y compris le profilage ;
- les décisions automatisées ayant un effet juridique ou significatif ;
- la surveillance systématique ;
- les données sensibles ou hautement personnelles ;
- le traitement à grande échelle ;
- le croisement ou la combinaison de jeux de données ;
- les personnes vulnérables ;
- l'usage innovant ou de nouvelles technologies ;
- l'exclusion d'un droit, d'un service ou d'un contrat.

Si le traitement est susceptible d'engendrer un risque élevé, figure sur une
liste imposant une AIPD, ou cumule plusieurs critères pertinents, réaliser
l'AIPD. La décision et sa justification doivent être validées par le responsable
de traitement et, lorsqu'il existe, par le DPO ou le conseil juridique.

---

*Document fourni à titre indicatif par Donopot. À adapter et compléter par le
responsable de traitement. Dernière mise à jour : 2026-06-14.*
