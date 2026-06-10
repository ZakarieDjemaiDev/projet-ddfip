#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Serveur Flask pour le tableau de bord RH DDFiP Moselle (VERSION PROFESSIONNELLE)
Tableau de bord complet avec CRUD, recherche, filtres et exports
"""

from flask import Flask, render_template, jsonify, request, send_file
from datetime import datetime, timedelta
from collections import defaultdict
import csv
import io
import json
from pathlib import Path

# Import du module de gestion CSV
from csv_handler import lire_agents, sauvegarder_agents, ajouter_agent, mettre_a_jour_agent, supprimer_agent

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

SERVICES = ["Fiscalité", "Gestion publique", "RH", "Contrôle fiscal", "Communication"]
GRADES = ["Contractuel", "Titulaire", "Cadre A", "Cadre B"]

# ==================== Utilitaires ====================

def calculer_kpis(agents):
    """Calcule les KPIs pour l'affichage"""
    if not agents:
        return {"total": 0, "conges_moyen": 0, "habilitations_a_renouveler": 0, "alertes_conges": 0}

    total = len(agents)
    conges_moyen = sum(int(a.get('jours_congés_pris', 0)) for a in agents) / total if total > 0 else 0

    limite_date = datetime.now() - timedelta(days=730)
    habilitations_a_renouveler = 0
    alertes_conges = 0

    for agent in agents:
        solde = int(agent.get('solde_congés', 0))
        if solde < 5:
            alertes_conges += 1

        date_str = agent.get('date_dernière_habilitation', '')
        try:
            date_hab = datetime.strptime(date_str, "%d/%m/%Y")
            if date_hab < limite_date:
                habilitations_a_renouveler += 1
        except ValueError:
            pass

    return {
        "total": total,
        "conges_moyen": round(conges_moyen, 1),
        "habilitations_a_renouveler": habilitations_a_renouveler,
        "alertes_conges": alertes_conges
    }

def enrichir_agent(agent, index):
    """
    Ajoute des informations calculées a un agent

    Args:
        agent (dict): donnees agent
        index (int): position dans la liste

    Returns:
        dict: agent enrichi
    """
    solde = int(agent.get('solde_congés', 0))
    date_hab = agent.get('date_dernière_habilitation', '')

    alerte_solde = solde < 5
    alerte_habilitation = False

    try:
        date_hab_obj = datetime.strptime(date_hab, "%d/%m/%Y")
        limite = datetime.now() - timedelta(days=730)
        alerte_habilitation = date_hab_obj < limite
    except ValueError:
        pass

    return {
        'index': index,
        'nom': agent.get('nom', ''),
        'prénom': agent.get('prénom', ''),
        'service': agent.get('service', ''),
        'grade': agent.get('grade', ''),
        'jours_congés_pris': agent.get('jours_congés_pris', ''),
        'solde_congés': solde,
        'habilitations': agent.get('habilitations', ''),
        'date_dernière_habilitation': date_hab,
        'alerte_solde': alerte_solde,
        'alerte_habilitation': alerte_habilitation,
        'a_alerte': alerte_solde or alerte_habilitation
    }

def preparer_stats_services(agents):
    """Prepare les statistiques des conges par service"""
    stats = defaultdict(lambda: {"nombre": 0, "conges_moyen": 0, "total_conges": 0})

    for agent in agents:
        service = agent.get('service', 'Inconnu')
        conges = int(agent.get('jours_congés_pris', 0))
        stats[service]['nombre'] += 1
        stats[service]['total_conges'] += conges

    for service in stats:
        stats[service]['conges_moyen'] = round(
            stats[service]['total_conges'] / stats[service]['nombre'], 1
        )

    return dict(stats)

def preparer_repartition_services(agents):
    """Prepare les donnees pour le graphique de repartition"""
    repartition = defaultdict(int)
    for agent in agents:
        service = agent.get('service', 'Inconnu')
        repartition[service] += 1
    return dict(repartition)

# ==================== Routes - Pages ====================

