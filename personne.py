from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load
from datetime import datetime
date_actuelle = datetime.now()
anneeac = date_actuelle.year
moisac = date_actuelle.month
jourac = date_actuelle.day
def ajouter():
    CIN= w.cin.text()
    nom=w.nom.text()
    prenom=w.pr.text()
    age=w.age.text()
    adresse=w.ad.text()
    nationalite=w.nt.currentText()
    tel = w.tel.text()
    jour=w.jour.text()
    mois=w.mois.text()
    annee=w.annee.text()
    if (CIN == "" or tel == "" or nom=="" or prenom=="" or age=="" or nationalite=="" or tel=="" or jour=="" or annee=="" or mois==""):
        QMessageBox.critical(w,"Erreur","Veuillez saisir toutes les informations")
    elif not CIN.isdecimal()or len(CIN)!=7 :
        QMessageBox.critical(w,"Erreur","Identifiant invalide")
    elif not age.isdecimal() or len(age)>3:
        QMessageBox.critical(w,"Erreur","Age invalide")
    elif not tel.isdecimal() or len(tel) != 8 :
        QMessageBox.critical(w,"Erreur","N° de Téléphone invalide")
    elif not(w.nt.currentText()in ["TUNISIENNE","ALGERIENNE","MAROCAINE"]):
        QMessageBox.critical(w,"Erreur","Vérifier votre nationnalite")
    elif not jour.isdecimal() or not 1<=len(jour) <= 2 or int(jour)>31 :
        QMessageBox.critical(w,"Erreur","Vérifier le jour")
    elif not mois.isdecimal() or  not 1<=len(mois) <= 2 or int(mois)>12:
        QMessageBox.critical(w,"Erreur","Vérifier le mois")
    elif not annee.isdecimal() or len(annee) != 4 or int(annee)>anneeac:
        QMessageBox.critical(w,"Erreur","Vérifier l'annee")   
    elif not(w.btr1.isChecked or w.btr2.isChecked ):
        QMessageBox.critical(w,"Erreur","DECEDE OU NON?")
    else :
        x = open("personne2.dat","ab")
        decede = "0"
        if w.btr1.isChecked():
            decede = "1"
        e=dict()
        e['CIN'] = CIN
        e['tel'] = tel
        e['decede'] = decede
        e['nationalite'] = nationalite
        e['age'] = age
        e['adresse'] = adresse
        e['jour'] =jour
        e['mois'] = mois
        e['annee'] = annee
        e['nom'] = nom
        e['prenom'] = prenom  
        dump(e, x)
        x.close()
        QMessageBox.information(w,"Ajout","personne ajouté")   
def affpersonne():
    x = open("personne2.dat", "rb")
    ligne = 0
    eox= False
    while not(eox):
        try:
            e = load(x)
            waff.tabl.insertRow(ligne)
            waff.tabl.setItem(ligne, 0, QTableWidgetItem(e["CIN"]))
            waff.tabl.setItem(ligne, 1, QTableWidgetItem(e["nom"]))
            waff.tabl.setItem(ligne, 2, QTableWidgetItem(e["prenom"]))
            waff.tabl.setItem(ligne, 3, QTableWidgetItem(e["tel"]))            
            waff.tabl.setItem(ligne, 4, QTableWidgetItem(e["nationalite"]))
            waff.tabl.setItem(ligne, 5, QTableWidgetItem(e["age"]))
            waff.tabl.setItem(ligne, 6, QTableWidgetItem(e["jour"]))
            waff.tabl.setItem(ligne, 7, QTableWidgetItem(e["mois"]))
            waff.tabl.setItem(ligne, 8, QTableWidgetItem(e["annee"]))
            waff.tabl.setItem(ligne, 9, QTableWidgetItem(e["decede"]))
            ligne += 1
        except:
            eox= True
    x.close()   
app=QApplication([])
w=loadUi("ajouter.ui")
waff=loadUi("afficherpersonne.ui")
w.show()
waff.show()
waff.affper.clicked.connect(affpersonne)
w.Ajouter.clicked.connect(ajouter)
#w.hide()
#waff.hide()
#win.actionajout.triggered.connect(ouvrirf)
app.exec_()
 