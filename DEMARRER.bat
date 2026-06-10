@echo off
REM Script de demarrage du projet DDFiP

echo.
echo ===============================================
echo Tableau de bord RH - DDFiP Moselle
echo ===============================================
echo.

if not exist "data\agents.csv" (
    echo [1] Generation des donnees...
    python generate_data.py
    echo.
)

echo [2] Affichage du rapport d'analyse...
python rapport.py
echo.

echo [3] Lancement du dashboard Flask...
echo Acces sur : http://127.0.0.1:5000
echo.
python dashboard/app.py

pause
