# Checklist onboarding client

> **Objectif :** Garantir une mise en route fluide et professionnelle à chaque nouveau client.
> **Quand déclencher :** Dès réception de l'acompte (30 %) et signature du contrat.
> **Acteurs :** Donopot (D), Client (C).

---

## Phase 0 — Signature & acompte

| # | Action | Qui | Livrable | Délai | ✅ |
|---|--------|:---:|----------|-------|:---:|
| 0.1 | Envoyer devis + contrat + annexes (scope, SLA, RGPD) | D | Email avec PDFs | J-7 avant signature | ☐ |
| 0.2 | Répondre aux questions juridiques/commerciales | D | Email ou appel | Sous 48h | ☐ |
| 0.3 | Recevoir contrat signé + bon pour accord devis | C | PDF signé | Avant démarrage | ☐ |
| 0.4 | Recevoir acompte 30 % | C | Virement | Avant démarrage | ☐ |
| 0.5 | Envoyer facture d'acompte | D | Facture PDF | Sous 48h | ☐ |
| 0.6 | Envoyer email de bienvenue (template `onboarding-email.md`) | D | Email | J0 | ☐ |

---

## Phase 1 — Collecte des accès

| # | Action | Qui | Détail | Délai | ✅ |
|---|--------|:---:|--------|-------|:---:|
| 1.1 | Créer un document partagé « Accès & ressources » | D | Lister les accès requis, leurs propriétaires et leur durée, sans aucun mot de passe ni secret | J+1 | ☐ |
| 1.2 | Inviter un compte nominatif CRM au moindre privilège | C | Pipedrive ou HubSpot, MFA activée, accès limité au projet | J+3 | ☐ |
| 1.3 | Créer une clé API dédiée à portée minimale | C | Transmission par coffre chiffré ou lien à usage unique, jamais par email/document | J+3 | ☐ |
| 1.4 | Inviter un compte nominatif pour le site/formulaire | C | Rôle limité ; éviter les comptes partagés et FTP quand une invitation est possible | J+3 | ☐ |
| 1.5 | Fournir liste des agents commerciaux (nom, email, secteur) | C | CSV ou tableau | J+5 | ☐ |
| 1.6 | Fournir templates email existants (signature, charte) | C | Fichiers ou captures | J+5 | ☐ |
| 1.7 | Fournir règles métier (affectation, qualification, seuils) | C | Document écrit ou appel | J+5 | ☐ |
| 1.8 | Vérifier tous les accès fonctionnels | D | Test de connexion | J+5 | ☐ |
| 1.9 | Documenter propriétaire, portée, expiration et révocation | D+C | Registre des accès sans secrets | J+5 | ☐ |

---

## Phase 2 — Kickoff

| # | Action | Qui | Livrable | Délai | ✅ |
|---|--------|:---:|----------|-------|:---:|
| 2.1 | Envoyer invitation réunion de lancement | D | Invitation calendrier | J+2 | ☐ |
| 2.2 | Réunion de lancement (45 min) | D+C | Ordre du jour ci-dessous | J+5 | ☐ |
| 2.3 | Envoyer compte-rendu de réunion | D | Email récapitulatif | J+5 | ☐ |

### Ordre du jour — Réunion de lancement

1. **Présentations** (5 min) — Équipe, interlocuteur unique
2. **Rappel du périmètre** (5 min) — Ce qui est inclus / exclu
3. **Revue des règles métier** (15 min) — Qualification, affectation, messages
4. **Validation des accès** (5 min) — Confirmer que tout fonctionne
5. **Calendrier** (5 min) — Dates clés (build, recette, go-live)
6. **Points de contact** (5 min) — Canal Slack/email, fréquence des points
7. **Questions** (5 min)

---

## Phase 3 — Audit (1h)

