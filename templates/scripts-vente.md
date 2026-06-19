# Scripts de vente complets — Agences immobilières

> **Règle d'or :** Le premier contact n'est jamais une vente. C'est une ouverture de conversation. La vente se fait pendant la démo.

---

## 1. 📞 Appel téléphonique — Premier contact

**Objectif :** Obtenir un rendez-vous de 15 minutes. Pas vendre.
**Timing :** Mardi-Jeudi, 9h30-11h30 ou 14h30-16h30.
**Durée cible :** 2-3 minutes max.

```
VOUS : Bonjour, [Prénom Nom] de l'agence [Nom agence] ?

EUX : Oui, c'est moi.

VOUS : Donopot, je suis consultant en automatisation pour les agences immobilières.
      Je ne vais pas vous faire perdre votre temps — j'ai deux questions très rapides.

EUX : (souvent) Allez-y / Oui ?

VOUS : Parmi vos tâches quotidiennes, qu'est-ce qui vous prend le plus de temps :
      le tri des leads entrants, les relances, ou la mise à jour du CRM ?

EUX : [Réponse — écouter attentivement, ne pas couper]

VOUS : Intéressant. J'accompagne justement des agences comme la vôtre sur ce point
      précis. En 7 à 30 jours, je mets en place un assistant IA qui fait ça tout seul.
      Concrètement, [bénéfice lié à leur réponse].

      Est-ce que vous auriez 15 minutes cette semaine pour que je vous montre
      un exemple concret ?

EUX : 
  → OUI : Parfait. Mardi 10h ou jeudi 14h, qu'est-ce qui vous arrange ?
  → PAS LE TEMPS : Je comprends. Je vous envoie un mail avec un exemple,
    vous le lisez quand vous avez 2 minutes ?
  → PAS INTÉRESSÉ : Merci pour votre honnêteté. Si un jour le sujet devient
    prioritaire, vous savez où me trouver. Bonne journée.
```

### Variantes d'accroche selon profil

**Agence indépendante :**
> « J'ai vu que vous êtes une agence de proximité sur [ville]. C'est une force — mais ça veut aussi dire que vous gérez tout, des visites aux relances. Je travaille avec des indépendants pour leur libérer du temps sur ces tâches. »

**Réseau (Orpi, Century 21, etc.) :**
> « Vous êtes [réseau] sur [ville] — vous avez déjà la puissance d'un grand groupe. J'aide les agences de réseau à aller plus loin sur la rapidité de traitement des leads. »

**Agence prestige (Daniel Féau, etc.) :**
> « Sur le marché haut de gamme de [ville], la rapidité de réponse fait la différence. Un lead luxe qui attend 4h est déjà parti chez un confrère. J'automatise ce premier contact pour qu'il soit immédiat et personnalisé. »

---

## 2. 📧 Email de prospection — Template à personnaliser

Cf. les 166 mails dans `crm/pj-sud-paris.csv` (colonne `mail_prospection`).

**Points clés de l'email :**
- Objet avec le nom de l'agence (taux d'ouverture ×2)
- Une phrase d'accroche personnalisée (ville, type d'agence)
- Question ouverte qui force la réflexion
- Call-to-action clair (« café virtuel de 15 minutes »)
- P.S. qui tease une ressource gratuite
- Lien de désinscription obligatoire (RGPD)

---

## 3. 📞 Relance téléphonique — J+5 après email

```
VOUS : Bonjour [Prénom], Donopot. Je vous avais envoyé un mail la semaine
      dernière sur l'automatisation du traitement des leads.

EUX : Ah oui, j'ai vu passer / je n'ai pas eu le temps / ...
      → Ne jamais dire « vous ne m'avez pas répondu » — c'est agressif.

VOUS : Pas de souci, je sais que vous êtes débordé — c'est justement pour ça
      que je vous contacte. Une question simple : aujourd'hui, quand un lead
      arrive sur votre site, il est traité en combien de temps ?

EUX : [Réponse]

VOUS : [Suivant réponse]
  → Si > 1h : « C'est le point que j'améliore pour mes clients. 15 minutes
    pour vous montrer comment faire ? »
  → Si « je ne sais pas » : « C'est un bon début de réflexion. Si vous voulez,
    je peux vous aider à le mesurer. »

RÈGLE : Maximum UNE relance téléphonique. Après, on lâche l'affaire.
       « Pas de problème, je vous laisse ma carte. Bonne continuation. »
```

---

## 4. 💬 Messages LinkedIn

### 4a. Invitation personnalisée (300 caractères)
```
Bonjour {{Prénom}}, je travaille avec des agences immobilières sur
l'automatisation du traitement des leads (réponse instantanée, CRM,
relances). J'ai vu votre actu récente sur [ville] — j'aimerais
échanger. Belle journée.
```

