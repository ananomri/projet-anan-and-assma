from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load
def ajouter():
    CIN= w.cin.text()
    nom_maladie= w.nommldie.text()
    nb_annee=w.annee.text()
    if CIN=="" or nom_maladie=="" or nb_annee=="":
        QMessageBox.critical(w,"Erreur","Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN)!=8 :
        QMessageBox.critical(w,"Erreur","Identifiant invalide")
    elif not nb_annee.isdecimal() or len(nb_annee)!=2:
        QMessageBox.critical(w,"Erreur"," nbre annee invalide")
    else :
        f = open("maladie.dat","ab")
        m=dict()
        #m['code']=codecalll()
        m['CIN'] = CIN
        m['nom_maladie'] = nom_maladie
        m['nb_annee'] = nb_annee
        dump(m, f)
        f.close()
        QMessageBox.information(w,"Ajout","personne ajouté")


def affmal():
    f = open("maladie.dat", "rb")
    ligne = 0
    eof= False
    while not(eof):
        try:
            m = load(f)
            wf.tab.insertRow(ligne)
            wf.tab.setItem(ligne, 0, QTableWidgetItem(m["CIN"]))
            wf.tab.setItem(ligne, 1, QTableWidgetItem(m["nom_maladie"]))
            wf.tab.setItem(ligne, 2, QTableWidgetItem(m["nb_annee"]))
            ligne += 1
        except:
            eof= True
    f.close() 
app=QApplication([])
w=loadUi("ajoutermaladie.ui")
wf=loadUi("affichermaladie.ui")
w.show()
wf.show()
w.Ajouter.clicked.connect(ajouter)
wf.afficherm.clicked.connect(affmal)
app.exec_()