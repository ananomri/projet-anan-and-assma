from PyQt5.uic import *
from PyQt5.QtWidgets import *
import loader
from datetime import datetime
import resources_rc
date_actuelle = datetime.now()
anneeac = date_actuelle.year
moisac = date_actuelle.month
jourac = date_actuelle.day
f = "personne.csv"
e = loader.chargement(f)

def ajouter():
    global e
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
    elif not(w.nt.currentText()in ["TUNISIENNE","ALGERIENNE","MAROCAINE","Ukrainienne","Vanuatuane","Venezuelienne","Vietnamienne","Yemenite","Zambienne","Zimbabweenne"]):
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
        x = "personne.csv"
        decede = "0"
        if w.btr1.isChecked():
            decede = "1"
        e2 = dict()
            
        e2['tel'] = tel
        e2['decede'] = decede
        e2['nationalite'] = nationalite
        e2['age'] = age
        e2['adresse'] = adresse
        e2['jour'] =jour
        e2['mois'] = mois
        e2['annee'] = annee
        e2['nom'] = nom
        e2['prenom'] = prenom
        e[CIN] = e2
        loader.enregistrement(e, x)
        QMessageBox.information(w,"Ajout","personne ajouté")
    w.close()
def affpersonne():
    f = "personne.csv"
    d = loader.chargement(f)
    waffp.tabl.setRowCount(0)
    for ligne, e in enumerate(d.items()):
        waffp.tabl.insertRow(ligne)
        waffp.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
        waffp.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
        waffp.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
        waffp.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))            
        waffp.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
        waffp.tabl.setItem(ligne, 5, QTableWidgetItem(e[1]["age"]))
        waffp.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["jour"]))
        waffp.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["mois"]))
        waffp.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["annee"]))
        waffp.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))
    
def affpersonnenumtel():
    #f = "personne.csv"
    #ligne = 0
    x=w.cin.text()
    """eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(e["tel"]==x):
             waffp.tabl.insertRow(ligne)
             waffp.tabl.setItem(ligne, 0, QTableWidgetItem(e["CIN"]))
             waffp.tabl.setItem(ligne, 1, QTableWidgetItem(e["nom"]))
             waffp.tabl.setItem(ligne, 2, QTableWidgetItem(e["prenom"]))
             waffp.tabl.setItem(ligne, 3, QTableWidgetItem(e["tel"]))            
             waffp.tabl.setItem(ligne, 4, QTableWidgetItem(e["nationalite"]))
             waffp.tabl.setItem(ligne, 5, QTableWidgetItem(e["age"]))
             waffp.tabl.setItem(ligne, 6, QTableWidgetItem(e["jour"]))
             waffp.tabl.setItem(ligne, 7, QTableWidgetItem(e["mois"]))
             waffp.tabl.setItem(ligne, 8, QTableWidgetItem(e["annee"]))
             waffp.tabl.setItem(ligne, 9, QTableWidgetItem(e["decede"]))
             ligne += 1
        except:
            eof= True"""
    
    f = "personne.csv"
    d = loader.chargement(f)
    ligne = 0
    eof= False
    #{"123":{"test","test"}, }
    for ligne, e in enumerate(d):
        if(e["tel"]==x):
            waffp.tabl.insertRow(ligne)
            waffp.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
            waffp.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
            waffp.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
            waffp.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))            
            waffp.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
            waffp.tabl.setItem(ligne, 5, QTableWidgetItem(e[1]["age"]))
            waffp.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["jour"]))
            waffp.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["mois"]))
            waffp.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["annee"]))
            waffp.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))
    
#********************SUPPRIME PERSONNE*****************************
def test(x):
    f = "personne.csv"
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(e['CIN']==x):
                return True
        except:
            eof= True
    return False
    
def test2(x):
    f = "personne.csv"
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(e['tel']==x):
                return True
        except:
            eof= True
    return False
    
def supprimer_pers():
    CIN= wsp.cin.text()
    if CIN=="":
     QMessageBox.critical(wsp,"Erreur","Veuillez saisir votre CIN")
    elif not test(CIN):
             QMessageBox.critical(wsp,"Erreur","Veuillez saisir une CIN qui existe deja!!")
    else:
     f = "personne.csv"
     f2 = "personne2.csv"
     eof= False
     eof2= False
     while not(eof):
        try:
            e = loader.chargement(f)
            if(e['CIN']!=CIN):
                loader.enregistrement(e, f2)
        except:
            eof= True
     
     
     f = "personne.csv"
     f2 = "personne2.csv"
     while not(eof2):
        try:
            e = loader.chargement(f2)
            loader.enregistrement(e, f)
        except:
            eof2= True
     
     
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
    f = "personne.csv"
    eof= False
    while not(eof):
        try:
            e = loader.chargement(f)
            if(testmeme(e['nationalite'],x)):
                return True
        except:
            eof= True
    return False
    
def supprimerp2():
    natio= wsp2.supp2.text()
    if natio=="":
     QMessageBox.critical(wsp2,"Erreur","Veuillez saisir votre nationalite")
    elif not testnatio(natio):
             QMessageBox.critical(wsp2,"Erreur","Veuillez saisir une nationalite qui existe deja!!")
    else:
     f = "personne.csv"
     f2 = "personne2.csv"
     eof= False
     eof2= False
     while not(eof):
        try:
            e = loader.chargement(f)
            if not(testmeme(e['nationalite'],natio)):
                loader.enregistrement(e, f2)
        except:
            eof= True
     
     
     f = "personne.csv"
     f2 = "personne2.csv"
     while not(eof2):
        try:
            e = loader.chargement(f2)
            loader.enregistrement(e, f)
        except:
            eof2= True
     
     
     QMessageBox.information(wsp2,"suppression","les personne qui ont cette nationalite sont supprimees")
def supprimer3():
    tel= wsp3.tel.text()
    if tel=="":
     QMessageBox.critical(wsp3,"Erreur","Veuillez saisir le numero de telephone")
    elif not test2(tel):
             QMessageBox.critical(wsp3,"Erreur","Veuillez saisir un numero de telephone qui existe deja!!")
    else:
     f = "personne.csv"
     f2 = "personne2.csv"
     eof= False
     eof2= False
     while not(eof):
        try:
            e = loader.chargement(f)
            if(e['tel']!=tel):
                loader.enregistrement(e, f2)
        except:
            eof= True
     
     
     f = "personne.csv"
     f2 = "personne2.csv"
     while not(eof2):
        try:
            e = loader.chargement(f2)
            loader.enregistrement(e, f)
        except:
            eof2= True
     
     
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
        f = "maladie.csv"
        m=dict()
        m['CIN'] = CIN
        m['nom_maladie'] = nom_maladie
        m['nb_annee'] = nb_annee
        loader.enregistrement(m, f)
        
        QMessageBox.information(wm,"Ajout","personne ajouté")
def affmal():
    f = "maladie.csv"
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
     
    
#app
app = QApplication([])
window = loadUi("projetqtds.ui")
w = loadUi("ajouter.ui")
waffp=loadUi("afficherpersonne.ui")
wm=loadUi("ajoutermaladie.ui")
waffm=loadUi("affichermaladie.ui")
wsp=loadUi("suppressionp1.ui")
wsp2=loadUi("suppressionp2.ui")
wsp3=loadUi("suppressionp3.ui")
weg=loadUi("modifiertelpersonne.ui")
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