| # | Action | Qui | Livrable | ✅ |
|---|--------|:---:|----------|:---:|
| 3.1 | Cartographier les flux existants | D | Schéma ou notes | ☐ |
| 3.2 | Lister les outils en place | D | Tableau des outils | ☐ |
| 3.3 | Mesurer les volumes (leads/jour, requêtes/semaine) | C | Chiffres | ☐ |
| 3.4 | Identifier les irritants et les doublons | D+C | Liste de problèmes | ☐ |
| 3.5 | Valider le périmètre définitif | D+C | Scope.md signé | ☐ |

---

## Phase 4 — Build

| # | Action | Qui | Délai | ✅ |
|---|--------|:---:|-------|:---:|
| 4.1 | Créer l'environnement Make (scénarios, connexions) | D | J+7 à J+30 | ☐ |
| 4.2 | Configurer le CRM (pipeline, champs, vues) | D | J+7 à J+30 | ☐ |
| 4.3 | Créer les templates email (Brevo) | D | J+7 à J+30 | ☐ |
| 4.4 | Rédiger la documentation de prise en main | D | J+7 à J+30 | ☐ |
| 4.5 | Tests internes (scénarios de recette) | D | Avant recette client | ☐ |
| 4.6 | Point d'avancement intermédiaire | D+C | Mi-build | ☐ |

---

## Phase 5 — Recette & go-live

| # | Action | Qui | Livrable | ✅ |
|---|--------|:---:|----------|:---:|
| 5.1 | Session de recette avec le client (1h) | D+C | Scénarios validés | ☐ |
| 5.2 | Corrections post-recette | D | Sous 48h | ☐ |
| 5.3 | Validation finale | C | Email « Bon pour go-live » | ☐ |
| 5.4 | Envoyer facture de solde (70 %) | D | Facture à la recette, conformément au devis | ☐ |
| 5.5 | Activation en production | D | Workflows live | ☐ |
| 5.6 | Session de prise en main (1h) | D+C | Équipe formée | ☐ |

---

## Phase 6 — Hypercare (7 jours)

| # | Action | Qui | Délai | ✅ |
|---|--------|:---:|-------|:---:|
| 6.1 | Surveillance quotidienne des workflows | D | 7 jours | ☐ |
| 6.2 | Corrections mineures (incluses) | D | Sous 24h | ☐ |
| 6.3 | Point de fin d'hypercare | D+C | J+7 post go-live | ☐ |
| 6.4 | Vérifier le règlement de la facture de solde envoyée à la recette (70 %) | D | À la recette, conformément au devis | ☐ |
| 6.5 | Activer la maintenance (si option retenue) | D | J+7 post go-live | ☐ |

---

## Phase 7 — Suivi

| # | Action | Qui | Fréquence | ✅ |
|---|--------|:---:|-----------|:---:|
| 7.1 | Rapport mensuel d'activité (si maintenance) | D | Mensuel | ☐ |
| 7.2 | Point trimestriel (si maintenance) | D+C | Trimestriel | ☐ |
| 7.3 | Demande de témoignage client | D | Après 3 mois | ☐ |
| 7.4 | Demande de référencement / recommandation | D | Après 3 mois | ☐ |

---

## Résumé des durées

| Phase | Durée | Cumul |
|-------|-------|-------|
| Signature & acompte | 7 jours | J-7 → J0 |
| Collecte des accès | 5 jours | J0 → J+5 |
| Kickoff + Audit | 5 jours | J+5 → J+10 |
| Build | 7 à 30 jours | J+10 → J+40 |
| Recette & go-live | 3 jours | J+40 → J+43 |
| Hypercare | 7 jours | J+43 → J+50 |

---

*Checklist à dupliquer pour chaque nouveau client. Adapter les délais selon le pack retenu.*

## Règles de sécurité des accès

- Utiliser des comptes nominatifs, le moindre privilège et la MFA partout où elle est disponible.
- Ne jamais transmettre un mot de passe, une clé API ou un token dans un email, un document partagé ou un ticket.
- Transmettre les secrets via un coffre chiffré ou un lien à usage unique, puis supprimer le lien après réception.
- Faire expirer, révoquer ou réduire les accès dès la fin du build et au plus tard à la clôture de l'hypercare.
