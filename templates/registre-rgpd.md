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
| **DPO / Référent RGPD** | [Nom, email] — obligatoire si + de 20 salariés, recommandé sinon |

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
| Logs techniques (Make) | 30 jours (rétention Make par défaut) | Suppression automatique |

### Mesures de sécurité

| Mesure | Détail |
|--------|--------|
| **Authentification** | MFA sur tous les outils (Make, Pipedrive, Brevo) |
| **Chiffrement** | HTTPS (transit), AES-256 (stockage Pipedrive/Brevo) |
| **Gestion des secrets** | API tokens stockés dans le gestionnaire de variables Make, pas en clair dans le code |
| **Journalisation** | Logs d'exécution Make, logs d'accès Pipedrive |
| **Sauvegarde** | Sauvegardes quotidiennes Pipedrive (rétention 30 jours) |
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

Conformément à l'article 28.2, le Client autorise le recours aux sous-traitants
ultérieurs suivants, qui présentent des garanties suffisantes en matière de sécurité :

| Sous-traitant | Localisation données | Certifications | Lien DPA |
|--------------|---------------------|----------------|----------|
| **Make** (Celonis) | UE (Allemagne) | ISO 27001, SOC 2 | [make.com/en/legal/data-processing-agreement](https://www.make.com/en/legal/data-processing-agreement) |
| **Pipedrive** | UE (Estonie) | ISO 27001, SOC 2 | [pipedrive.com/en/privacy](https://www.pipedrive.com/en/privacy) |
| **Brevo** (ex-Sendinblue) | UE (France) | ISO 27001 | [brevo.com/fr/legal/privacypolicy](https://www.brevo.com/fr/legal/privacypolicy/) |
| **Mistral AI** | UE (France) | En cours | [mistral.ai/terms](https://mistral.ai/terms/) |
| **OpenAI** (si utilisé) | États-Unis (DPF) | SOC 2, Data Privacy Framework | [openai.com/policies/data-processing-addendum](https://openai.com/policies/data-processing-addendum) |
| **HubSpot** (si utilisé) | États-Unis (DPF) | ISO 27001, SOC 2 | [hubspot.com/data-privacy](https://www.hubspot.com/data-privacy) |

> Pour tout nouveau sous-traitant ultérieur, Donopot informe le Client par écrit
> avec un préavis de 15 jours. Le Client peut s'y opposer par écrit motivé.

---

## 6. Transferts hors Union Européenne

Les données sont hébergées et traitées prioritairement dans l'UE.

| Outil | Transfert hors UE ? | Mécanisme de conformité |
|-------|:---:|------------------------|
| Make | Non | Données hébergées en Allemagne |
| Pipedrive | Non | Données hébergées en Estonie |
| Brevo | Non | Données hébergées en France |
| Mistral AI | Non | Données hébergées en France |
| OpenAI | **Oui** (si utilisé) | Data Privacy Framework (DPF) — décision d'adéquation 2023 |
| HubSpot | **Oui** (si utilisé) | Data Privacy Framework (DPF) + Clauses contractuelles types |

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

Une AIPD est-elle obligatoire ?

| Critère | Traitement n° 1 (Lead) | n° 2 (CRM) | n° 3 (Support) |
|---------|:---:|:---:|:---:|
| Profilage ou évaluation systématique | Non | Non | Non |
| Décision automatisée produisant des effets juridiques | Non | Non | Non |
| Surveillance systématique à grande échelle | Non | Non | Non |
| Données sensibles (art. 9) | Non | Non | Non |
| Données à grande échelle | Non (PME) | Non (PME) | Non (PME) |
| **AIPD obligatoire ?** | **Non** | **Non** | **Non** |

> Si votre agence traite plus de 10 000 leads/an ou utilise un scoring automatisé
> (ex : notation des leads), une AIPD devient obligatoire. Contactez votre DPO.

---

*Document fourni à titre indicatif par Donopot. À adapter et compléter par le
responsable de traitement. Dernière mise à jour : 2026-06-14.*
