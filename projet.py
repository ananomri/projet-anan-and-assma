from PyQt5.uic import *
from PyQt5.QtWidgets import *
from pickle import dump, load
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
    elif test(CIN):
        QMessageBox.critical(w,"Erreur","Identifiant existe deja!")
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
        x = open("personne.dat","ab")
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
    f = open("personne.dat", "rb")
    ligne = 0
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
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
            eof= True
    f.close()
def affpersonnenumtel():
    f = open("personne.dat", "rb")
    ligne = 0
    x=w.cin.text()
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(e["tel"]==x):
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
            eof= True
    f.close()
#********************SUPPRIME PERSONNE*****************************
def test(x):
    f = open("personne.dat", "rb")
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(e['CIN']==x):
                return True
        except:
            eof= True
    return False
    f.close()
def test2(x):
    f = open("personne.dat", "rb")
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(e['tel']==x):
                return True
        except:
            eof= True
    return False
    f.close()
def supprimer_pers():
    CIN= wsp.cin.text()
    if CIN=="":
     QMessageBox.critical(wsp,"Erreur","Veuillez saisir votre CIN")
    elif not test(CIN):
             QMessageBox.critical(wsp,"Erreur","Veuillez saisir une CIN qui existe deja!!")
    else:
     f = open("personne.dat", "rb")
     f2 = open("personne2.dat", "wb")
     eof= False
     eof2= False
     while not(eof):
        try:
            e = loader.chargement(f)
            if(e['CIN']!=CIN):
                dump(e, f2)
        except:
            eof= True
     f.close()
     f2.close()
     f = open("personne.dat", "wb")
     f2 = open("personne2.dat", "rb")
     while not(eof2):
        try:
            e = loader.chargement(f2)
            dump(e, f)
        except:
            eof2= True
     f.close()
     f2.close()
     QMessageBox.information(wsp,"suppression","personne supprimee")
def testmeme(x,y):
    if len(x)!=len(y):
        return False
    else:
        for i in range(len(x)):
            if not(x[i]==y[i]):
                return False
    return True
def testnatio(x):
    f = open("personne.dat", "rb")
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(testmeme(e['nationalite'],x)):
                return True
        except:
            eof= True
    return False
    f.close()
def supprimerp2():
    natio= wsp2.supp2.text()
    if natio=="":
     QMessageBox.critical(wsp2,"Erreur","Veuillez saisir votre nationalite")
    elif not testnatio(natio):
             QMessageBox.critical(wsp2,"Erreur","Veuillez saisir une nationalite qui existe deja!!")
    else:
     f = open("personne.dat", "rb")
     f2 = open("personne2.dat", "wb")
     eof= False
     eof2= False
     while not(eof):
        try:
            e = loader.chargement(f)
            if not(testmeme(e['nationalite'],natio)):
                dump(e, f2)
        except:
            eof= True
     f.close()
     f2.close()
     f = open("personne.dat", "wb")
     f2 = open("personne2.dat", "rb")
     while not(eof2):
        try:
            e = loader.chargement(f2)
            dump(e, f)
        except:
            eof2= True
     f.close()
     f2.close()
     QMessageBox.information(wsp2,"suppression","les personne qui ont cette nationalite sont supprimees")
def supprimer3():
    tel= wsp3.tel.text()
    if tel=="":
     QMessageBox.critical(wsp3,"Erreur","Veuillez saisir le numero de telephone")
    elif not test2(tel):
             QMessageBox.critical(wsp3,"Erreur","Veuillez saisir un numero de telephone qui existe deja!!")
    else:
     f = open("personne.dat", "rb")
     f2 = open("personne2.dat", "wb")
     eof= False
     eof2= False
     while not(eof):
        try:
            e = loader.chargement(f)
            if(e['tel']!=tel):
                dump(e, f2)
        except:
            eof= True
     f.close()
     f2.close()
     f = open("personne.dat", "wb")
     f2 = open("personne2.dat", "rb")
     while not(eof2):
        try:
            e = loader.chargement(f2)
            dump(e, f)
        except:
            eof2= True
     f.close()
     f2.close()
     QMessageBox.information(wsp3,"suppression","les personnes qui ont ce numero de telephone sont supprimees")

