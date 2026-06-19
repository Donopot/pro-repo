# Processus de livraison — Livrer sans stress en 7 à 30 jours

> Ce document décrit le processus standard de livraison d'une mission d'automatisation, de la signature à l'hypercare.

---

## Vue d'ensemble

```
Signature → Cadrage → Prototype → Tests → Mise en prod → Hypercare → Maintenance
  J-7         J1-3       J4-10      J11-15     J16-20       J21-30       J30+
```

---

## Phase 1 — Cadrage (J1 à J3)

**Objectif :** Aligner les attentes et geler le périmètre.

### Réunion de cadrage (60-90 minutes)
- [ ] Présentation des participants et de leurs rôles
- [ ] Rappel du contexte et des objectifs
- [ ] Revue détaillée du flux actuel (étape par étape)
- [ ] Identification des cas particuliers et exceptions
- [ ] Définition des règles métier
- [ ] Définition des cas d'erreur et du comportement attendu
- [ ] Définition du niveau d'automatisation vs validation humaine
- [ ] Confirmation du périmètre (inclus / hors périmètre)

### Checklist cadrage
- [ ] Outils utilisés (CRM, email, formulaires, API disponibles)
- [ ] Données disponibles (champs, formats, volumes)
- [ ] Règles métier documentées
- [ ] Cas d'erreur listés
- [ ] Personnes impliquées identifiées (qui valide quoi)
- [ ] Niveau d'automatisation défini (full auto / semi-auto / assisté)
- [ ] Critères de succès mesurables (ex : temps de réponse < 2 min)
- [ ] Planning validé

### Livrable cadrage
Document de spécifications fonctionnelles (1-2 pages) :
- Flux actuel vs flux cible
- Règles métier
- Cas d'erreur
- Outils et accès nécessaires
- Planning détaillé

> **Envoyer le livrable de cadrage au client pour validation écrite avant de commencer le prototype.**
> Un email de confirmation suffit.

---

## Phase 2 — Prototype (J4 à J10)

**Objectif :** Construire une première version fonctionnelle mais limitée.

### Principes
- Commencer par le flux nominal (le cas le plus simple)
- Ne pas chercher à couvrir tous les cas particuliers
- Utiliser des données de test (pas de vraies données client)
- Livrer rapidement (3-5 jours max) pour avoir un feedback

### Étapes
1. **Mettre en place les outils** : créer les comptes, installer les connecteurs
2. **Construire le flux nominal** : le chemin principal, de A à Z
3. **Tester avec des données fictives** : 5-10 scénarios simples
4. **Préparer une démo** : 15 minutes, juste le flux nominal

