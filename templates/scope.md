# Document de périmètre — Modèle

> **Projet :** [Nom du projet]
> **Client :** [Nom du client]
> **Date :** [JJ/MM/AAAA]
> **Version :** 1.0

---

## 1. Objectif du projet

Le projet vise à mettre en place [description claire du résultat attendu].

*Exemple immobilier :* « Automatiser la réponse aux demandes d'estimation et de visite reçues
via le formulaire du site et les portails d'annonces, avec création automatique dans le CRM,
affectation au bon agent commercial et relance en cas d'absence de réponse sous 48h. »

---

## 2. Périmètre inclus

- [ ] Connexion de [formulaire / email / portail] à [outil d'automatisation]
- [ ] Création / mise à jour de [contact / deal / tâche] dans le CRM
- [ ] Envoi de [email / notification] de réponse automatique
- [ ] Règles de qualification : [critères]
- [ ] Règles d'affectation : [logique]
- [ ] Relances automatiques si absence de réponse sous [X] heures/jours
- [ ] Proposition de créneau de rendez-vous
- [ ] Documentation de prise en main
- [ ] Phase de recette et hypercare de [X] jours

---

## 3. Périmètre exclu

- Refonte complète du CRM
- Développement applicatif sur mesure (code métier)
- Migration historique de données au-delà de [X] enregistrements
- Rédaction complète de base de connaissances
- Gestion juridique RGPD du client au-delà des éléments fournis au contrat
- [Autre exclusion spécifique]

---

## 4. Dépendances client

Le client s'engage à fournir dans un délai de [X] jours ouvrés après signature :

- Accès administrateur aux outils listés
- Validation des messages, règles métier et contenus
- Désignation d'un interlocuteur décisionnaire unique
- Liste des agents / utilisateurs / règles d'affectation

---

## 5. Recette

Le projet est considéré comme livré lorsque les scénarios de test suivants
(à compléter et valider avant le build) fonctionnent sur les cas réels :

Scénarios types :
1. Un lead soumet le formulaire → réponse automatique sous 3 min → fiche CRM créée
2. Un lead ne répond pas sous 48h → relance automatique
3. Un lead prend rendez-vous → notification à l'agent assigné

---

## 6. Révisions incluses

Le forfait inclut :
- 1 aller-retour mineur sur les règles de qualification
- 1 aller-retour mineur sur les messages et templates

Toute demande supplémentaire constitue une évolution hors périmètre,
facturée au temps passé (demi-journée ou journée).

---

## 7. Maintenance

**Option retenue :** [Oui / Non]

La présente section et l'Annexe 2 ne s'appliquent que si l'option est retenue dans le devis.

La maintenance couvre :
- Surveillance des workflows
- Corrections en cas de dysfonctionnement
- Ajustements mineurs (changement de champ, de destinataire)
- Support par email

La maintenance ne couvre pas :
- Nouvelles fonctionnalités
- Nouveaux flux
- Nouvelles intégrations non prévues au périmètre initial

---

## 8. Hypothèses et limites

- Les performances dépendent des outils tiers (CRM, emailing, API).
- Toute modification unilatérale des champs, accès, intégrations ou API côté client
  peut impacter le fonctionnement des automatisations.
- Les délais de livraison supposent que le client fournit les accès et validations
  dans les temps convenus.

---

## 9. Budget et délai estimatif

| Poste | Montant |
|-------|--------:|
| Build | [X] € |
| Maintenance mensuelle | [X] € / mois si option retenue |
| **Total première année** | **[X] €** |

Délai de livraison estimé : [X] jours ouvrés.

---

*Document à compléter et signer avant le démarrage du build.*
