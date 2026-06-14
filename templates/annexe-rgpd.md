# Annexe RGPD — Article 28

> **Annexe au contrat de prestation entre Donopot (sous-traitant) et [Client] (responsable de traitement).**
> **Date :** [JJ/MM/AAAA]
>
> La présente annexe est établie conformément à l'article 28 du Règlement Général
> sur la Protection des Données (UE) 2016/679.

---

## 1. Description des traitements

| Élément | Détail |
|---------|--------|
| **Nature** | Automatisation de flux métier (réponse lead, workflows CRM, support client) |
| **Finalité** | Traitement, qualification et suivi des demandes entrantes pour le compte du Client |
| **Catégories de données** | Données d'identification (nom, prénom, email, téléphone), données professionnelles, contenu des messages |
| **Catégories de personnes** | Prospects et clients du Client |
| **Durée de conservation** | Durée du contrat + 30 jours pour la réversibilité |

---

## 2. Traitement sur instruction documentée

Le Prestataire s'engage à ne traiter les données à caractère personnel que sur
**instruction documentée du Client**, y compris en ce qui concerne les transferts
de données vers un pays tiers.

Le Prestataire informe immédiatement le Client si, selon lui, une instruction
constitue une violation du RGPD ou d'autres dispositions relatives à la protection
des données.

---

## 3. Confidentialité

Le Prestataire veille à ce que les personnes autorisées à traiter les données
à caractère personnel s'engagent à respecter la confidentialité ou soient soumises
à une obligation légale appropriée de confidentialité.

---

## 4. Sous-traitants ultérieurs

Le Client autorise le recours aux sous-traitants ultérieurs listés ci-dessous.
Le Prestataire informe le Client de tout changement envisagé concernant l'ajout
ou le remplacement de sous-traitants ultérieurs. Le Client dispose de **15 jours**
pour émettre une objection motivée.

| Sous-traitant | Rôle | Localisation | Garanties |
|---------------|------|-------------|-----------|
| **Make** (Celonis) | Automatisation | UE / US (AWS) | DPA, CCT |
| **n8n** (n8n GmbH) | Automatisation (cloud/self-host) | UE (Francfort) si cloud | DPA |
| **Pipedrive** | CRM | US (AWS) | DPA, CCT |
| **HubSpot** | CRM | US | DPA, CCT |
| **Brevo** (Sendinblue) | Emailing | France / UE | DPA, hébergement UE |
| **Mistral AI** | LLM (classification, rédaction) | UE | DPA, pas d'entraînement sur données API |
| **OpenAI** | LLM (classification, rédaction) | US | DPA, CCT, opt-out entraînement |
| **Scaleway** | Hébergement (self-host) | France / UE | Certifications, DPA |
| **OVHcloud** | Hébergement (self-host) | France / UE | Certifications, DPA |
| **Google Workspace** | Messagerie, documents | UE / US | DPA, CCT |

> ⚠️ La localisation effective et les garanties dépendent de la configuration retenue
> pour chaque projet. Le tableau ci-dessus sera précisé projet par projet dans le
> Document de Périmètre.

### Obligations répercutées

Le Prestataire impose à chaque sous-traitant ultérieur, par contrat écrit, les
mêmes obligations en matière de protection des données que celles définies dans
la présente annexe, notamment en ce qui concerne les garanties suffisantes quant
à la mise en œuvre de mesures techniques et organisationnelles appropriées.

Si un sous-traitant ultérieur ne remplit pas ses obligations, le Prestataire
demeure pleinement responsable envers le Client de l'exécution des obligations
du sous-traitant ultérieur.

---

## 5. Mesures techniques et organisationnelles

| Domaine | Mesure |
|---------|--------|
| **Authentification** | MFA sur tous les outils critiques, comptes séparés par client |
| **Gestion des secrets** | Secrets stockés dans un gestionnaire dédié, jamais en clair dans les workflows |
| **Chiffrement** | Données en transit : TLS 1.2+. Données au repos : chiffrées par les fournisseurs |
| **Sauvegarde** | Export hebdomadaire des workflows, sauvegarde quotidienne de la base si self-host |
| **Journalisation** | Logs d'exécution, alertes en cas d'échec critique |
| **Tests** | Test de bout en bout de chaque flux critique avant mise en production |
| **Accès** | Revue mensuelle des accès, suppression des comptes inutilisés |
| **Rotation des clés** | Rotation annuelle des clés API et tokens |

---

## 6. Notification d'incident

En cas de violation de données à caractère personnel :
- Notification au Client dans un délai maximal de **24 heures**
- Description de la nature de la violation, des catégories de données concernées,
  des mesures prises et des mesures proposées pour remédier à la violation
- Le Client est responsable de la notification à la CNIL dans les 72 heures
  si le risque pour les personnes l'exige

---

## 7. Assistance au Client

Le Prestataire assiste le Client, dans la mesure du possible, pour :

- Le respect de son obligation de répondre aux demandes d'exercice des droits
  des personnes : accès, rectification, opposition, limitation, portabilité
- La réalisation d'**analyses d'impact relatives à la protection des données**
  (AIPD / DPIA) lorsque le traitement présente un risque élevé
- Les **consultations préalables** auprès de la CNIL, le cas échéant

---

## 8. Audits et informations

Le Prestataire met à la disposition du Client toutes les informations nécessaires
pour démontrer le respect des obligations prévues à l'article 28 du RGPD.

Il permet des **audits**, y compris des inspections, menés par le Client ou un
mandataire qualifié, et y contribue. Ces audits sont planifiés avec un préavis
raisonnable et ne doivent pas perturber de manière disproportionnée les activités
du Prestataire.

---

## 9. Registre des traitements

Le Prestataire tient un registre des activités de traitement pour son activité
propre (prospection, gestion commerciale, facturation) et pour chaque client.

Le Client est responsable de son propre registre. Le Prestataire fournit les
informations nécessaires pour le compléter.

---

## 10. Sort des données en fin de contrat

Au terme du contrat, selon le choix du Client :

- Restitution des données dans un format standard (CSV, JSON, export CRM)
- Suppression de toutes les copies des données à caractère personnel
- Attestation de suppression fournie sur demande
- Les workflows sont désactivés et exportés

Ce traitement intervient dans un délai maximal de **30 jours** suivant la fin
du contrat, sauf obligation légale de conservation.

---

## 11. Contact

- **Prestataire :** Donopot — donopot@pm.me
- **Client :** [Contact DPO ou responsable RGPD — à compléter]

---

*Cette annexe est signée conjointement avec le contrat principal et le Document de Périmètre.*
