# PRESENTATION ENTRETIEN - DDFiP MOSELLE

## ACCROCHE (30 secondes)

"J'ai crée un projet complet de gestion RH qui combine les technologies 
demandées par la DDFiP : Python, macros LibreOffice, automatisation et 
datavisualisation. Ce n'est pas juste une démo technique - c'est une 
approche opérationnelle du problème que vous avez probablement au quotidien."

---

## 1. PYTHON & AUTOMATISATION (2 minutes)

### La situation réelle à la DDFiP
- Chaque mois : traiter des données agents (congés, habilitations, mutations...)
- Actuellement : feuilles Excel = erreurs, pas de synthèse
- Ce qu'il manque : une source unique de vérité, des alertes automatiques

### Ce que j'ai construit
Le script `generate_data.py` :
  ✓ Génère 30 agents avec données réalistes
  ✓ Services variés (Fiscalité, RH, Gestion publique...)
  ✓ Grades, congés, habilitations cohérents

Le script `rapport.py` :
  ✓ Lit les données
  ✓ Calcule automatiquement les alertes :
    - Agents avec solde congés < 5 jours
    - Habilitations expirées (> 2 ans)
    - Moyennes par service
  ✓ Affiche un rapport propre et lisible

### Avantage
Pas d'erreur manuelle, rapide à exécuter, résultat structuré.

**À dire en entretien :**
"Ce type d'automatisation, appliqué à vos vraies données, économiserait 
plusieurs heures de travail RH par mois et éliminerait les erreurs manuelles."

---

## 2. MACROS LIBREOFFICE (2 minutes)

### Pourquoi c'est important
- La DDFiP utilise LibreOffice (pas Microsoft)
- Les données arrivent souvent en CSV/Excel
- Les utilisateurs RH connaissent Calc, pas Python

### Ce que j'ai construit
Une macro LibreOffice Basic (macro_suivi.bas) qui :

1. **ImporterDonnees()** :
   - Importe data/agents.csv dans une feuille "Agents"
   - Un clic = données importées

2. **Mise en forme automatique** :
   - En-têtes en gras + couleur grise
   - Colonnes ajustées à la largeur du contenu
   - Alternance de couleurs (blanc/gris) pour lisibilité

3. **Alertes coloriées** :
   - Rouge = solde < 5 jours (urgence)
   - Orange = habilitation > 2 ans (renouvellement)
   - Les lignes problématiques ressortent immédiatement

4. **Export PDF** :
   - Génère rapport_agents_DD_MM_AAAA.pdf

### Avantage
Aucune compétence technique requise pour l'utilisateur final. 
C'est de l'automatisation RH opérationnelle.

**À dire en entretien :**
"Une RH peut simplement cliquer sur le bouton 'Importer' et avoir un rapport 
complet et mis en forme en 2 secondes, au lieu de 20 minutes de tri manuel."

---

## 3. DASHBOARD DATAVISUALISATION (2 minutes)

### La limite de Calc
- Calc affiche les données
- Mais ça ne raconte pas d'histoire
- Les chiffres se perdent dans les lignes

### Ce que j'ai construit
Un dashboard web Flask avec :

**KPIs visibles immédiatement** :
  - Total d'agents
  - Moyenne congés pris
  - Nombre d'habilitations à renouveler

**Graphiques interactifs** (Chart.js) :
  - Barres : congés pris par service
    → Quelle équipe a consommé le plus ?
  - Camembert : répartition agents par service
    → Quelle est la répartition des effectifs ?

**Tableau complet** :
  - Tous les détails agents
  - Lignes coloriées selon les alertes
  - Tri possible sur chaque colonne

### Avantage
Vue d'ensemble immédiate + données détaillées en un seul endroit.
C'est ce qu'on appelle une "single source of truth".

**À dire en entretien :**
"Au lieu de se demander 'combien d'agents sont en alerte ce mois-ci ?', 
la réponse est là, graphiquement, en une seconde."

---

## 4. STACK TECHNIQUE (1 minute)

### Pourquoi ces choix ?

