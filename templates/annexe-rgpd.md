# Annexe RGPD — Article 28

> **Annexe au contrat de prestation entre Donopot (sous-traitant) et [Client] (responsable de traitement).**
> **Date :** [JJ/MM/AAAA]

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

## 2. Sous-traitants ultérieurs

Le Client autorise le recours aux sous-traitants ultérieurs suivants,
sous réserve qu'ils présentent des garanties suffisantes :

| Sous-traitant | Rôle | Localisation des données | Garanties |
|---------------|------|--------------------------|-----------|
| **Make** (Celonis) | Plateforme d'automatisation | UE / États-Unis (AWS) | DPA signé, CCT disponibles |
| **n8n** (n8n GmbH) | Automatisation self-host ou cloud | UE (Francfort) si cloud | DPA disponible |
| **Pipedrive** | CRM | États-Unis (AWS) | DPA, CCT |
| **HubSpot** | CRM | États-Unis | DPA, CCT |
| **Brevo** (Sendinblue) | Emailing / automation | France / UE | DPA, hébergement UE |
| **Mistral AI** | LLM pour classification / rédaction | UE | API, pas de stockage des données |
| **OpenAI** | LLM pour classification / rédaction | États-Unis | DPA, CCT, opt-out entraînement |
| **Scaleway** / **OVHcloud** | Hébergement (si self-host) | France / UE | Certifications, DPA |
| **Google Workspace** | Messagerie, documents | UE / États-Unis | DPA, CCT |

Le Prestataire informe le Client de tout changement de sous-traitant ultérieur.
Le Client dispose de 15 jours pour s'y opposer pour un motif légitime.

---

## 3. Mesures techniques et organisationnelles

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

## 4. Notification d'incident

En cas de violation de données à caractère personnel :
- Notification au Client dans un délai maximal de **24 heures**
- Description de la nature de la violation, des catégories de données concernées,
  des mesures prises et des mesures proposées pour remédier à la violation
- Le Client est responsable de la notification à la CNIL dans les 72 heures
  si le risque pour les personnes l'exige

---

## 5. Sort des données en fin de contrat

Au terme du contrat :
- Restitution des données dans un format standard (CSV, JSON, export CRM)
- Suppression des données hébergées sous 30 jours
- Attestation de suppression fournie sur demande
- Les workflows sont désactivés et exportés

---

## 6. Registre des traitements

Le Prestataire tient un registre des activités de traitement pour son activité
propre (prospection, gestion commerciale, facturation) et pour chaque client.

Le Client est responsable de son propre registre des traitements.
Le Prestataire fournit les informations nécessaires pour le compléter.

---

## 7. Droits des personnes

Le Prestataire assiste le Client dans le respect de son obligation de donner suite
aux demandes d'exercice des droits des personnes : droit d'accès, de rectification,
d'opposition, de limitation, de portabilité, dans la mesure du possible compte tenu
de la nature du traitement.

---

## 8. Contact et DPO

- **Prestataire :** Donopot — donopot@pm.me
- **Client :** [Contact DPO ou responsable RGPD]

---

*Cette annexe est signée conjointement avec le contrat principal.*