### 4b. Après acceptation (message vocal ou texte)
```
Merci pour la connexion {{Prénom}}.

Question rapide : quel est votre plus gros irritant quotidien —
le tri des leads, les relances, ou la paperasse administrative ?

(Je pose la question parce que j'aide des agences à automatiser
ces 3 là — en 7 à 30 jours. Si ça vous parle, je peux vous
montrer un exemple concret en 15 min.)
```

### 4c. Suite à un like/commentaire
```
J'ai vu votre post sur [sujet] — intéressant, surtout le point sur
[détail]. Je travaille justement avec des agences sur ce type de
problématique côté automatisation. Si le sujet vous botte, on
s'appelle 10 minutes ?
```

---

## 5. 🎯 Script du rendez-vous découverte (15 minutes)

**Objectif :** Qualifier le besoin → présenter la solution → proposer un devis.

### Minute 0-2 : Brise-glace
```
« Merci pour votre temps. Avant de commencer, dites-moi : qu'est-ce qui
vous a poussé à prendre ce rendez-vous ? »
→ Écouter. Noter les mots exacts qu'ils utilisent.
```

### Minute 2-5 : Diagnostic éclair
```
« Pour que je comprenne bien votre contexte : quand un lead arrive
aujourd'hui (estimation, visite, question), il se passe quoi ? »

Questions de relance :
- « Qui le traite ? »
- « En combien de temps en moyenne ? »
- « Combien de leads par semaine ? »
- « Qu'est-ce qui coince le plus ? »
```

### Minute 5-9 : La solution (adaptée à leur problème)
```
Ne PAS présenter les 3 packs d'un coup.
Présenter UNIQUEMENT le pack qui correspond à leur problème.

Exemple — si le problème c'est les leads :
« Voici ce que je propose : un assistant IA qui, 24h/24 —
  → répond aux demandes d'estimation en moins de 2 minutes
  → qualifie le lead (budget, type de bien, calendrier)
  → l'assigne au bon négociateur
  → relance automatiquement à J+3 si pas de réponse

  Résultat : 0 lead perdu. Vos négociateurs ne font que des
  rendez-vous qualifiés. »
```

### Minute 9-12 : Questions / objections
```
« Qu'est-ce que ça évoque pour vous ?
   Est-ce que ça répond à votre problématique ? »
→ Laisser parler. Noter les objections.
```

### Minute 12-15 : Prochaine étape
```
« Voici ce que je vous propose :
   Je vous envoie un devis personnalisé d'ici 48h.
   On se revoit la semaine prochaine pour le détailler ensemble.
   Le déploiement prend 7 à 30 jours selon le périmètre.
   Ça vous convient ? »
```

---

## 6. 🛡️ Gestion des objections

### « C'est trop cher »
```
« Je comprends. Mettons les choses en perspective :
   Un lead immobilier traité = combien de commissions en moyenne ?
   [5 000 € ? 10 000 € ?]
   Si vous en perdez 1 par mois à cause du délai de réponse...
   Le pack s'autofinance en 1 mois. »
```

### « On a déjà un CRM »
```
« Excellent — vous êtes déjà structuré. Mais votre CRM,
   c'est votre base de données. Mon travail, c'est la couche
   au-dessus : l'IA qui remplit le CRM à votre place et qui
   interagit avec vos leads avant même qu'ils n'arrivent
   dans le pipeline. »
```

### « L'IA, c'est pas pour nous / on préfère l'humain »
```
« L'humain reste au centre — c'est fondamental.
   L'IA ne remplace pas vos négociateurs.
   Elle leur mâche le travail : le lead arrive déjà qualifié,
   avec un créneau de visite proposé. Le négociateur n'a plus
   qu'à confirmer et préparer la visite.

   C'est comme avoir un assistant qui travaille la nuit. »
```

### « Je n'ai pas le temps »
```
« Justement — c'est pour ça que vous devriez me parler.
   Mes clients gagnent en moyenne 10 à 15 heures par semaine
   sur les tâches répétitives.

   15 minutes aujourd'hui pour potentiellement libérer 15 heures
   par semaine — le ratio est plutôt bon, non ? »
```

### « On va réfléchir / On vous rappelle »
```
« Bien sûr. Je vous propose un test simple : je vous envoie
   un mini-audit de votre processus actuel (gratuit, 2 pages).
   Vous le regardez, et si vous y voyez des axes d'amélioration,
   on en reparle.

   Je vous l'envoie par mail ? »
```

### « J'ai déjà quelqu'un qui fait ça / un prestataire »
```
« Super — vous avez déjà conscience de l'enjeu, c'est rare.
   Par curiosité, qu'est-ce que votre prestataire actuel
   automatise exactement ? »
→ Écouter. Chercher une lacune.
« Intéressant. Justement, le point [X] est une spécialité
   chez moi. Si jamais vous voulez un deuxième avis ou
   compléter votre dispositif actuel, je suis là. »
```

