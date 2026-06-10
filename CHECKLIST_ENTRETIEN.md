# ✓ Checklist avant l'entretien

À vérifier avant d'aller à votre entretien à la DDFiP ! 

## 📋 2 jours avant

- [ ] **Relire** PRESENTATION_ENTRETIEN.md une fois complètement
- [ ] **Tester** les scripts sur votre machine :
  ```bash
  python generate_data.py
  python rapport.py
  ```
- [ ] Vérifier que tout marche (pas de messages d'erreur)
- [ ] **Vérifier les fichiers** :
  - [ ] `data/agents.csv` existe et a 50 lignes
  - [ ] Tous les fichiers .py sont commentés en français
  - [ ] `macro_suivi.bas` s'affiche correctement
- [ ] **Lire** les questions probables dans PRESENTATION_ENTRETIEN.md
- [ ] **Imprimer** ce document (pour relire 1h avant)

---

## 🖥️ Jour de l'entretien - Matériel

Apporter avec vous :

- [ ] **Laptop/PC** avec le projet dessus
- [ ] **Clé USB** (backup, au cas où)
- [ ] **Papier/stylo** (notes)
- [ ] **Impression** de PRESENTATION_ENTRETIEN.md
- [ ] **Chargeur** (batterie = stress supplémentaire)

Sur l'ordi :

- [ ] Python installé et fonctionnel (`python --version`)
- [ ] LibreOffice Calc ouvert (optionnel mais bien vu)
- [ ] Terminal/PowerShell prêt à lancer les scripts
- [ ] Éditeur de code (VS Code, Notepad++, etc.)
- [ ] Le dossier `projet-ddfip/` en accès facile (bureau ou dossier racine)

---

## 🎤 1h avant l'entretien

Relire cette checklist :

**Préparation mentale**

- [ ] Relire les "Points forts à rappeler" de PRESENTATION_ENTRETIEN.md
- [ ] Bien dormir la nuit d'avant 😴
- [ ] Pas trop de café (mains qui tremblent = pas bon)
- [ ] Arriver 15 min en avance (pas de stress de retard)

**Tech check**

- [ ] Tester les scripts encore une fois
- [ ] Ouvrir les fichiers Python dans l'éditeur
- [ ] Vérifier que le CSV s'ouvre bien dans Excel/Calc
- [ ] Allumer la macro LibreOffice (optionnel)

**Plan mental**

- [ ] Réciter les 6 étapes de présentation
  1. Aperçu général (30 sec)
  2. Génération de données (1-2 min)
  3. Analyse et rapport (1-2 min)
  4. Automatisation LibreOffice (1 min, optionnel)
  5. Code commenté (30 sec)
  6. Compétences démontrées (30 sec)

- [ ] Avoir 2-3 questions à poser à la fin (montre l'intérêt)

---

## 🎯 Pendant la présentation

### ✅ À faire

- [ ] Démarrer par un sourire et merci de les rencontrer
- [ ] **Lancer les scripts** (ne pas juste parler, montrer)
- [ ] **Pointer le résultat** ("Vous voyez ici..." au lieu de "Il y a...")
- [ ] **Parler lentement** (stress = parler vite)
- [ ] **Chercher la compréhension** ("C'est clair ?" "Des questions ?")
- [ ] **Écouter les questions** (vraiment, pas juste attendre le tour)
- [ ] **Répondre de manière honnête** (si vous savez pas, dites le)
- [ ] **Montrer l'enthousiasme** (c'est votre projet, vous devez l'aimer !)
- [ ] **Rester dans le timing** (5-7 min de présentation max)

### ❌ À ÉVITER

- [ ] Parler trop vite (professionnel = maître de soi)
- [ ] Surcharger de détails techniques (RH ne comprennent pas `for i in range()`)
- [ ] Critiquer le projet ("C'est pas terrible mais...")
- [ ] Inventer des choses ("J'utilise AWS" si non)
- [ ] Dire "euh", "tu sais", "genre" (improfessionnel)
- [ ] Montrer du manque de confiance ("J'espère que ça marche...")
- [ ] Parler dans le vide (toujours pointer le code/terminal)
- [ ] Oublier que les RH ne sont pas devs (vulgariser)
- [ ] Faire 20 minutes de présentation (entretien, pas conférence)

---

## 💬 Questions probables - Réponses courtes

### Q: "Pourquoi ce projet ?"
**R:** "Pour montrer comment j'automatiserais les tâches RH récurrentes à la DDFiP."

### Q: "Combien de temps tu as passé dessus ?"
**R:** "Prototype en ~1-2 jours. Mais extensible facilement."

### Q: "Ça marche sur Linux aussi ?"
**R:** "Oui, Python est multi-plateforme. LibreOffice aussi."

### Q: "Comment tu géreriez les vraies données sensibles ?"
**R:** "Chiffrement, authentification, audit trail, RGPD."

### Q: "Ça scale à combien d'agents ?"
**R:** "CSV : ~10k agents max. Au-delà : base de données."

### Q: "Tu ferais ça en prod ?"
**R:** "Pas tel quel. J'ajouterais DB, API, tests, sécurité."

---

## 🏆 À la fin : Vos 3 questions de RH

Vous posez 3 questions (curiosité = bon signe) :

1. **Question technique** : "Quel système RH utilisez-vous actuellement à la DDFiP ?"
2. **Question métier** : "Quelles sont les tâches RH les plus récurrentes ?"
3. **Question entretien** : "Quel serait le rôle de l'alternant sur ce type de projet ?"

(Les questions = vous posez, pas eux qui vous dominent)

---

## ✅ Après l'entretien

- [ ] Envoyer un **email de remerciement** dans les 24h
- [ ] Mentionner un **détail** de la conversation (montre attention)
- [ ] Reconfirmer **votre intérêt** pour le poste
- [ ] Proposer un **moyen de contact** clair

**Email template** :

```
Objet : Merci pour l'entretien du [date]

Bonjour [Nom],

Merci beaucoup de m'avoir consacré du temps ce [date].
Notre discussion sur [point spécifique] m'a vraiment intéressé.

Je reste disponible si vous avez des questions supplémentaires.

Cordialement,
Zakarie Djemai
```

---

## 🎓 Points à renforcer MAINTENANT

### Si vous êtes faible en Python
- [ ] Relire `generate_data.py` et pouvoir l'expliquer ligne par ligne
- [ ] Comprendre les listes, dicts, fichiers (CSV)
- [ ] Pouvoir modifier `NOMBRE_AGENTS` et relancer le script

### Si vous êtes faible en LibreOffice
- [ ] Ne pas présenter la macro (skip it)
- [ ] Dire : "J'ai aussi créé une macro, mais ce qui compte c'est Python"
- [ ] Montrer juste les boutons, pas le code Basic

### Si vous êtes faible sur RH
- [ ] Relire les sections "Pédagogie" dans README.md
- [ ] Comprendre : congés, catégories (A/B/C), habilitations, services
- [ ] Pouvoir expliquer à quelqu'un d'autre

---

## 🚨 Plan B (si ça bug)

### "Mon PC affiche une erreur"

✅ Restez calme, c'est normal
✅ Dites : "Pas de problème, regardons le code plutôt"
✅ Ouvrez le fichier .py dans l'éditeur
✅ Montrez le code commenté (ça suffit)
✅ Dites : "Chez moi ça marche, probablement un truc d'env"

### "J'ai oublié mon laptop"

❌ PROBLÈME
✅ Solution : avoir des **captures d'écran** sur votre téléphone
- Résultat de `python generate_data.py`
- Résultat de `python rapport.py`
- Code Python dans éditeur
- CSV ouvert dans Calc

### "On me pose une question que je ne comprends pas"

✅ Dites : "Bonne question, peux-tu clarifier ?"
✅ Écoutez bien la question
✅ Répondez honnêtement : "Je ne sais pas, mais je pourrais apprendre"
✅ Pas de "euh...", pas de mensonge

---

## 📊 Scoring - Êtes-vous prêt ?

Complétez cette partie 1h avant d'y aller :

| Aspect | Score (0-10) | Commentaire |
|--------|:----:|-----------|
| Code Python compris | __/10 | |
| Projet marche sur ma machine | __/10 | |
| Peut expliquer sans slides | __/10 | |
| Timing maîtrisé (5-7 min) | __/10 | |
| Réponses aux questions clés | __/10 | |
| Confiance générale | __/10 | |

**Total** : __/60

- **54+** : Vous êtes prêt ! Go ! 🚀
- **45-54** : Presque, relisez un peu plus
- **< 45** : Pratiquez encore (replay mental)

---

## 🎪 Dernier trick : Le "One-liner" clair

Préparez-vous à dire **en une phrase** ce que c'est :

> "C'est un outil Python qui génère des données RH fictives, les analyse 
> avec des recommandations, et expose un rapport lisible pour la DDFiP."

**Ou plus court** :

> "Outil Python pour automatiser le suivi des agents : génération, 
> analyse, rapport."

Vous devez pouvoir le dire en 10 secondes max.

---

## 🍀 Mindset avant d'entrer

**Pas** : "Oh non, je vais me planter"
**Mais** : "Je vais montrer ce que je sais faire"

**Pas** : "Ils vont me juger"
**Mais** : "Ils veulent juste voir si je m'entends avec la team"

**Pas** : "Je dois avoir la bonne réponse"
**Mais** : "Je dois montrer comment je réfléchis"

---

## ✅ Final check (5 min avant)

- [ ] Respirer profondément (3x)
- [ ] Relire le "One-liner"
- [ ] Vérifier pantalon/chemise pas froissé (details!)
- [ ] Téléphone en silence (pas vibrant dans le sac)
- [ ] Laptop fermé (ouverture dramatique 🎬)
- [ ] Sourire ! Vous allez killer cet entretien.

---

**Vous pouvez le faire ! 💪**

*Revenir à cette page si stress ou oubli.*

**Bonne chance !** 🎯