### Démo prototype (30 minutes)
- [ ] Montrer le flux nominal (pas les cas d'erreur)
- [ ] Expliquer ce qui est temporaire / sera amélioré
- [ ] Recueillir les premières réactions
- [ ] Noter les ajustements demandés
- [ ] Valider la direction avant d'aller plus loin

### Checklist prototype
- [ ] Flux nominal fonctionnel
- [ ] Tests basiques OK (5-10 scénarios)
- [ ] Démo faite avec le client
- [ ] Retours notés
- [ ] Ajustements planifiés

---

## Phase 3 — Tests (J11 à J15)

**Objectif :** Couvrir TOUS les scénarios avant la mise en production.

### Scénarios à tester

| Catégorie | Scénario | Résultat attendu |
|-----------|----------|-----------------|
| Nominal | Nouveau lead complet (tous les champs remplis) | Traitement normal |
| Nominal | Nouveau lead partiel (champs manquants) | Traitement normal |
| Doublon | Même email, nouvelle demande | Fusion ou alerte |
| Erreur | Email invalide | Rejet avec notification |
| Erreur | Fichier joint corrompu | Alerte humaine |
| Erreur | API CRM indisponible | File d'attente + retry |
| Absence | Pas de réponse du prospect | Relance automatique |
| Volume | 50 leads en 5 minutes | Pas de perte, pas de doublon |
| Humain | Escalade manuelle déclenchée | Bonne personne alertée |

### Checklist tests
- [ ] Tous les scénarios nominaux OK
- [ ] Tous les cas d'erreur gérés
- [ ] Doublons détectés
- [ ] Relances programmées
- [ ] Alertes humaines configurées
- [ ] Test de charge (volume) OK
- [ ] Logs et traçabilité en place
- [ ] Client a validé les tests

---

## Phase 4 — Mise en production (J16 à J20)

**Objectif :** Déployer progressivement, sans tout casser.

### Déploiement progressif

1. **Shadow mode (J16-17)** : l'automatisation tourne en parallèle du process manuel, sans impacter le client. On compare les résultats.

2. **Déploiement partiel (J18-19)** : activation sur 20% des leads. Surveillance renforcée. Un humain vérifie chaque décision automatique.

3. **Déploiement complet (J20)** : activation sur 100% des leads. L'humain ne vérifie que les cas escaladés.

### Checklist mise en production
- [ ] Shadow mode exécuté sans anomalie
- [ ] Déploiement partiel validé
- [ ] Équipe formée (30-60 minutes)
- [ ] Documentation livrée
- [ ] Contact d'urgence communiqué
- [ ] Procédure de rollback prête
- [ ] Activation complète

---

## Phase 5 — Hypercare (J21 à J30)

**Objectif :** Surveiller, ajuster, rassurer.

### Monitoring quotidien (J21-J24)
- [ ] Vérifier les logs chaque matin
- [ ] Vérifier qu'aucun lead n'est perdu
- [ ] Vérifier les temps de réponse
- [ ] Corriger les bugs immédiatement

### Ajustements (J25-J28)
- [ ] Appliquer les retours du client
- [ ] Optimiser les règles si nécessaire
- [ ] Ajouter les cas particuliers oubliés

### Bilan hypercare (J30)
- [ ] Réunion de 30 minutes avec le client
- [ ] Présenter les chiffres (leads traités, temps de réponse, conversions)
- [ ] Recueillir les feedbacks
- [ ] Proposer des évolutions
- [ ] Discuter du contrat de maintenance

---

## Documentation à livrer

Un document unique (3-5 pages) remis au client à la mise en production :

```markdown
# Documentation — [Nom du projet]

## 1. Résumé
Ce que fait l'automatisation, en une phrase.

## 2. Fonctionnement
Description simple du flux, étape par étape.

## 3. Outils utilisés
Liste des outils, comptes, accès.

## 4. Règles de gestion
Les règles métier appliquées par l'automatisation.

## 5. Cas d'erreur
Ce qui se passe en cas d'erreur, qui est alerté.

## 6. Modifications possibles
Ce que le client peut modifier lui-même, ce qui nécessite ton intervention.

## 7. Désactivation
Comment désactiver l'automatisation en cas de problème.

## 8. Contact
Ton email, téléphone, délai de réponse.
```

---

## Outils de suivi recommandés

| Besoin | Outil |
|--------|-------|
| Gestion de projet | Notion, Linear, ou un simple fichier Markdown |
| Logs et erreurs | Canal Slack/Teams dédié, ou email automatique |
| Temps passé | Toggl, Clockify |
| Facturation | Freebe, InvoiceNinja, ou facture PDF manuelle |
| Signature électronique | Yousign, Docusign |

---

## Pièges à éviter

- ❌ **Commencer sans validation écrite du cadrage.** Le client aura « oublié » ce qui était inclus.
- ❌ **Vouloir tout automatiser d'un coup.** Livrer un flux simple qui marche > un flux complexe qui plante.
- ❌ **Négliger les cas d'erreur.** 80% du temps de dev est passé sur les 20% de cas qui plantent.
- ❌ **Ne pas former l'équipe.** Si personne ne sait comment ça marche, ça ne marche pas.
- ❌ **Disparaître après la livraison.** L'hypercare, c'est ce qui transforme un client satisfait en ambassadeur.