### « Les leads viennent surtout par téléphone / physique »
```
« Aujourd'hui, peut-être. Mais le marché bouge vite.
   Est-ce que vous mesurez la part de vos leads qui passent
   par votre site, les portails (SeLoger, Bien'ici), ou
   Google Business Profile ?

   (Souvent, ils sous-estiment ce canal.)
   Même 5 leads web par mois non traités, c'est 5 RDV perdus. »
```

### « C'est trop technique pour nous »
```
« C'est justement mon job. Je m'occupe de tout — de la
   configuration à la mise en route. Vous n'avez rien à
   faire techniquement.

   On fait un point de 30 minutes au début pour comprendre
   vos process, et 30 minutes à la fin pour vous former.
   Le reste, c'est moi. »
```

### « On est trop petit pour ça »
```
« C'est l'inverse. Une petite agence a encore plus besoin
   d'automatisation qu'un grand groupe — parce que vous
   n'avez pas 10 assistants pour absorber les tâches
   répétitives.

   Mon plus petit client, c'est une agence de 2 personnes
   à [ville]. Ils traitent maintenant 3× plus de leads
   sans avoir recruté. »
```

### « Et la sécurité / RGPD ? »
```
« Question essentielle. Je suis 100% conforme RGPD :
   - Registre des traitements (article 30)
   - Données hébergées en France / UE
   - Désinscription en 1 clic
   - Contrat avec annexe RGPD (article 28)

   Je vous fournis tous les documents. »
```

---

## 7. 📧 Relance post-rendez-vous

### Si devis envoyé — J+2
```
Objet : Suite à notre échange — [Nom agence]

Bonjour {{Prénom}},

Merci pour notre échange de [jour]. Comme promis, vous avez
le devis dans votre boîte mail.

Pour rappel, voici ce qu'on a vu ensemble :
- [Point 1]
- [Point 2]

Question bête : y a-t-il un point qui mériterait d'être creusé
avant qu'on se reparle ?

À [jour proposé],
Donopot
```

### Si pas de réponse au devis — J+7
```
Objet : [Nom agence] — une question ?

Bonjour {{Prénom}},

Je n'ai pas eu de retour sur le devis — et c'est normal,
vous êtes occupé.

Une seule question : est-ce que c'est le budget, le timing,
ou le périmètre qui coince ?

Dites-le-moi franchement, je préfère. Je pourrai peut-être
vous proposer une alternative.

Belle journée,
Donopot
```

---

## 8. 📧 Demande de referral (J+30 après livraison)

```
Objet : [Prénom], une question

Bonjour {{Prénom}},

J'espère que [nom de l'outil] tourne bien. Les premiers chiffres
sont bons : [X leads traités, Y heures gagnées].

Petite question : connaîtriez-vous 1 ou 2 confrères (sur [ville]
ou ailleurs) qui galèrent avec les mêmes problèmes que vous aviez
— des leads qui traînent, un CRM mal rempli ?

Une simple mise en relation par mail me suffirait.
Je m'occupe du reste.

Et évidemment, si je peux faire quoi que ce soit pour vous
en retour, n'hésitez pas.

Merci,
Donopot
```

---

## 9. 📊 Script de relance « contenu » (nurturing)

À envoyer 1× par mois aux prospects qui n'ont pas encore converti.

```
Objet : [Ville] — une stat qui m'a fait penser à vous

Bonjour {{Prénom}},

Je suis tombé sur ce chiffre cette semaine :
70% des leads immobiliers qui achètent ont choisi
l'agence qui a répondu en premier.

(Pas la moins chère. Pas la plus connue. La plus rapide.)

Je me suis dit que ça vous parlerait — à [ville],
avec le marché actuel.

Pas de pitch aujourd'hui. Juste une info.

Si vous voulez qu'on en parle un jour, ma porte est ouverte.

Belle semaine,
Donopot
```

---

## 10. ✅ Checklist avant envoi / appel

- [ ] Nom de l'agence vérifié (pas de faute)
- [ ] Prénom du contact si connu, sinon « l'équipe [Agence] »
- [ ] Ville mentionnée dans l'accroche
- [ ] Une seule question posée (pas un questionnaire)
- [ ] Un seul call-to-action (pas « appelez-moi ET envoyez-moi un mail ET visitez mon site »)
- [ ] Signature complète (nom, email, téléphone, site si existant)
- [ ] Lien de désinscription présent (email) ou formule de sortie (téléphone)
- [ ] Ton humain, pas corporate (éviter : « dans le cadre de », « par la présente », « optimal »)

---

## Conseils de rythme commercial

| Canal | Volume quotidien | Fréquence relance |
|-------|-----------------|-------------------|
| 📧 Email | 10-15 | 1 relance à J+5 |
| 📞 Téléphone | 10-15 appels | 1 relance à J+5 |
| 💬 LinkedIn | 5-10 invitations | 1 message après acceptation |
| 📰 Nurturing | — | 1× par mois |

**Règle :** Pas plus d'UNE relance par contact. Si pas de réponse après relance → nurturing mensuel uniquement.
