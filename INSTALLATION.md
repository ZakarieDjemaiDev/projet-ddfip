# Guide d'installation rapide

## 1️⃣ Prérequis

- **Python 3.7+** : [python.org](https://www.python.org/downloads/)
- **LibreOffice Calc** : [libreoffice.org](https://fr.libreoffice.org/download/) (gratuit)

Vérifier l'installation :
```bash
python --version
```

## 2️⃣ Générer les données

```bash
python generate_data.py
```

Résultat : `data/agents.csv` créé avec 50 agents fictifs.

## 3️⃣ Voir le rapport d'analyse

```bash
python rapport.py
```

Affiche un rapport détaillé : statistiques, services, habilitations, recommandations.

## 4️⃣ Utiliser la macro LibreOffice (optionnel)

### Installation de la macro

1. Ouvrir **LibreOffice Calc**
2. Aller à `Outils → Macros → Éditeur de macros`
3. Créer un nouveau module ou importer `macro_suivi.bas`
4. Copier-coller le contenu de `macro_suivi.bas` dans le module

### Créer les boutons

1. **Activer le mode création** : Formulaire → Activer le mode création
2. **Ajouter un bouton** :
   - Clic droit dans la feuille → Insérer un bouton
   - Texte du bouton : "Importer les données"
   - Double-clic dessus
   - Aller à l'onglet "Événements"
   - Lier "Exécuter" à `ImporterDonnees()`
3. **Deuxième bouton** : Répéter pour "Exporter en PDF" → `ExporterPDF()`

### Utiliser les boutons

- **Importer** : Charge le CSV, met en forme, calcule soldes
- **Exporter PDF** : Génère un PDF horodaté

## 5️⃣ Questions fréquentes

### Q: Où se trouve le CSV ?
**R:** Dans le dossier `data/agents.csv` relatif au script Python.

### Q: Comment modifier le nombre d'agents ?
**R:** Éditer `generate_data.py` ligne ~174 : `nombre = 50` → changez la valeur.

### Q: La macro ne marche pas sur mon LibreOffice ?
**R:** Vérifier que les macros sont activées : `Outils → Options → Sécurité → Macros`.
Choisir "Exécuter les macros".

### Q: Comment exporter le tableau en PDF sans la macro ?
**R:** `Fichier → Exporter en PDF` depuis LibreOffice.

### Q: Puis-je utiliser Excel à la place ?
**R:** Oui, mais la macro LibreOffice Basic fonctionne mieux. Excel utilise VBA (syntaxe différente).

## 6️⃣ Structure attendue après exécution

```
projet-ddfip/
├── data/
│   └── agents.csv              # ✓ Créé après generate_data.py
├── generate_data.py
├── rapport.py
├── macro_suivi.bas
├── README.md
└── INSTALLATION.md             # Ce fichier
```

## 7️⃣ Conseils pour la présentation en entretien

Exécutez simplement :
```bash
python generate_data.py
python rapport.py
```

Montrez :
1. Sortie du rapport dans le terminal
2. Contenu de `data/agents.csv`
3. Code source (bien commenté en français)

C'est suffisant pour montrer les compétences !

---

**Besoin d'aide ?** Consulter le README.md pour une documentation complète.
