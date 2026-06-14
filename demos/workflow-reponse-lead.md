# Workflow — Réponse Lead Immobilier

> **Plateforme :** Make (compatible n8n avec adaptation)
> **Pack :** Réponse Lead
> **Temps d'exécution :** < 3 minutes (hors délais de relance)
> **Déclencheur :** Webhook entrant

---

## Vue d'ensemble

```
[Formulaire site web]
        │
        ▼
  ╔══════════════════════════════════════════╗
  ║           MODULE 1 — Webhook            ║
  ║       Réception + parsing JSON          ║
  ╚══════════════════════════════════════════╝
        │
        ▼
  ╔══════════════════════════════════════════╗
  ║ MODULE 2 — Variables de qualification   ║
  ║ Catégorie, template et assignation      ║
  ╚══════════════════════════════════════════╝
        │
         │
         ▼
  ╔══════════════════════════════════════════╗
  ║   MODULE 3 — Pipedrive « Search person »║
  ║     Détection doublon par email         ║
  ╚══════════════════════════════════════════╝
         │
    ┌────┴────┐
    ▼         ▼
[Existe ?] [Nouveau]
    │         │
    │    ╔═══════════════════════════════╗
    │    ║ MODULE 4 — Pipedrive         ║
    │    ║ « Create person »            ║
    │    ╚═══════════════════════════════╝
    │         │
    └────┬────┘
         ▼
  ╔══════════════════════════════════════════╗
  ║ MODULE 5 — Pipedrive « Create deal »    ║
  ║    Deal avec étape, valeur, agent        ║
  ╚══════════════════════════════════════════╝
         │
         ▼
  ╔══════════════════════════════════════════╗
  ║  MODULE 6 — Text Parser (Make)          ║
  ║   Composition email personnalisé        ║
  ╚══════════════════════════════════════════╝
         │
         ▼
  ╔══════════════════════════════════════════╗
  ║  MODULE 7 — Brevo « Send email »        ║
  ║    Envoi réponse + Calendly             ║
  ╚══════════════════════════════════════════╝
         │
         ▼
  ╔══════════════════════════════════════════╗
  ║  MODULE 8 — Pipedrive « Create note »   ║
  ║    Note interne : email envoyé           ║
  ╚══════════════════════════════════════════╝
         │
         ▼
  ╔══════════════════════════════════════════╗
  ║ MODULE 9 — Pipedrive « Update deal »    ║
  ║    relance_due_at = maintenant + 48 h   ║
  ╚══════════════════════════════════════════╝

[Scénario séparé, planifié toutes les 15 minutes]
         │
         ▼
  Chercher les deals « Nouveau lead »
  dont relance_due_at est dépassée
         │
    ┌────┴────┐
    ▼         ▼
[À relancer] [Déjà avancé]
    │         │
    ▼        STOP
  Envoyer la relance puis renseigner
  relance_sent_at et ajouter une note
```

---

## Modules détaillés

### Module 1 — Webhook

| Propriété | Valeur |
|-----------|--------|
| **Type** | Webhook → Custom webhook |
| **Méthode** | POST |
| **Format** | JSON |
| **Exemple payload** | Voir ci-dessous |

```json
{
  "name": "Sophie Martin",
  "email": "s.martin@email.com",
  "phone": "06 12 34 56 78",
  "type": "estimation",
  "property_type": "appartement",
  "city": "Paris",
  "postal_code": "75015",
  "surface": 65,
  "message": "Je souhaite estimer mon appartement en vue d'une vente.",
  "source": "site-web",
  "submitted_at": "2026-06-15T10:23:00Z"
}
```

### Module 2 — Préparer qualification et template

Utiliser un module de définition de variables et la fonction `switch()` afin de
conserver une chaîne unique après la qualification.

| Variable | Règle |
|----------|-------|
| `lead_category` | Estimation, Visite, Vente ou Autre selon `type` |
| `email_template` | Template correspondant au type, avec fallback générique |
| `agent_*` | Valeurs issues de la table d'assignation par code postal |

> 💡 Si un vrai routeur est nécessaire pour des traitements différents, les
> modules suivants doivent être dupliqués dans chaque route : les routes Make
> ne convergent pas ensuite vers une chaîne commune.

### Module 3 — Pipedrive Search person

| Propriété | Valeur |
|-----------|--------|
| **Type** | Pipedrive → Search persons |
| **Champ** | Email |
| **Terme** | `{{1.email}}` |
| **Exact match** | Oui |

Résultat : `person_id` si trouvé, vide sinon.

> ⚠️ Configurer le module pour poursuivre la route lorsqu'aucun résultat n'est
> trouvé. Sinon, zéro bundle est émis et la création du contact ne s'exécute pas.
> Une alternative robuste consiste à utiliser deux routes filtrées :
> « personne trouvée » et « personne absente ».

### Module 4 — Pipedrive Create person (conditionnel)

| Propriété | Valeur |
|-----------|--------|
| **Condition** | `{{3.person_id}}` est vide |
| **Type** | Pipedrive → Create a person |
| **Name** | `{{1.name}}` |
| **Email** | `{{1.email}}` (primary) |
| **Phone** | `{{1.phone}}` (primary) |
| **Custom fields** | `source_lead` = `{{1.source}}`, `type_bien` = `{{1.property_type}}` |

### Module 5 — Pipedrive Create deal

