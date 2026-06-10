' Macro LibreOffice Basic pour DDFiP Moselle
' Suivi des agents et gestion des habilitations
' ============================================

Sub ImporterDonnees()
    ' Procédure principale pour importer les données du CSV
    
    Dim oDoc As Object
    Dim oSheet As Object
    Dim sCheminFichier As String
    
    oDoc = ThisComponent
    
    ' Créer ou récupérer la feuille "Agents"
    On Error Resume Next
    oSheet = oDoc.Sheets.getByName("Agents")
    On Error GoTo 0
    
    If IsNull(oSheet) Then
        oDoc.Sheets.insertNewByName("Agents", 0)
        oSheet = oDoc.Sheets.getByName("Agents")
    End If
    
    ' Demander le chemin du fichier CSV
    sCheminFichier = "data\agents.csv"
    
    ' Importer les données
    ImporterCSV(oSheet, sCheminFichier)
    
    ' Appliquer la mise en forme
    MettreEnForme(oSheet)
    
    ' Colorier les alertes
    ColorierAlertes(oSheet)
    
    MsgBox "Données importées et mises en forme !", 64, "Succès"
End Sub

Sub ImporterCSV(oSheet As Object, sCheminFichier As String)
    ' Importe le CSV dans la feuille
    
    Dim oFile As Object
    Dim sLigne As String
    Dim aChamps() As String
    Dim iLigne As Integer
    Dim iCol As Integer
    
    Const SEPARATEUR = ","
    
    iLigne = 1
    
    ' Lire et importer le fichier CSV
    On Error GoTo ErrHandler
    
    Dim iHandle As Integer
    iHandle = FreeFile()
    Open sCheminFichier For Input As iHandle
    
    ' Sauter la première ligne (en-têtes)
    Line Input #iHandle, sLigne
    
    ' Importer les en-têtes
    aChamps = Split(sLigne, SEPARATEUR)
    For iCol = LBound(aChamps) To UBound(aChamps)
        oSheet.getCellByPosition(iCol, 0).setString(Trim(aChamps(iCol)))
    Next iCol
    
    ' Importer les données
    iLigne = 2
    While Not EOF(iHandle)
        Line Input #iHandle, sLigne
        If Len(sLigne) > 0 Then
            aChamps = Split(sLigne, SEPARATEUR)
            For iCol = LBound(aChamps) To UBound(aChamps)
                oSheet.getCellByPosition(iCol, iLigne - 1).setString(Trim(aChamps(iCol)))
            Next iCol
            iLigne = iLigne + 1
        End If
    Wend
    
    Close iHandle
    Exit Sub
    
ErrHandler:
    MsgBox "Erreur lors de l'import : " & Error$, 16, "Erreur"
End Sub

Sub MettreEnForme(oSheet As Object)
    ' Applique le formatage (en-têtes gras, colonnes ajustées, etc.)
    
    Dim oEntetes As Object
    Dim i As Integer
    
    ' Sélectionner la ligne d'en-têtes
    oEntetes = oSheet.getRows().getByIndex(0)
    
    ' En gras
    oEntetes.CharWeight = com.sun.star.awt.FontWeight.BOLD
    
    ' Couleur de fond grise
    oEntetes.BackColor = RGB(200, 200, 200)
    
    ' Ajuster les colonnes
    For i = 0 To 7
        oSheet.getColumns().getByIndex(i).OptimalWidth = True
    Next i
    
    ' Alterner les couleurs des lignes
    Dim oCell As Object
    Dim iLignes As Integer
    Dim iLigne As Integer
    
    iLignes = oSheet.queryContentCells(3).getRangeAddress().EndRow
    
    For iLigne = 1 To iLignes
        If (iLigne Mod 2) = 0 Then
            oSheet.getRows().getByIndex(iLigne).BackColor = RGB(240, 240, 240)
        End If
    Next iLigne
End Sub

Sub ColorierAlertes(oSheet As Object)
    ' Colorie en rouge les soldes de congés faibles et en orange les habilitations expirées
    
    Dim oCell As Object
    Dim iLignes As Integer
    Dim iLigne As Integer
    Dim iSolde As Integer
    Dim sDate As String
    Dim dDateHab As Date
    Dim dLimite As Date
    
    ' Index des colonnes
    Const COL_SOLDE = 5          ' solde_congés
    Const COL_DATE_HAB = 7       ' date_dernière_habilitation
    
    ' Limite pour habilitations expirées (2 ans)
    dLimite = DateSerial(Year(Now()) - 2, Month(Now()), Day(Now()))
    
    iLignes = oSheet.queryContentCells(3).getRangeAddress().EndRow
    
    ' Parcourir les lignes de données
    For iLigne = 1 To iLignes
        ' Vérifier le solde de congés
        oCell = oSheet.getCellByPosition(COL_SOLDE, iLigne)
        iSolde = Val(oCell.getString())
        
        If iSolde < 5 Then
            oCell.BackColor = RGB(255, 200, 200)  ' Rose/Rouge clair
        End If
        
        ' Vérifier la date d'habilitation
        oCell = oSheet.getCellByPosition(COL_DATE_HAB, iLigne)
        sDate = oCell.getString()
        
        On Error Resume Next
        dDateHab = DateValue(sDate)
        If dDateHab < dLimite Then
            oSheet.getCellByPosition(COL_DATE_HAB, iLigne).BackColor = RGB(255, 200, 100)  ' Orange
        End If
        On Error GoTo 0
    Next iLigne
End Sub

Sub ExporterPDF()
    ' Exporte la feuille courante en PDF
    
    Dim oDoc As Object
    Dim aFilterData(0) As New com.sun.star.beans.PropertyValue
    Dim sNomFichier As String
    
    oDoc = ThisComponent
    
    ' Nom du fichier
    sNomFichier = "rapport_agents_" & Format(Now(), "dd_mm_yyyy") & ".pdf"
    
    ' Paramètres d'export
    aFilterData(0).Name = "SelectPdfVersion"
    aFilterData(0).Value = 1
    
    ' Exporter
    oDoc.storeToURL("file:///" & sNomFichier, Array(aFilterData(0)))
    
    MsgBox "PDF exporté : " & sNomFichier, 64, "Succès"
End Sub
