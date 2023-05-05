def afficher_pourcentage():
    nom_maladie = ws.nommldie.text()
    if (nom_maladie == ""):
        QMessageBox.critical(ws, "Erreur", "Veuillez saisir toutes les informations")
    maladies = loader.chargement("maladies.csv")
    nb_personnes = len(maladies)
    nb_personnes_avec_maladie = 0
    for cin in maladies:
        maladies_cin = maladies[cin]
        for maladie in maladies_cin:
            if maladie["nom"] == nom_maladie:
                nb_personnes_avec_maladie += 1
                break
    pourcentage = (nb_personnes_avec_maladie / nb_personnes) * 100
    print(f"{pourcentage}% des personnes ont la maladie {nom_maladie}")
    QMessageBox.critical(ws, f"{pourcentage}% des personnes ont la maladie {nom_maladie}")
    
def afficher_quarantaine():
    date_en_cours=date.today()
    f = "personne.csv"
    d = loader.chargement(f)
    waffq.tabl.setRowCount(0)
    for ligne, e in enumerate(d.items()):
        if e[1].get("date_infection") is not None:
            date_infection = datetime.strptime(e[1]["date_infection"], '%d/%m/%Y')
            jours_quarantaine = (date_en_cours - date_infection).days
            if jours_quarantaine <= 14:
                waffq.tabl.insertRow(ligne)
                waffq.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
                waffq.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
                waffq.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
                waffq.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))            
                waffq.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
                waffq.tabl.setItem(ligne, 5, QTableWidgetItem(str(date_infection.date())))
                waffq.tabl.setItem(ligne, 6, QTableWidgetItem(str(jours_quarantaine)))
                
def afficher_deces():
    f = "personne.csv"
    d = loader.chargement(f)
    decedes = []
    for e in d.values():
        if e.get("decede", "0") == "1":
            decedes.append(e)
    nb_deces = len(decedes)
    pourcentage_deces = round(nb_deces / len(d) * 100, 2)
    table = QTableWidget()
    table.setColumnCount(7)
    table.setHorizontalHeaderLabels(["CIN", "Nom", "Prénom", "Age", "Nationalité", "Téléphone", "Adresse"])
    table.setRowCount(nb_deces)
    for ligne, e in enumerate(decedes):
        table.setItem(ligne, 0, QTableWidgetItem(str(e.get("CIN", ""))))
        table.setItem(ligne, 1, QTableWidgetItem(e.get("nom", "")))
        table.setItem(ligne, 2, QTableWidgetItem(e.get("prenom", "")))
        table.setItem(ligne, 3, QTableWidgetItem(str(e.get("age", ""))))
        table.setItem(ligne, 4, QTableWidgetItem(e.get("nationalite", "")))
        table.setItem(ligne, 5, QTableWidgetItem(str(e.get("tel", ""))))
        table.setItem(ligne, 6, QTableWidgetItem(e.get("adresse", "")))
    layout.addWidget(table)
    
    label = QLabel(f"Nombre de décès : {nb_deces} ({pourcentage_deces}%)")
    layout.addWidget(label)
    wdeces.exec_()
    
def afficher_personnes_a_risque():
    f = "personne.csv"
    d = loader.chargement(f)
    maladies = loader.chargement("maladies.csv")
    personnes_a_risque = []
    for cin, e in d.items():
        risque = 0
        age = int(e['age'])
        if age > 70:
            risque += 20
        elif age >= 50:
            risque += 10
        for cin2, x in maladies.items():
            if cin==cin2:
                for x2 in x:
                    if x2['nom']=='diabete':
                        risque += 15
                    if x2['nom']=='hypertension':
                        risque += 20
                    if x2['nom']=='asthme':
                        risque += 20
        if risque > 0:
            personnes_a_risque.append((e['nom'], e['prenom'], risque))
    
    personnes_a_risque.sort(key=lambda x: x[2], reverse=True)
    waffp_risque = QDialog()
    waffp_risque.setWindowTitle("Personnes à risque")
    layout = QVBoxLayout()
    waffp_risque.setLayout(layout)
    
    table = QTableWidget()
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["Nom", "Prénom", "Risque"])
    table.setRowCount(len(personnes_a_risque))
    
    for i, personne in enumerate(personnes_a_risque):
        nom, prenom, risque = personne
        if len(nom) > 0:
            table.setItem(i, 0, QTableWidgetItem(nom))
        if len(prenom) > 0:
            table.setItem(i, 1, QTableWidgetItem(prenom))
        table.setItem(i, 2, QTableWidgetItem(str(risque) + "%"))
    
    layout.addWidget(table)
    
    waffp_risque.exec_()
