# Script de démo — Pack Réponse Lead (immobilier)

> **Durée cible :** 5 min 30 à 7 min
> **Format :** Loom ou enregistrement écran + voix off
> **Public :** Dirigeant d'agence immobilière, non technique

---

## Structure

| # | Section | Durée | Écran |
|---|---------|-------|-------|
| 1 | Hook | 0:00–0:30 | Slide titre |
| 2 | Le problème | 0:30–1:00 | Site web agence + boîte mail |
| 3 | Déclencheur | 1:00–1:30 | Formulaire → Webhook Make |
| 4 | Workflow pas à pas | 1:30–4:30 | Interface Make, 8 étapes |
| 5 | Résultat côté agent | 4:30–5:15 | Pipedrive + notification |
| 6 | Monitoring | 5:15–5:45 | Dashboard Make |
| 7 | CTA | 5:45–6:15 | Slide contact |

---

## Script complet

### 1. Hook (0:00–0:30)

> 🎬 **Écran :** Slide « Donopot — Automatisation IA pour agences immobilières »

```
Quand un prospect remplit un formulaire d'estimation sur votre site,
combien de temps faut-il pour qu'il reçoive une réponse ?

Dans la plupart des agences : plusieurs heures, parfois le lendemain.

Voici comment on fait pour que la réponse parte en moins de 3 minutes,
que le lead soit automatiquement dans votre CRM, et que le bon agent
reçoive une notification. Le tout sans recruter personne.

Je vous montre.
```

### 2. Le problème (0:30–1:00)

> 🎬 **Écran :** Site web d'une agence immobilière fictive « Agence Duport » — formulaire « Demander une estimation »

```
Voici le site d'une agence classique.
Un formulaire d'estimation. Classique.

Aujourd'hui, que se passe-t-il ?
Le formulaire arrive dans une boîte mail générique.
Quelqu'un doit le lire, comprendre la demande, chercher le bon agent,
créer une fiche dans le CRM, répondre au prospect.

Résultat : 30 minutes de travail manuel par lead.
Et souvent plusieurs heures de délai.
```

### 3. Déclencheur (1:00–1:30)

> 🎬 **Écran :** Passage de la page web à l'interface Make

```
Voici ce qu'on va mettre en place.
Dès que le formulaire est soumis, un webhook envoie les données
dans Make — notre plateforme d'automatisation.

Regardez.
```

> 🎬 **Action :** Simuler une soumission de formulaire (nom : « Sophie Martin », email : s.martin@email.com, type : estimation appartement)

```
Je soumets le formulaire... et le scénario se déclenche instantanément.
```

### 4. Workflow pas à pas (1:30–4:30)

> 🎬 **Écran :** Interface Make, vue du scénario complet (tous les modules)

```
Voici le scénario complet. Je vais vous montrer chaque étape.
```

> 🎬 **Étape 1 — Réception (1:30–1:50)**

```
Étape 1 : le webhook reçoit les données du formulaire.
Nom, email, téléphone, type de demande, message.
Tout est parsé et structuré automatiquement.
```

> 🎬 **Étape 2 — Détection doublon (1:50–2:10)**

```
Étape 2 : Make interroge votre CRM Pipedrive.
« Est-ce que Sophie Martin existe déjà ? »
Si oui → on met à jour sa fiche.
Si non → on la crée.
```

> 🎬 **Étape 3 — Classification (2:10–2:30)**

```
Étape 3 : le lead est classifié automatiquement.
Type : estimation, visite, ou vente.
Priorité : selon le type de bien et l'urgence.
Agent : attribué selon le secteur géographique.
```

> 🎬 **Étape 4 — Création dans le CRM (2:30–3:00)**

```
Étape 4 : la fiche est créée dans Pipedrive.
Contact → Sophie Martin.
Deal → « Estimation appartement — Sophie Martin ».
Étape → Nouveau lead.
Agent assigné → Thomas (secteur Paris 15).
Tout ça automatiquement, sans saisie.
```

> 🎬 **Étape 5 — Réponse email (3:00–3:30)**

```
Étape 5 : un email personnalisé part immédiatement.

« Bonjour Sophie,
Merci pour votre demande d'estimation de votre appartement.
Je suis Thomas, votre agent dédié pour le secteur Paris 15.
Je vous propose un créneau cette semaine... »
Avec un lien Calendly pour prendre rendez-vous directement.
```

> 🎬 **Étape 6 — Notification agent (3:30–3:50)**

```
Étape 6 : Thomas reçoit une notification.
Par email, ou sur son téléphone.
« Nouveau lead : Sophie Martin — Estimation — Paris 15.
Fiche CRM créée. Premier contact envoyé. »
```

> 🎬 **Étape 7 — Relance automatique (3:50–4:30)**

```
Étape 7 : si Sophie ne répond pas sous 48 heures,
une relance automatique part.
Pas besoin que Thomas y pense.
Pas besoin d'un assistant.
Le système gère le suivi.
```

### 5. Résultat côté agent (4:30–5:15)

> 🎬 **Écran :** Pipedrive, vue pipeline

```
Côté agent, voici ce que Thomas voit dans Pipedrive.
Un nouveau deal « Sophie Martin » dans la colonne « Nouveau lead ».
Toutes les infos sont là.
Il n'a rien eu à saisir.
Il peut se concentrer sur ce qui compte : la relation client.
```

### 6. Monitoring (5:15–5:45)

> 🎬 **Écran :** Dashboard Make — historique des exécutions

```
Et moi, en tant que prestataire, je supervise tout ça.
Chaque exécution est loguée.
Si quelque chose échoue, je suis alerté immédiatement.
Une fois par mois, je vous envoie un rapport :
- Nombre de leads traités
- Délai moyen de réponse
- Taux de transformation
```

### 7. CTA (5:45–6:15)

> 🎬 **Écran :** Slide contact — photo, nom, email, Calendly

```
Voilà. Ce que vous venez de voir, c'est le Pack Réponse Lead.
Livré en 7 à 12 jours. Avec maintenance incluse.

Si vous voulez la même chose pour votre agence,
on se parle 20 minutes.
Je fais un audit de vos flux, et je vous dis exactement
ce qui est automatisable et combien ça coûte.

Le lien est dans la description.
```

---

## Notes de tournage

- **Silencieux** pendant l'enregistrement (pas de notifications)
- **Zoomer** sur les parties importantes de l'interface Make
- **Curseur visible** et lent pour suivre les explications
- **Pas de jargon** technique. Remplacer « webhook » par « connexion automatique », « module » par « étape »
- **Ton :** calme, pédagogue, pas de pression commerciale
- **Ajouter** une musique de fond légère (optionnel, couper pendant les moments clés)
- **Sous-titres :** recommandés pour LinkedIn et l'accessibilité

---

## Checklist avant publication

- [ ] Son clair, pas de bruit de fond
- [ ] Toutes les données affichées sont fictives (pas de vrais clients)
- [ ] Les URLs/emails visibles sont génériques
- [ ] Le lien Calendly fonctionne
- [ ] La description contient le CTA et le lien
- [ ] Miniature personnalisée (pas un freeze frame aléatoire)