#---------------------modifier personne----------------------------
def modifierptel():
    cin=weg.cin.text()
    tel=weg.tel.text()
    if cin=="" or tel=="":
     QMessageBox.critical(wsp,"Erreur","Veuillez saisir tout les informations")

#___________________________maladie____________________________
def ajouterm():
    CIN= wm.cin.text()
    nom_maladie= wm.nommldie.text()
    nb_annee=wm.annee.text()
    if CIN=="" or nom_maladie=="" or nb_annee=="":
        QMessageBox.critical(wm,"Erreur","Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN)!=8 :
        QMessageBox.critical(wm,"Erreur","Identifiant invalide")
    elif not nb_annee.isdecimal() or len(nb_annee)!=2:
        QMessageBox.critical(wm,"Erreur"," nbre annee invalide")
    else :
        f = open("maladie.dat","ab")
        m=dict()
        m['CIN'] = CIN
        m['nom_maladie'] = nom_maladie
        m['nb_annee'] = nb_annee
        dump(m, f)
        f.close()
        QMessageBox.information(wm,"Ajout","personne ajouté")
def affmal():
    f = open("maladie.dat", "rb")
    ligne = 0
    eof= False
    while not(eof):
        try:
            m = loader.chargement(f)
            waffm.tab.insertRow(ligne)
            waffm.tab.setItem(ligne, 0, QTableWidgetItem(m["CIN"]))
            waffm.tab.setItem(ligne, 1, QTableWidgetItem(m["nom_maladie"]))
            waffm.tab.setItem(ligne, 2, QTableWidgetItem(m["nb_annee"]))
            ligne += 1
        except:
            eof= True
    f.close() 
    
#app
app = QApplication([])
window = loader.chargementUi ("projetqtds.ui")
w = loader.chargementUi("ajouter.ui")
waffp=loader.chargementUi("afficherpersonne.ui")
wm=loader.chargementUi("ajoutermaladie.ui")
waffm=loader.chargementUi("affichermaladie.ui")
wsp=loader.chargementUi("suppressionp1.ui")
wsp2=loader.chargementUi("suppressionp2.ui")
wsp3=loader.chargementUi("suppressionp3.ui")
weg=loader.chargementUi("modifiertelpersonne.ui")
def modiftel():
    weg.show
    weg.modif.clicked.connect(modifierptel)
def ajoutp():
    w.show()
    w.Ajouter.clicked.connect(ajouter)
def afficherp():
    waffp.show()
    waffp.affper.clicked.connect(affpersonne)
def ajoutm():
    wm.show()
    wm.Ajouter.clicked.connect(ajouterm)
def afficherm():
    waffm.show()
    waffm.affm.clicked.connect(affmal)
def suppressionp1():
    wsp.show()
    wsp.supprimer1.clicked.connect(supprimer_pers)
def suppressionp2():
    wsp2.show()
    wsp2.suppression.clicked.connect(supprimerp2)
def suppressionp3():
    wsp3.show()
    wsp3.supp3.clicked.connect(supprimerp3)
window.actionAjouter.triggered.connect(ajoutp)
window.actiondicper.triggered.connect(afficherp)
window.actionajoutm_2.triggered.connect(ajoutm)
window.actiontelephone.triggered.connect(modiftel)
window.actioncontenu_du_dictionnaire_maladies_2.triggered.connect(afficherm)
window.actionsupp1.triggered.connect(suppressionp1)
window.actionsupp2.triggered.connect(suppressionp2)
window.actionsupp3.triggered.connect(suppressionp3)
window.show()
app.exec_()