| Propriété | Valeur |
|-----------|--------|
| **Type** | Pipedrive → Create a deal |
| **Title** | `{{1.type}} — {{1.property_type}} — {{1.name}}` |
| **Person** | `{{3.person_id}}` ou `{{4.person_id}}` |
| **Pipeline** | Transactions immobilières |
| **Stage** | Nouveau lead |
| **Value** | `0` (à compléter après estimation) |
| **Owner** | Assigné selon secteur (`{{1.postal_code}}` → table de correspondance) |
| **Custom fields** | `surface` = `{{1.surface}}`, `ville` = `{{1.city}}`, `code_postal` = `{{1.postal_code}}`, `urgence` = calculée, `relance_due_at` = `addHours(now; 48)`, `relance_sent_at` = vide |

**Table d'assignation (exemple Paris) :**

| Code postal | Agent | Email agent |
|-------------|-------|-------------|
| 75001–75009 | Sophie | s.agent@agence.fr |
| 75010–75015 | Thomas | t.agent@agence.fr |
| 75016–75020 | Marie | m.agent@agence.fr |

### Module 6 — Text Parser (template email)

> ⚠️ La syntaxe `{{if}}/{{elseif}}/{{endif}}` ci-dessous est du **pseudo-code**.
> Dans Make, utiliser le module « Router » avant le Text Parser ou la fonction
> `if()` dans le template. La logique conditionnelle dépend du moteur de template
> utilisé côté Make.

```text
Objet : {{if 1.type == "estimation"}}Votre demande d'estimation — {{1.property_type}} {{1.city}}{{elseif 1.type == "visite"}}Votre demande de visite — {{1.property_type}} {{1.city}}{{else}}Votre projet immobilier — {{1.city}}{{endif}}

Bonjour {{1.name}},

Merci pour votre {{if 1.type == "estimation"}}demande d'estimation{{elseif 1.type == "visite"}}demande de visite{{else}}message{{endif}} concernant votre {{1.property_type}} à {{1.city}}.

Je suis {{agent_name}}, votre agent dédié pour le secteur {{1.city}}.
Je vous propose un créneau cette semaine pour en discuter :

👉 [Prendre rendez-vous](https://calendly.com/agence/{{agent_slug}})

Vous pouvez aussi me joindre directement au {{agent_phone}}.

À très bientôt,
{{agent_name}}
Agence Duport
```

### Module 7 — Brevo Send email

| Propriété | Valeur |
|-----------|--------|
| **Type** | Brevo → Send transactional email |
| **To** | `{{1.email}}` |
| **Subject** | `{{6.subject}}` |
| **HTML** | `{{6.html}}` |
| **Sender** | `{{agent_email}}` |

### Module 8 — Pipedrive Create note

| Propriété | Valeur |
|-----------|--------|
| **Type** | Pipedrive → Add a note |
| **Deal** | `{{5.deal_id}}` |
| **Content** | `📨 Email de réponse envoyé le {{formatDate now "DD/MM/YYYY à HH:mm"}} — template estimation` |

### Module 9 — Programmer la relance

Mettre à jour le deal créé avec :

| Champ | Valeur |
|-------|--------|
| `relance_due_at` | `addHours(now; 48)` |
| `relance_sent_at` | Vide |

### Scénario séparé — Envoyer les relances

Créer un second scénario Make, planifié toutes les 15 minutes :

1. Rechercher les deals à l'étape « Nouveau lead ».
2. Garder uniquement ceux dont `relance_due_at <= now` et
   `relance_sent_at` est vide.
3. Envoyer la relance Brevo.
4. Renseigner `relance_sent_at` et ajouter une note dans le deal.

Cette architecture évite de conserver une exécution ouverte pendant 48 heures
et rend les relances observables et relançables en cas d'erreur.

```text
Objet : Suite à votre demande d'estimation

Bonjour {{1.name}},

Je fais suite à mon message concernant l'estimation
de votre {{1.property_type}} à {{1.city}}.

Avez-vous eu le temps d'y réfléchir ? Je reste disponible pour en discuter
quand vous le souhaitez.

👉 [Prendre rendez-vous](https://calendly.com/agence/{{agent_slug}})

Bien à vous,
{{agent_name}}
```

---

## Variables globales

| Variable | Source | Exemple |
|----------|--------|---------|
| `agent_name` | Table d'assignation (code postal) | Thomas |
| `agent_email` | Table d'assignation | t.agent@agence.fr |
| `agent_phone` | Table d'assignation | 01 23 45 67 89 |
| `agent_slug` | Table d'assignation | thomas |

---

## Gestion des erreurs

| Erreur | Action |
|--------|--------|
| Webhook reçoit un payload invalide | Répondre 400 + log |
| Pipedrive API down | Réessayer 3 fois (intervalle 5 min), puis alerter |
| Brevo échec d'envoi | Noter dans le deal + alerter |
| Deal déjà existant (doublon réel) | Mettre à jour au lieu de créer (module alternatif) |

---

## Adaptation n8n

| Make | n8n |
|------|-----|
| Webhook | Webhook node |
| Variables avec `switch()` | Edit Fields / Code node |
| Pipedrive modules | Pipedrive nodes |
| Text parser | Function node (JavaScript) |
| Scénario de relance planifié | Schedule Trigger + recherche Pipedrive |
| Brevo | HTTP Request node (Brevo API) |

> Le blueprint JSON Make est disponible dans `demos/workflow-reponse-lead.json`.
> Pour n8n, recréer le workflow avec les nœuds équivalents. Les imports n8n
> attendent un export JSON n8n ; le blueprint conceptuel Make n'est pas importable.
