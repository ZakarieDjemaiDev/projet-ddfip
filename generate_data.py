#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de données fictives pour la gestion RH DDFiP Moselle
Crée un fichier CSV avec des agents réalistes pour la démonstration
"""

import csv
from datetime import datetime, timedelta
import random

# Configuration des données
SERVICES = ["Fiscalité", "Gestion publique", "RH", "Contrôle fiscal", "Communication"]
GRADES = ["Contractuel", "Titulaire", "Cadre A", "Cadre B"]
HABILITATIONS = [
    "Secret défense",
    "Données sensibles",
    "Paie confidentielle",
    "Données personnelles",
    "Accès système"
]

# Données réalistes françaises
PRENOMS = [
    "Marie", "Jean", "Sophie", "Pierre", "Isabelle", "Marc", "Françoise",
    "Philippe", "Anne", "Laurent", "Céline", "Vincent", "Laurence", "Thierry",
    "Nathalie", "Bernard", "Catherine", "Claude", "Monique", "François"
]

NOMS = [
    "Dubois", "Durand", "Lefevre", "Martin", "Garcia", "Michel", "David",
    "Bertrand", "Roux", "Vincent", "Fournier", "Morel", "Girard", "Andre",
    "Leroy", "Laurent", "Dupont", "Leger", "Simon", "Moreau", "Blanc",
    "Bonnet", "Dumas", "Caillon", "Leclerc", "Renault", "Perrin", "Fontaine"
]

def generer_date_habilitation():
    """Génère une date d'habilitation entre 2 et 4 ans dans le passé"""
    jours_passes = random.randint(365 * 2, 365 * 4)
    return (datetime.now() - timedelta(days=jours_passes)).strftime("%d/%m/%Y")

def generer_donnees(nombre_agents=30):
    """
    Génère les données fictives des agents

    Args:
        nombre_agents (int): nombre d'agents à générer

    Returns:
        list: liste de dictionnaires avec les données des agents
    """
    agents = []

    for i in range(nombre_agents):
        agent = {
            "nom": random.choice(NOMS),
            "prénom": random.choice(PRENOMS),
            "service": random.choice(SERVICES),
            "grade": random.choice(GRADES),
            "jours_congés_pris": random.randint(5, 25),
            "solde_congés": random.randint(0, 18),
            "habilitations": " | ".join(random.sample(HABILITATIONS, k=random.randint(1, 3))),
            "date_dernière_habilitation": generer_date_habilitation()
        }
        agents.append(agent)

    return agents

def sauvegarder_csv(agents, chemin_fichier="data/agents.csv"):
    """
    Sauvegarde les données dans un fichier CSV

    Args:
        agents (list): liste des agents à sauvegarder
        chemin_fichier (str): chemin de destination du fichier
    """
    entetes = [
        "nom", "prénom", "service", "grade", "jours_congés_pris",
        "solde_congés", "habilitations", "date_dernière_habilitation"
    ]

    with open(chemin_fichier, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entetes)
        writer.writeheader()
        writer.writerows(agents)

    print(f"[OK] {len(agents)} agents generes et sauvegardes dans '{chemin_fichier}'")

if __name__ == "__main__":
    # Générer 30 agents réalistes
    donnees = generer_donnees(30)

    # Sauvegarder dans le CSV
    sauvegarder_csv(donnees)

    # Afficher un aperçu
    print("\nAperçu des 5 premiers agents :")
    print("-" * 80)
    for agent in donnees[:5]:
        print(f"  {agent['nom'].upper()} {agent['prénom']} - {agent['service']} ({agent['grade']})")