**Python 3** (demandé dans l'offre)
  ✓ Scripts d'automatisation RH
  ✓ Traitement de données
  ✓ Calculs, statistiques

**LibreOffice Basic** (déjà utilisé à la DDFiP)
  ✓ Les gens connaissent Calc
  ✓ Pas de dépendance externe
  ✓ Macro = automatisation immédiate

**Flask** (léger, adapté)
  ✓ Pas lourd comme Django
  ✓ Pas de build complexe
  ✓ Déployable sur une petite infra

**Chart.js** (CDN, zero install)
  ✓ Graphiques sans npm/webpack
  ✓ Responsive, propre
  ✓ Facile à maintenir

**CSV comme données**
  ✓ Universel
  ✓ Pas de serveur DB complexe
  ✓ Peut venir de n'importe où

### Points forts
- Rien de lourd
- Rien qui ne tienne dans une infra RH type
- Tout maintainable par un petit développeur

**À dire en entretien :**
"Je n'ai pas utilisé les derniers outils à la mode. J'ai choisi ce qui 
marche, ce qui dure, et ce qui s'intègre avec votre infrastructure."

---

## QUESTIONS ATTENDUES

### Q1: Comment tu gères les vraies données RH (sensibles) ?
**Réponse :**
"Cette démo utilise des données fictives. Avec des vraies données :
- Chiffrement des données sensibles
- Contrôle d'accès (qui voit quoi?)
- Audit des modifications
- Respect du RGPD
- Sauvegardes régulières

La structure reste la même, on ajoute juste la sécurité."

### Q2: Comment ça s'intègre avec vos systèmes existants?
**Réponse :**
"Actuellement c'est du CSV pour la démo. En production :
- Lecture depuis votre base RH existante
- Via une API si vous avez
- Ou import quotidien depuis vos exports
- Les traitements (alertes, etc) restent les mêmes"

### Q3: Ça fera combien de temps à maintenir ?
**Réponse :**
"Une fois déployé : 
- 5 min/mois pour relancer les imports
- 1 heure/mois pour vérifier/documenter
- Si besoin d'ajustement : 1-2 jours
(C'est très peu comparé au temps économisé)"

### Q4: Et si les données changent de format ?
**Réponse :**
"L'avantage de Python : très flexible. Adapter le script à un nouveau 
format CSV ou ajouter une source de données = quelques heures max.
C'est vraiment conçu pour évoluer."

### Q5: Pourquoi pas une solution du commerce ?
**Réponse :**
"Deux raisons :
1. Coût : une solution toute-prête coûte cher
2. Flexibilité : avec du code, c'est votre outil, vous le changez comme vous voulez

Ici, c'est sur-mesure pour les besoins DDFiP."

---

## DEMONSTRATION EN ENTRETIEN

Si possible, préparez à l'avance sur votre ordi :

1. Montrez le rapport terminal :
   ```
   python rapport.py
   ```
   → Les alertes ressortent immédiatement

2. Montrez le dashboard :
   ```
   python dashboard/app.py
   ```
   → Ouvrez http://localhost:5000
   → Montrez les KPIs, les graphiques

3. Si possible, ouvrez LibreOffice et montrez la macro
   → Clic sur "ImporterDonnees"
   → Les données arrivent avec les couleurs
   → Les alertes sont visibles

**Timing :** 3-5 minutes max, avec l'enthousiasme

---

## DERNIER POINT - LES CHIFFRES

Préparez mentalement les chiffres du projet à annoncer :
- 30 agents fictifs réalistes
- 5 services différents
- 4 grades différents
- 5 types d'habilitations
- 8 agents avec alerte congés faibles
- 30 agents avec habilitations à renouveler

(Les chiffres changent à chaque fois qu'on lance generate_data.py, 
c'est normal, c'est aléatoire)

---

## CONCLUSION

"Cette approche c'est :
✓ De l'automatisation RH opérationnelle
✓ Facile à maintenir (Python simple, pas de framework lourd)
✓ Adaptée à votre contexte (LibreOffice, petite infra)
✓ Extensible (on peut ajouter des alertes, des exports, des API)
✓ Peu coûteuse (juste du code open-source)

Je suis prêt à discuter comment adapter ça exactement à vos besoins."
