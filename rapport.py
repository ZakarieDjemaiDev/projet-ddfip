#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rapport d'analyse des données RH DDFiP Moselle
Lit le CSV d'agents et affiche un rapport terminal formaté
"""

import csv
from datetime import datetime, timedelta
from collections import defaultdict

def lire_agents(chemin_fichier="data/agents.csv"):
    """
    Lit les agents depuis le fichier CSV

    Args:
        chemin_fichier (str): chemin du fichier CSV

    Returns:
        list: liste des agents
    """
    agents = []
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as csvfile:
            lecteur = csv.DictReader(csvfile)
            agents = list(lecteur)
    except FileNotFoundError:
        print(f"[ERREUR] Le fichier '{chemin_fichier}' n'existe pas")
        print("   Lancez d'abord : python generate_data.py")
        exit(1)

    return agents

def analyser_services(agents):
    """Compte les agents par service"""
    comptage = defaultdict(int)
    for agent in agents:
        comptage[agent['service']] += 1
    return dict(sorted(comptage.items()))

def calculer_conges_moyens(agents):
    """Calcule la moyenne des congés pris"""
    if not agents:
        return 0
    total = sum(int(a['jours_congés_pris']) for a in agents)
    return total / len(agents)

def agents_solde_faible(agents, seuil=5):
    """
    Retourne les agents avec un solde de congés faible

    Args:
        agents (list): liste des agents
        seuil (int): seuil de solde faible

    Returns:
        list: agents avec solde < seuil
    """
    return [a for a in agents if int(a['solde_congés']) < seuil]

def habilitations_expirees(agents, jours_limite=730):
    """
    Retourne les agents avec habilitations expirées (> 2 ans)

    Args:
        agents (list): liste des agents
        jours_limite (int): nombre de jours pour considérer comme expiré

    Returns:
        list: agents avec habilitations expirées
    """
    agents_expires = []
    limite_date = datetime.now() - timedelta(days=jours_limite)

    for agent in agents:
        date_str = agent['date_dernière_habilitation']
        try:
            date_hab = datetime.strptime(date_str, "%d/%m/%Y")
            if date_hab < limite_date:
                agents_expires.append(agent)
        except ValueError:
            pass

    return agents_expires

def afficher_rapport(agents):
    """Affiche un rapport formaté dans le terminal"""
    print("\n" + "=" * 80)
    print(" " * 15 + "RAPPORT D'ANALYSE RH - DDFiP MOSELLE")
    print("=" * 80)
    print(f"Date du rapport : {datetime.now().strftime('%d/%m/%Y a %H:%M:%S')}\n")

    # Nombre total d'agents
    print(f"[TOTAL] Nombre total d'agents : {len(agents)}\n")

    # Agents par service
    print("[STATS] Repartition par service :")
    print("-" * 40)
    services = analyser_services(agents)
    for service, nombre in services.items():
        pourcentage = (nombre / len(agents)) * 100
        print(f"  - {service:.<25} {nombre:2d} agents ({pourcentage:5.1f}%)")
    print()

    # Congés
    moyenne_conges = calculer_conges_moyens(agents)
    print("[CONGES] Conges pris (en moyenne) : {:.1f} jours par agent\n".format(moyenne_conges))

    # Soldes faibles
    faibles = agents_solde_faible(agents)
    print(f"[ALERTE] Agents avec solde faible (< 5 jours) : {len(faibles)}")
    if faibles:
        print("-" * 40)
        for agent in faibles:
            nom_complet = f"{agent['prénom']} {agent['nom']}"
            print(f"  - {nom_complet:.<30} {agent['solde_congés']} jours | {agent['service']}")
    print()

    # Habilitations expirées
    expires = habilitations_expirees(agents)
    print(f"[SECURITE] Habilitations a renouveler (> 2 ans) : {len(expires)}")
    if expires:
        print("-" * 40)
        for agent in expires:
            nom_complet = f"{agent['prénom']} {agent['nom']}"
            date_hab = agent['date_dernière_habilitation']
            print(f"  - {nom_complet:.<30} {date_hab} | {agent['service']}")
    print()

    print("=" * 80 + "\n")

if __name__ == "__main__":
    # Lire les données
    donnees = lire_agents()

    # Afficher le rapport
    afficher_rapport(donnees)
