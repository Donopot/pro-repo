# Base documentaire — Support Client IA

> **Pack :** Support Client IA
> **Usage :** Base de connaissances pour le tri, la réponse automatique et le handoff humain.
> **Mise à jour :** À personnaliser par client avant mise en production.

---

## 1. FAQ — Agence immobilière type

### 🏠 Estimation

| Question | Réponse |
|----------|---------|
| Comment faire estimer mon bien ? | Vous pouvez remplir notre formulaire d'estimation en ligne ou prendre rendez-vous avec un agent. L'estimation est gratuite et sans engagement. |
| Combien coûte une estimation ? | L'estimation est entièrement gratuite. |
| Combien de temps prend une estimation ? | Comptez 30 à 45 minutes pour une visite complète du bien. |
| Quels documents fournir pour une estimation ? | [À valider avec l'agence : liste des documents demandés et caractère obligatoire ou facultatif.] |

### 🔑 Visite

| Question | Réponse |
|----------|---------|
| Comment organiser une visite ? | Contactez l'agent en charge du bien ou réservez un créneau directement via le lien de l'annonce. |
| Puis-je visiter le week-end ? | [À valider avec l'agence : jours et horaires de visite.] |
| Faut-il une pièce d'identité pour visiter ? | [À valider avec l'agence : politique d'identification avant visite.] |
| Puis-je être accompagné pendant la visite ? | Bien sûr, vous pouvez venir accompagné. |

### 📋 Mandat

| Question | Réponse |
|----------|---------|
| Quels types de mandat proposez-vous ? | Mandat simple (non exclusif) et mandat exclusif. Le mandat exclusif inclut des services premium (photos pro, home staging, diffusion élargie). |
| Quelle est la durée d'un mandat ? | [À valider avec l'agence : durées et modalités de renouvellement par type de mandat.] |
| Quels sont vos honoraires ? | [À valider avec l'agence : barème d'honoraires applicable et lien vers le barème public.] |
| Puis-je vendre moi-même sans commission ? | [À valider avec l'agence selon les clauses du mandat signé.] |

### 💰 Financement

| Question | Réponse |
|----------|---------|
| Proposez-vous un courtier ? | Oui, nous travaillons avec des courtiers partenaires. Nous pouvons vous mettre en relation. |
| Quels sont les frais de notaire ? | Environ 7-8% du prix dans l'ancien, 2-3% dans le neuf. |
| Puis-je acheter sans apport ? | C'est possible dans certains cas. Nous vous recommandons d'en parler avec notre courtier partenaire. |

### 🛠 Technique / Administratif

| Question | Réponse |
|----------|---------|
| Comment sont diffusées mes annonces ? | Sur notre site, les portails partenaires (SeLoger, Leboncoin, Bien'ici) et nos réseaux sociaux. |
| Comment suivre l'avancement de ma vente ? | Vous avez accès à votre espace client en ligne. Votre agent vous tient également informé par email et téléphone. |
| Où se situe votre agence ? | [Adresse de l'agence — à personnaliser]. |
| Quels sont vos horaires ? | [Horaires de l'agence — à personnaliser]. |

---

## 2. Arborescence des catégories

```
Support Client
├── 🏠 Estimation
│   ├── Process
│   ├── Prix
│   └── Documents
├── 🔑 Visite
│   ├── Réservation
│   ├── Disponibilités
│   └── Préparation
├── 📋 Mandat
│   ├── Types
│   ├── Honoraires
│   └── Durée
├── 💰 Financement
│   ├── Courtier
│   ├── Prêt
│   └── Frais de notaire
├── 🛠 Technique
│   ├── Diffusion annonces
│   ├── Suivi vente
│   └── Agence
└── 🔄 After-sales / Réclamation
    ├── Suivi de dossier
    ├── Réclamation
    └── Demande de rappel
```

---

## 3. Règles de handoff humain

Le chatbot escalade à un humain si :

| Condition | Action |
|-----------|--------|
| Score de confiance < 70% | « Je transfère votre demande à un agent qui vous répondra rapidement. » |
| Mention de mots-clés d'urgence : « urgent », « problème », « plainte », « mécontent » | Transfert immédiat avec priorité haute |
| Demande de rendez-vous complexe (plusieurs créneaux, contraintes spécifiques) | Transfert à l'assistant administratif |
| Question hors base documentaire après 2 tentatives de reformulation | « Je n'ai pas la réponse pour le moment. Un agent va prendre le relais. » |
| Le client demande explicitement à parler à un humain | Transfert immédiat |

---

## 4. Runbook opérateur

### Quotidien (5 min)

- [ ] Vérifier le dashboard Make : toutes les exécutions en vert ?
- [ ] Vérifier les conversations en attente de handoff
- [ ] Traiter les escalades de la veille (max 24h de délai)

### Hebdomadaire (15 min)

- [ ] Analyser les 5 conversations les plus longues → la FAQ est-elle incomplète ?
- [ ] Vérifier le taux de handoff → s'il dépasse 30 %, enquêter
- [ ] Ajouter les nouvelles questions récurrentes à la FAQ
- [ ] Exporter les logs et les archiver

### Mensuel (30 min)

- [ ] Rapport KPI : taux de résolution, temps moyen, satisfaction
- [ ] Revue des catégories les plus sollicitées
- [ ] Optimisation des réponses : reformuler les FAQ mal notées
- [ ] Réunion avec le client : présentation du rapport + suggestions d'amélioration

---

## 5. KPIs à suivre

| Métrique | Cible | Alerte si |
|----------|-------|-----------|
| Taux de résolution sans humain | > 60 % | < 50 % |
| Temps moyen de première réponse | < 30 secondes | > 2 minutes |
| Taux de handoff | < 25 % | > 35 % |
| Délai de traitement des handoffs | < 4h ouvrées | > 24h |
| Satisfaction (post-conversation) | > 4/5 | < 3,5/5 |
| Taux d'abandon avant réponse | < 10 % | > 20 % |

---

## 6. Initialisation chez un client

1. **Audit des questions fréquentes** — interview de l'équipe support : quelles sont les 20 questions qui reviennent tout le temps ?
2. **Rédaction des réponses** — avec le client, pour garantir l'exactitude ; aucune réponse entre crochets ne doit rester avant mise en production
3. **Intégration dans la base documentaire** — format structuré (question → réponse → catégorie)
4. **Test en dry-run** — 50 vraies conversations historiques passées dans le système, vérification des réponses
5. **Ajustement** — correction des erreurs, enrichissement de la FAQ
6. **Go-live** — activation sur le canal choisi (chat site web, email, WhatsApp)
7. **Hypercare 7 jours** — surveillance renforcée, handoff systématique si doute

---

*Ce document est un modèle. Toute la section FAQ doit être remplacée par les questions/réponses réelles du client.*
