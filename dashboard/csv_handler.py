# -*- coding: utf-8 -*-
"""
Module de gestion des donnees CSV
Centralise la lecture/ecriture des agents dans le fichier agents.csv
"""

import csv
import os
from datetime import datetime, timedelta
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "agents.csv"

def lire_agents():
    """Lit tous les agents depuis le CSV"""
    agents = []
    try:
        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            agents = list(lecteur) if lecteur else []
    except FileNotFoundError:
        pass
    return agents

def sauvegarder_agents(agents):
    """Sauvegarde les agents dans le CSV"""
    if not agents:
        return
    
    entetes = [
        "nom", "prénom", "service", "grade", "jours_congés_pris",
        "solde_congés", "habilitations", "date_dernière_habilitation"
    ]
    
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=entetes)
        writer.writeheader()
        writer.writerows(agents)

def ajouter_agent(donnees):
    """
    Ajoute un nouvel agent
    
    Args:
        donnees (dict): dictionnaire avec les champs de l'agent
        
    Returns:
        tuple: (succes, message)
    """
    try:
        if not all(k in donnees for k in ["nom", "prénom", "service", "grade"]):
            return False, "Champs obligatoires manquants"
        
        agents = lire_agents()
        
        nouvel_agent = {
            "nom": donnees.get("nom", "").strip(),
            "prénom": donnees.get("prénom", "").strip(),
            "service": donnees.get("service", "").strip(),
            "grade": donnees.get("grade", "").strip(),
            "jours_congés_pris": donnees.get("jours_congés_pris", "0"),
            "solde_congés": donnees.get("solde_congés", "0"),
            "habilitations": donnees.get("habilitations", ""),
            "date_dernière_habilitation": donnees.get("date_dernière_habilitation", 
                                                     datetime.now().strftime("%d/%m/%Y"))
        }
        
        agents.append(nouvel_agent)
        sauvegarder_agents(agents)
        return True, "Agent ajoute avec succes"
        
    except Exception as e:
        return False, f"Erreur : {str(e)}"

def mettre_a_jour_agent(index, donnees):
    """
    Met a jour un agent
    
    Args:
        index (int): index de l'agent
        donnees (dict): nouvelels donnees
        
    Returns:
        tuple: (succes, message)
    """
    try:
        agents = lire_agents()
        
        if index < 0 or index >= len(agents):
            return False, "Agent introuvable"
        
        agents[index] = {
            "nom": donnees.get("nom", agents[index].get("nom", "")).strip(),
            "prénom": donnees.get("prénom", agents[index].get("prénom", "")).strip(),
            "service": donnees.get("service", agents[index].get("service", "")).strip(),
            "grade": donnees.get("grade", agents[index].get("grade", "")).strip(),
            "jours_congés_pris": donnees.get("jours_congés_pris", agents[index].get("jours_congés_pris", "0")),
            "solde_congés": donnees.get("solde_congés", agents[index].get("solde_congés", "0")),
            "habilitations": donnees.get("habilitations", agents[index].get("habilitations", "")),
            "date_dernière_habilitation": donnees.get("date_dernière_habilitation", 
                                                     agents[index].get("date_dernière_habilitation", ""))
        }
        
        sauvegarder_agents(agents)
        return True, "Agent mis a jour avec succes"
        
    except Exception as e:
        return False, f"Erreur : {str(e)}"

def supprimer_agent(index):
    """
    Supprime un agent
    
    Args:
        index (int): index de l'agent
        
    Returns:
        tuple: (succes, message)
    """
    try:
        agents = lire_agents()
        
        if index < 0 or index >= len(agents):
            return False, "Agent introuvable"
        
        agents.pop(index)
        sauvegarder_agents(agents)
        return True, "Agent supprime avec succes"
        
    except Exception as e:
        return False, f"Erreur : {str(e)}"

def generer_csv_export(donnees_agents, filename="agents"):
    """Genere un fichier CSV a exporter"""
    try:
        entetes = [
            "nom", "prénom", "service", "grade", "jours_congés_pris",
            "solde_congés", "habilitations", "date_dernière_habilitation"
        ]
        
        chemin = f"/tmp/{filename}.csv"
        with open(chemin, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=entetes)
            writer.writeheader()
            writer.writerows(donnees_agents)
        
        return True, chemin
    except Exception as e:
        return False, str(e)