@app.route('/')
def index():
    """Affiche le dashboard principal"""
    agents = lire_agents()
    agents_enrichis = [enrichir_agent(a, i) for i, a in enumerate(agents)]

    kpis = calculer_kpis(agents)
    stats_services = preparer_stats_services(agents)
    repartition = preparer_repartition_services(agents)

    # Convertir les donnees en JSON pour le template
    donnees_barres = json.dumps(
        {service: stats['conges_moyen'] for service, stats in stats_services.items()},
        ensure_ascii=False
    )
    donnees_donut = json.dumps(
        {service: nombre for service, nombre in repartition.items()},
        ensure_ascii=False
    )

    return render_template(
        'index.html',
        kpis=kpis,
        stats_services=stats_services,
        repartition=repartition,
        agents=agents_enrichis,
        services=SERVICES,
        grades=GRADES,
        date_du_jour=datetime.now().strftime("%d/%m/%Y"),
        donnees_barres=donnees_barres,
        donnees_donut=donnees_donut
    )

@app.route('/agents')
def agents_page():
    """Affiche la page de gestion des agents"""
    agents = lire_agents()
    agents_enrichis = [enrichir_agent(a, i) for i, a in enumerate(agents)]

    return render_template(
        'agents.html',
        agents=agents_enrichis,
        services=SERVICES,
        grades=GRADES,
        date_du_jour=datetime.now().strftime("%d/%m/%Y")
    )

# ==================== Routes - API ====================

@app.route('/api/agents')
def api_agents():
    """Retourne la liste complete des agents en JSON"""
    agents = lire_agents()
    agents_enrichis = [enrichir_agent(a, i) for i, a in enumerate(agents)]
    return jsonify(agents_enrichis)

@app.route('/api/agent/add', methods=['POST'])
def api_ajouter_agent():
    """Ajoute un nouvel agent"""
    try:
        donnees = request.get_json()
        succes, message = ajouter_agent(donnees)

        if succes:
            agents = lire_agents()
            return jsonify({
                'success': True,
                'message': message,
                'agents': [enrichir_agent(a, i) for i, a in enumerate(agents)]
            })
        else:
            return jsonify({'success': False, 'message': message}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': f"Erreur : {str(e)}"}), 500

@app.route('/api/agent/update/<int:index>', methods=['POST'])
def api_mettre_a_jour_agent(index):
    """Met a jour un agent"""
    try:
        donnees = request.get_json()
        succes, message = mettre_a_jour_agent(index, donnees)

        if succes:
            agents = lire_agents()
            return jsonify({
                'success': True,
                'message': message,
                'agents': [enrichir_agent(a, i) for i, a in enumerate(agents)]
            })
        else:
            return jsonify({'success': False, 'message': message}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': f"Erreur : {str(e)}"}), 500

@app.route('/api/agent/delete/<int:index>', methods=['DELETE'])
def api_supprimer_agent(index):
    """Supprime un agent"""
    try:
        succes, message = supprimer_agent(index)

        if succes:
            agents = lire_agents()
            return jsonify({
                'success': True,
                'message': message,
                'agents': [enrichir_agent(a, i) for i, a in enumerate(agents)]
            })
        else:
            return jsonify({'success': False, 'message': message}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': f"Erreur : {str(e)}"}), 500

@app.route('/api/export/csv')
def api_export_csv():
    """Exporte les donnees en CSV"""
    try:
        agents = lire_agents()

        entetes = [
            "nom", "prénom", "service", "grade", "jours_congés_pris",
            "solde_congés", "habilitations", "date_dernière_habilitation"
        ]

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=entetes)
        writer.writeheader()
        writer.writerows(agents)

        output.seek(0)
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name=f"agents_{datetime.now().strftime('%d_%m_%Y')}.csv"
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("[DEMARRAGE] Tableau de bord RH - DDFiP Moselle (Professional)")
    print("=" * 70)
    print("  Accedez au dashboard sur : http://127.0.0.1:5000")
    print("  Appuyez sur Ctrl+C pour arreter le serveur")
    print("=" * 70 + "\n")
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
