# Tableau de bord RH

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask&logoColor=white)
![LibreOffice](https://img.shields.io/badge/LibreOffice-Basic-orange?logo=libreoffice&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-Interactive-red?logo=javascript&logoColor=white)

Outil complet de gestion RH développé en Python/Flask avec dashboard interactif pour le suivi des congés, des habilitations et de la gestion administrative du personnel.

---

## 🎯 Fonctionnalités principales

- **Dashboard RH** : Visualisation des KPIs (effectif total, congés pris, alertes, habilitations à renouveler)
- **Gestion complète des agents** : Interface CRUD pour ajouter, modifier et supprimer des agents
- **Recherche temps réel** : Filtrage par nom, prénom, service
- **Filtres dynamiques** : Par service, par statut d'alerte
- **Pagination fluide** : Navigation avec 10 agents par page
- **Alertes visuelles** : 
  - 🔴 Rouge si solde de congés < 5 jours
  - 🟠 Orange si habilitation > 2 ans
- **Graphiques interactifs** : Visualisation des congés par service et répartition des agents (Chart.js)
- **Export CSV** : Extraction des données filtrées

## 📸 Captures d'écran

![Dashboard](screenshots/dashboard.png)
*Dashboard principal avec KPIs et graphiques interactifs*

![Liste des agents](screenshots/agents-list.png)
*Interface de gestion complète avec recherche et filtres temps réel*

---

## 🛠️ Stack technique

| Layer | Technologies |
|-------|---------------|
| **Backend** | Python 3.x, Flask |
| **Frontend** | HTML5, CSS3, JavaScript ES6+ |
| **Visualisation** | Chart.js |
| **Automatisation** | LibreOffice Basic (macros) |
| **Données** | CSV |
| **Accessibilité** | WCAG 2.1 compliant |

---

## 📦 Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)
- LibreOffice (optionnel - pour les macros)

### Quick Start

```bash
# 1. Cloner le dépôt
git clone https://github.com/ZakarieDjemaiDev/projet-ddfip
cd projet-ddfip

# 2. Installer les dépendances
pip install flask

# 3. Générer les données de test
python generate_data.py

# 4. Lancer le serveur
cd dashboard
python app.py
```

Le tableau de bord sera accessible sur **`http://127.0.0.1:5000`**

---

## 🚀 Utilisation

### Dashboard Web

Une fois le serveur Flask lancé, vous accédez à l'interface complète avec deux pages principales :

#### 📊 **Accueil / Dashboard**
- KPIs : effectif total, congés pris (moyenne), alertes, habilitations à renouveler
- Graphique : congés par service (barres)
- Graphique : répartition des agents (donut)

#### 👥 **Agents**
- **Recherche temps réel** : par nom, prénom, service
- **Filtrage** : par service, alertes uniquement
- **CRUD complet** : 
  - Ajouter un agent (modale avec validation)
  - Modifier un agent (édition en modale)
  - Supprimer un agent (confirmation requise)
- **Export CSV** : exporter les données filtrées
- **Pagination** : 10 agents par page

### Macros LibreOffice

#### Installation
1. Ouvrir LibreOffice Calc
2. **Outils** → **Macros** → **Organiser les macros** → **LibreOffice Basic**
3. Créer un nouveau module
4. Copier le contenu de `macro_suivi.bas`
5. Enregistrer

#### Utilisation
- **Importer les données** : charge `data/agents.csv` dans Calc avec mise en forme automatique
  - En-têtes gras/gris
  - Alternance de couleurs
  - Colonnes ajustées
  
- **Coloration automatique** selon règles métier :
  - 🔴 Rouge : solde < 5 jours
  - 🟠 Orange : habilitation > 2 ans

- **Exporter en PDF** : génère `rapport_agents_JJ_MM_AAAA.pdf`

---

## 📁 Structure du projet

```
projet-ddfip/
├── README.md                    # Ce fichier
├── .gitignore
├── generate_data.py             # Script de génération des données
├── rapport.py                   # Script d'analyse (optionnel)
├── macro_suivi.bas              # Macros LibreOffice Basic
│
├── dashboard/                   # Application Flask
│   ├── app.py                   # Serveur Flask & routes
│   ├── csv_handler.py           # Gestion des opérations CRUD CSV
│   ├── static/
│   │   ├── style.css            # Styles du dashboard
│   │   ├── script.js            # Logique JavaScript
│   ├── templates/
│   │   ├── index.html           # Page d'accueil & dashboard
│   │   └── agents.html          # Page de gestion des agents
│
├── data/
│   └── agents.csv               # Base de données agents (généré)
│
└── screenshots/                 # Captures d'écran
    ├── dashboard.png
    └── agents-list.png
```

---

## 📊 Format des données

Chaque agent stocké en CSV contient :

| Champ | Description | Exemple |
|-------|-------------|---------|
| **nom** | Nom de famille | Vincent |
| **prénom** | Prénom | Céline |
| **service** | Service (5 options) | Gestion publique |
| **grade** | Grade (4 niveaux) | Cadre B |
| **jours_congés_pris** | Jours consommés | 13 |
| **solde_congés** | Jours restants | 10 |
| **habilitations** | Permissions (séparées \|) | Accès système \| Données sensibles |
| **date_dernière_habilitation** | Dernier renouvellement | 25/10/2022 |

---

## 🔧 Configuration

Aucune configuration requise. Les données par défaut sont générées automatiquement.

Pour personnaliser :
- **Ajouter un service** : modifier `SERVICES` dans `dashboard/app.py` (ligne 22)
- **Modifier les grades** : ajuster `GRADES` dans `dashboard/app.py` (ligne 23)
- **Données** : éditer directement `data/agents.csv`
- **Styles** : adapter `dashboard/static/style.css`

---

## ✨ Points forts

✅ **Accessibilité** : Conforme WCAG 2.1  
✅ **Performance** : Pagination fluide, réponses rapides  
✅ **Responsive** : Adapté mobile/tablet/desktop  
✅ **Sécurité** : Validation backend des données  
✅ **Zero config** : Aucune dépendance lourde  

---

## 📝 Licence

MIT License - Voir `LICENSE` pour les détails.

---

## 👤 Auteur

**Zakarie Djemai**  
[GitHub](https://github.com/ZakarieDjemaiDev) • [LinkedIn](https://www.linkedin.com/in/zakarie-djemai) • [Portfolio](https://zakariedjemaidev.github.io/portfolio)

*Développé en formation à Metz Numeric School — Projet de démonstration pour alternance en développement web.*
