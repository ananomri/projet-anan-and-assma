from PyQt5.uic import *
from PyQt5.QtWidgets import *
import loader
from datetime import datetime, date
import resources_rc
date_actuelle = datetime.now()
anneeac = date_actuelle.year
moisac = date_actuelle.month
jourac = date_actuelle.day
f = "personne.csv"
e = loader.chargement(f)
m = "maladies.csv"
maladies = loader.chargementMaladies(m)
countries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
             'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
############ajouter############


def ajouter():
    global e
    CIN = w.cin.text()
    nom = w.nom.text()
    prenom = w.pr.text()
    age = w.age.text()
    adresse = w.ad.text()
    nationalite = w.nt.currentText()
    tel = w.tel.text()
    jour = w.jour.text()
    mois = w.mois.text()
    annee = w.annee.text()
    if (CIN == "" or tel == "" or nom == "" or prenom == "" or age == "" or nationalite == "" or tel == "" or jour == "" or annee == "" or mois == ""):
        QMessageBox.critical(w, "Erreur", "Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(w, "Erreur", "Identifiant invalide")
    elif test(CIN):
        QMessageBox.critical(w, "Erreur", "Identifiant existe deja!")
    elif not age.isdecimal() or len(age) > 3:
        QMessageBox.critical(w, "Erreur", "Age invalide")
    elif not tel.isdecimal() or len(tel) != 8:
        QMessageBox.critical(w, "Erreur", "N° de Téléphone invalide")
    elif not jour.isdecimal() or not 1 <= len(jour) <= 2 or int(jour) > 31:
        QMessageBox.critical(w, "Erreur", "Vérifier le jour")
    elif not mois.isdecimal() or not 1 <= len(mois) <= 2 or int(mois) > 12:
        QMessageBox.critical(w, "Erreur", "Vérifier le mois")
    elif not annee.isdecimal() or len(annee) != 4 or int(annee) > anneeac:
        QMessageBox.critical(w, "Erreur", "Vérifier l'annee")
    elif not(w.btr1.isChecked or w.btr2.isChecked):
        QMessageBox.critical(w, "Erreur", "DECEDE OU NON?")
    else:
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
        e2['jour'] = jour
        e2['mois'] = mois
        e2['annee'] = annee
        e2['nom'] = nom
        e2['prenom'] = prenom
        e[CIN] = e2
        loader.enregistrement(e, x)
        QMessageBox.information(w, "Ajout", "personne ajouté")
        w.close()

###############affpersonne############


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
        waffp.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["adresse"]))
        waffp.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["jour"]))
        waffp.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["mois"]))
        waffp.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["annee"]))
        waffp.tabl.setItem(ligne, 10, QTableWidgetItem(e[1]["decede"]))
##############affpersonne_tel*****************###########


def test(x):
    f = "personne.csv"
    e = loader.chargement(f)
    return x in e


"""def affpersonne_tel():
    f = "personne.csv"
    d = loader.chargement(f)
    tel = wtel.tel.text()
    waffp.tabl.setRowCount(0)
    for ligne, e in enumerate(d.items()):
        if e[1]["tel"] == tel:
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
            waffp.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))"""
############supprimer_nationalite***********##########


def supprimerp2():
    global e
    nationalite = wsp2.supp2.text()
    if (nationalite == ""):
        QMessageBox.critical(wsp2, "Erreur", "Veuillez sélectionner une nationalité valide")
    else:
        x = "personne.csv"
        personnes_a_supprimer = []
        for cin, personne in e.items():
            if personne["nationalite"] == nationalite:
                personnes_a_supprimer.append(cin)
        if len(personnes_a_supprimer) == 0:
            QMessageBox.information(wsp2, "Suppression", "Aucune personne à supprimer pour cette nationalité")
        else:
            for cin in personnes_a_supprimer:
                del e[cin]
            loader.enregistrement(e, x)
            QMessageBox.information(wsp2, "Suppression", "Les personnes de nationalité " +
                                    nationalite + " ont été supprimées")
# supprimer_tel########***********


def supprimerp3():
    global e
    tel = wsp3.tel.text()
    if tel == "":
        QMessageBox.critical(wsp3, "Erreur", "Veuillez saisir un numéro de téléphone")
    elif not tel.isdecimal() or len(tel) != 8:
        QMessageBox.critical(wsp3, "Erreur", "Numéro de téléphone invalide")
    else:
        x = "personne.csv"
        e2 = {c: v for c, v in e.items() if v['tel'] != tel}
        if len(e2.values()) == len(e.values()):
            QMessageBox.critical(wsp3, "Erreur", "Personne avec ce numéro de téléphone introuvable")
        else:
            e = e2
            loader.enregistrement(e, x)
            QMessageBox.information(wsp3, "Suppression", "Personne supprimée")
# supprimer_tel_indicatif########***********


def supprimerp4():
    global e
    tel = wsp3.tel.text()
    if tel == "":
        QMessageBox.critical(wsp3, "Erreur", "Veuillez saisir un indicatid de numéro de téléphone")
    elif not tel.isdecimal() or len(tel) != 2:
        QMessageBox.critical(wsp3, "Erreur", "Indicatif invalide")
    else:
        x = "personne.csv"
        e2 = {c: v for c, v in e.items() if v['tel'][:2] != tel}
        if len(e2.values()) == len(e.values()):
            QMessageBox.critical(wsp3, "Erreur", "Personne avec ce numéro de téléphone introuvable")
        else:
            e = e2
            loader.enregistrement(e, x)
            QMessageBox.information(wsp3, "Suppression", "Personnes ave... supprimée")
# supprimer_pers############*********


def supprimer_pers():
    global e
    CIN = wsp.cin.text()
    if CIN == "":
        QMessageBox.critical(wsp, "Erreur", "Veuillez saisir un identifiant")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(wsp, "Erreur", "Identifiant invalide")
    elif not test(CIN):
        QMessageBox.critical(wsp, "Erreur", "Identifiant introuvable")
    else:
        x = "personne.csv"
        del e[CIN]
        loader.enregistrement(e, x)
        QMessageBox.information(wsp, "Suppression", "personne supprimée")
# modifier_tel#########*********


def modifier_tel():
    global e
    CIN = w2.cin.text()
    tel = w2.tel.text()
    x = "personne.csv"
    if CIN == "" or tel == "":
        QMessageBox.critical(w2, "Erreur", "Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(w2, "Erreur", "Identifiant invalide")
    elif not test(CIN):
        QMessageBox.critical(w2, "Erreur", "Identifiant introuvable")
    elif not tel.isdecimal() or len(tel) != 8:
        QMessageBox.critical(w2, "Erreur", "Numéro de téléphone invalide")
    else:
        e[CIN]['tel'] = tel
        loader.enregistrement(e, x)
        QMessageBox.information(w2, "Modification", "Numéro de téléphone modifié avec succès")
# modifier_adresse##########******


def modifier_adresse():
    global e
    CIN = w7.cin.text()
    adresse = w7.ad.text()
    if CIN == "" or adresse == "":
        QMessageBox.critical(w7, "Erreur", "Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(w7, "Erreur", "Identifiant invalide")
    elif not test(CIN):
        QMessageBox.critical(w7, "Erreur", "Identifiant introuvable")
    else:
        e[CIN]['adresse'] = adresse
        x = "personne.csv"
        loader.enregistrement(e, x)
        QMessageBox.information(w7, "Modification", "Adresse modifiée avec succès")
        w.close()
# affpersonne_tel########*****


def affpersonne_tel():
    f = "personne.csv"
    d = loader.chargement(f)
    tel = w17.tel.text()
    w17.tabl.setRowCount(0)
    count = 0
    for ligne, e in enumerate(d.items()):
        if e[1]["tel"] == tel:
            w17.tabl.insertRow(ligne)
            w17.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
            w17.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
            w17.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
            w17.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))
            w17.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
            w17.tabl.setItem(ligne, 5, QTableWidgetItem(e[1]["age"]))
            w17.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["jour"]))
            w17.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["mois"]))
            w17.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["annee"]))
            w17.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))
            count += 1
    if(count == 0):
        QMessageBox.information(ws, "Recherche par tel", "Telephone introuvable!")
# affpersonne_nationalite###########*****


def fillComboBox(comboBox, elems):
    comboBox.clear()
    for i in elems:
        comboBox.addItem(i)


def affpersonne_nationalite():
    f = "personne.csv"
    d = loader.chargement(f)
    nationalite = wnat.nat.currentText()
    if nationalite == "":
        QMessageBox.critical(wnat, "Erreur", "Veuillez saisir une nationalite")
    elif (nationalite not in countries):
        QMessageBox.critical(wnat, "Erreur", "Nationalite n'existe pas")
    else:
        wnat.tabl.setRowCount(0)
        pers = {c: v for c, v in d.items() if(v["nationalite"] == nationalite)}
        if(len(pers.values()) == 0):
            QMessageBox.information(w7, "Info", "Aucun pers de cette nat!")
            return
        wnat.tabl.setRowCount(len(pers.values()))
        for ligne, e in enumerate(pers.items()):
            # if e[1]["nationalite"] == nationalite:
            wnat.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
            wnat.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
            wnat.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
            wnat.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))
            wnat.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
            wnat.tabl.setItem(ligne, 5, QTableWidgetItem(e[1]["age"]))
            wnat.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["jour"]))
            wnat.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["mois"]))
            wnat.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["annee"]))
            wnat.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))
# affpersonne_decede#####********


def affpersonne_decede():
    f = "personne.csv"
    d = loader.chargement(f)
    w13.tabl.setRowCount(0)
    for ligne, e in enumerate(d.items()):
        if e[1]["decede"] == "1":
            w13.tabl.insertRow(ligne)
            w13.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
            w13.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
            w13.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
            w13.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))
            w13.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
            w13.tabl.setItem(ligne, 5, QTableWidgetItem(e[1]["age"]))
            w13.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["jour"]))
            w13.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["mois"]))
            w13.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["annee"]))
            w13.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))
            ligne += 1

#######affpersonne_non_decede#########


def affpersonne_non_decede():
    f = "personne.csv"
    d = loader.chargement(f)
    w16.tabl.setRowCount(0)
    ligne = 0
    for e in d.items():
        if e[1]["decede"] == "0":
            w16.tabl.insertRow(ligne)
            w16.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
            w16.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
            w16.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
            w16.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))
            w16.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
            w16.tabl.setItem(ligne, 5, QTableWidgetItem(e[1]["age"]))
            w16.tabl.setItem(ligne, 6, QTableWidgetItem(e[1]["jour"]))
            w16.tabl.setItem(ligne, 7, QTableWidgetItem(e[1]["mois"]))
            w16.tabl.setItem(ligne, 8, QTableWidgetItem(e[1]["annee"]))
            w16.tabl.setItem(ligne, 9, QTableWidgetItem(e[1]["decede"]))
            ligne += 1

##########supprimerm###########


def supprimerm():
    global maladies
    CIN = ws.cin.text()
    nom_maladie = ws.nommldie.text()
    if (CIN == "" or nom_maladie == ""):
        QMessageBox.critical(ws, "Erreur", "Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(ws, "Erreur", "Identifiant invalide")
    elif CIN not in maladies:
        QMessageBox.critical(ws, "Erreur", "Personne non trouvée")
    else:
        maladie = None
        for m in maladies[CIN]:
            if m['nom'] == nom_maladie:
                maladie = m
                break
        if maladie is not None:
            maladies[CIN].remove(maladie)
            loader.enregistrement(maladies, "maladies.csv")
            QMessageBox.information(ws, "Suppression", "Maladie supprimée")
            ws.close()
        else:
            QMessageBox.critical(ws, "Erreur", "Maladie non trouvée")
############modifier_nb_annees###########


def modifier_nb_annees():
    maladies = loader.chargementMaladies("maladies.csv")
    CIN = w11.cin.text()
    nb_annees = w11.nb.text()
    nom_maladie = w11.nom.text()
    if (CIN == "" or nom_maladie == "" or nb_annees == ""):
        QMessageBox.critical(w11, "Erreur", "Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(w11, "Erreur", "Identifiant invalide")
    elif CIN not in maladies:
        QMessageBox.critical(w11, "Erreur", "Personne non trouvée")
    if CIN in maladies:
        maladies_cin = maladies[CIN]
        maladie = [m for m in maladies_cin if m['nom'] == nom_maladie][0]
        if maladie is not None:
            maladie['nb_annees'] = nb_annees
            loader.enregistrement(maladies, "maladies.csv")
            QMessageBox.information(w11, "Modification", "Nombre d'années modifié")
        else:
            QMessageBox.critical(w11, "Erreur", "Maladie non trouvée")
    else:
        QMessageBox.critical(w11, "Erreur", "Personne non trouvée")
############afficherm###########


def afficherm():
    maladies = loader.chargementMaladies("maladies.csv")
    waffm.tab.setRowCount(0)
    ligne = 0
    for cin, maladies_cin in maladies.items():
        for maladie in maladies_cin:
            if(len(maladie.values())):
                waffm.tab.insertRow(ligne)
                waffm.tab.setItem(ligne, 0, QTableWidgetItem(cin))
                waffm.tab.setItem(ligne, 1, QTableWidgetItem(maladie["nom"]))
                waffm.tab.setItem(ligne, 2, QTableWidgetItem(maladie["nb_annees"]))
                ligne += 1
############afficher_par_nom_maladie##########


def afficher_par_nom_maladie():
    maladies = loader.chargementMaladies("maladies.csv")
    nom_maladie = w18.nom.text()
    if (nom_maladie == ""):
        QMessageBox.critical(w18, "Erreur", "Veuillez saisir toutes les informations")
    w18.tab.setRowCount(0)
    ligne = 0
    for cin, maladies_cin in maladies.items():
        for maladie in maladies_cin:
            if maladie["nom"] == nom_maladie:
                w18.tab.insertRow(ligne)
                w18.tab.setItem(ligne, 0, QTableWidgetItem(cin))
                w18.tab.setItem(ligne, 1, QTableWidgetItem(maladie["nom"]))
                w18.tab.setItem(ligne, 2, QTableWidgetItem(maladie["nb_annees"]))
                ligne += 1
#########afficher_par_personne#########


def afficher_par_personne():
    maladies = loader.chargementMaladies("maladies.csv")
    cin = wrm.nommldie.text()
    if (nom_maladie == ""):
        QMessageBox.critical(wrm, "Erreur", "Veuillez saisir toutes les informations")
    wrm.tab.setRowCount(0)
    ligne = 0
    for cin, maladies_cin in maladies.items():
        for maladie in maladies_cin:
            if maladie["nom"] == nom_maladie:
                wrm.tab.insertRow(ligne)
                wrm.tab.setItem(ligne, 0, QTableWidgetItem(cin))
                wrm.tab.setItem(ligne, 1, QTableWidgetItem(maladie["nom"]))
                wrm.tab.setItem(ligne, 2, QTableWidgetItem(maladie["nb_annees"]))
                ligne += 1
###########afficher_par_cin############


def afficher_par_cin():
    maladies = loader.chargementMaladies("maladies.csv")
    cin = wrm.cin.text()
    if (cin == ""):
        QMessageBox.critical(wrm, "Erreur", "Veuillez saisir toutes les informations")
    else:
        wrm.tab.setRowCount(0)
        ligne = 0
        if cin in maladies:
            maladies_cin = maladies[cin]
            for maladie in maladies_cin:
                wrm.tab.insertRow(ligne)
                wrm.tab.setItem(ligne, 0, QTableWidgetItem(cin))
                wrm.tab.setItem(ligne, 1, QTableWidgetItem(maladie["nom"]))
                wrm.tab.setItem(ligne, 2, QTableWidgetItem(maladie["nb_annees"]))
                ligne += 1
        else:
            QMessageBox.critical(ws, "Erreur", "Personne non trouvée ou aucune maladie associée")
##############afficher_pourcentage###


def afficher_pourcentage():
    nom_maladie = w19.nommldie.text()
    if (nom_maladie == ""):
        QMessageBox.critical(w19, "Erreur", "Veuillez saisir toutes les informations")
    else:
        maladies = loader.chargementMaladies("maladies.csv")
        nb_personnes = len(maladies)
        nb_personnes_avec_maladie = 0
        for cin in maladies:
            maladies_cin = maladies[cin]
            for maladie in maladies_cin:
                if maladie["nom"] == nom_maladie:
                    nb_personnes_avec_maladie += 1
                    break
        pourcentage = (nb_personnes_avec_maladie / nb_personnes) * 100
        #print(f"{pourcentage}% des personnes ont la maladie {nom_maladie}")
        QMessageBox.critical(w19, "Maladies", f"{pourcentage}% des personnes ont la maladie {nom_maladie}")
# _____ajoutermaladie____________________________


def ajouterm():
    global e
    global maladies
    CIN = wm.cin.text()
    nom_maladie = wm.nommldie.text()
    nb_annees = wm.annee.text()
    #print(CIN, nom_maladie, nb_annees)
    if (CIN == "" or nom_maladie == "" or nb_annees == ""):
        QMessageBox.critical(wm, "Erreur", "Veuillez saisir toutes les informations")
    elif not CIN.isdecimal() or len(CIN) != 7:
        QMessageBox.critical(wm, "Erreur", "Identifiant invalide")
    elif not nb_annees.isdecimal():
        QMessageBox.critical(wm, "Erreur", "Nombre d'années invalide")
    elif CIN not in e:
        QMessageBox.critical(wm, "Erreur", "Personne non trouvée")
    else:
        # print(maladies)
        if CIN in maladies:
            #print("dans maladie")
            # print(maladies[CIN])
            testL = list(filter(lambda x: x['nom'] == nom_maladie, maladies[CIN]))
            # print(testL)
            if(len(maladies.items()) > 0 and len(testL) > 0):
                QMessageBox.critical(wm, "Erreur", "Maladie existe!")
            else:
                maladies[CIN] = maladies[CIN] + [{'nom': nom_maladie, 'nb_annees': nb_annees}]
        else:
            #print("nouveau cin")
            maladies[CIN] = [{'nom': nom_maladie, 'nb_annees': nb_annees}]
        loader.enregistrement(maladies, "maladies.csv")
        QMessageBox.information(wm, "Ajout", "Maladie ajoutée")
        wm.close()


def afficher_quarantaine():
    date_en_cours = datetime.today().date()
    f = "personne.csv"
    d = loader.chargement(f)
    w12.tabl.setRowCount(0)
    ligne = 0
    for e in d.items():
        # if ("annee" in e[1] and "mois" in e[1] and "jour" in e[1]):
        date_infection = date(int(e[1]["annee"]), int(e[1]["mois"]), int(e[1]["jour"]))
        jours_quarantaine = (date_en_cours - date_infection).days

        if jours_quarantaine <= 14:
            w12.tabl.insertRow(ligne)
            w12.tabl.setItem(ligne, 0, QTableWidgetItem(e[0]))
            w12.tabl.setItem(ligne, 1, QTableWidgetItem(e[1]["nom"]))
            w12.tabl.setItem(ligne, 2, QTableWidgetItem(e[1]["prenom"]))
            w12.tabl.setItem(ligne, 3, QTableWidgetItem(e[1]["tel"]))
            w12.tabl.setItem(ligne, 4, QTableWidgetItem(e[1]["nationalite"]))
            w12.tabl.setItem(ligne, 5, QTableWidgetItem(str(date_infection)))
            w12.tabl.setItem(ligne, 6, QTableWidgetItem(str(jours_quarantaine)))
            ligne += 1


def afficher_personnes_a_risque():
    f = "personne.csv"
    d = loader.chargement(f)
    maladies = loader.chargementMaladies("maladies.csv")
    personnes_a_risque = []
    for cin, e in d.items():
        risque = 0
        age = int(e['age'])
        if age > 70:
            risque += 20
        elif age >= 50:
            risque += 10
        for cin2, x in maladies.items():
            if cin == cin2:
                for x2 in x:
                    if x2['nom'] == 'diabete':
                        risque += 15
                    if x2['nom'] == 'hypertension':
                        risque += 20
                    if x2['nom'] == 'asthme':
                        risque += 20
        if risque > 0:
            personnes_a_risque.append((e['nom'], e['prenom'], risque))

    personnes_a_risque.sort(key=lambda x: x[2], reverse=True)

    columns = ["Nom", "Prénom", "Risque"]
    w5.tab.setColumnCount(len(columns))
    w5.tab.setHorizontalHeaderLabels(columns)
    w5.tab.setRowCount(len(personnes_a_risque))

    for i, personne in enumerate(personnes_a_risque):
        nom, prenom, risque = personne

        w5.tab.setItem(i, 0, QTableWidgetItem(nom))
        w5.tab.setItem(i, 1, QTableWidgetItem(prenom))
        w5.tab.setItem(i, 2, QTableWidgetItem(str(risque) + "%"))

# afficher maladies par nat


def afficherMalParNat():
    personnes = loader.chargement("personne.csv")
    maladies = loader.chargementMaladies("maladies.csv")
    wnat.tab.setRowCount(0)
    ligne = 0
    for cin, maladies_cin in maladies.items():
        for maladie in maladies_cin:
            if(len(maladie.values()) and personnes[cin]["nationalite"] == wnat.natComboBox.currentText()):
                wnat.tab.insertRow(ligne)
                wnat.tab.setItem(ligne, 0, QTableWidgetItem(cin))
                wnat.tab.setItem(ligne, 1, QTableWidgetItem(maladie["nom"]))
                wnat.tab.setItem(ligne, 2, QTableWidgetItem(maladie["nb_annees"]))
                ligne += 1


def afficher_deces():
    f = "personne.csv"
    d = loader.chargement(f)
    decedes = []
    for cin, e in d.items():
        if e.get("decede", "0") == "1":
            decedes.append({cin: e})
    nb_deces = len(decedes)
    pourcentage_deces = round(nb_deces / len(d) * 100, 2)
    w6.tab.setColumnCount(7)
    w6.tab.setHorizontalHeaderLabels(["CIN", "Nom", "Prénom", "Age", "Nationalité", "Téléphone", "Adresse"])
    w6.tab.setRowCount(nb_deces)
    for ligne, l in enumerate(decedes):
        cin, e = list(l.items())[0]
        w6.tab.setItem(ligne, 0, QTableWidgetItem(cin))
        w6.tab.setItem(ligne, 1, QTableWidgetItem(e.get("nom", "")))
        w6.tab.setItem(ligne, 2, QTableWidgetItem(e.get("prenom", "")))
        w6.tab.setItem(ligne, 3, QTableWidgetItem(str(e.get("age", ""))))
        w6.tab.setItem(ligne, 4, QTableWidgetItem(e.get("nationalite", "")))
        w6.tab.setItem(ligne, 5, QTableWidgetItem(str(e.get("tel", ""))))
        w6.tab.setItem(ligne, 6, QTableWidgetItem(e.get("adresse", "")))

    w6.pourcentage.setText(f"Nombre de décès : {nb_deces} ({pourcentage_deces}%)")


# app
app = QApplication([])
window = loadUi("projetqtds.ui")
w = loadUi("ajouter.ui")
waffp = loadUi("afficherpersonne.ui")
wm = loadUi("ajoutermaladie.ui")
waffm = loadUi("affichermaladie.ui")
wsp = loadUi("suppressionp1.ui")
wsp2 = loadUi("suppressionp2.ui")
wsp3 = loadUi("suppressionp3.ui")
wnat = loadUi("recherchenatiop.ui")
w2 = loadUi("modifiertelpersonne.ui")
w5 = loadUi("affpersonnearisque.ui")
w6 = loadUi("affpersonnedecedescalcl.ui")
w7 = loadUi("modifieradressepers.ui")
w8 = loadUi("modifierdecesmaladie.ui")
w10 = loadUi("modifimaladienbreann.ui")
w11 = loadUi("modifnbrann.ui")
w12 = loadUi("personnequantine.ui")
w13 = loadUi("recherchedecedep.ui")
w14 = loadUi("RECHERCHEINDICATIFP.ui")
w15 = loadUi("recherchemaldchaque.ui")
w16 = loadUi("recherchenondecp.ui")
w17 = loadUi("recherchenump.ui")
wrm = loadUi("recherchemalpersonne.ui")
w18 = loadUi("rechercheparmaladuie.ui")
w19 = loadUi("recherchepourcentage.ui")
ws = loadUi("suppmaladie.ui")
wnat = loadUi("recherchenatiop.ui")


def afficherDeces():
    w6.showMaximized()
    w6.affiche.clicked.connect(afficher_deces)


def affnatio2():
    global countries
    wnat.showMaximized()
    fillComboBox(wnat.nat, countries)
    wnat.affiche.clicked.connect(afficherMalParNat)


def rechchaqueper():
    w15.showMaximized()
    w15.affiche.clicked.connect(affpersonne_tel)


def recherchenumtel():
    w17.showMaximized()
    w17.affiche.clicked.connect(affpersonne_tel)


def rechindica():
    w14.showMaximized()
    w14.affiche.clicked.connect(affpersonne_non_decede)


def persnondec():
    w16.showMaximized()
    w16.affiche.clicked.connect(affpersonne_non_decede)


def persdec():
    w13.showMaximized()
    w13.affiche.clicked.connect(affpersonne_decede)


def personnequarant():
    w12.showMaximized()
    w12.affiche.clicked.connect(afficher_quarantaine)


def mofifann():
    w11.showMaximized()
    w11.modif.clicked.connect(modifier_nb_annees)


def affnatiop():
    global e
    global countries
    fillComboBox(wnat.nat, countries)
    wnat.showMaximized()
    wnat.affiche.clicked.connect(affpersonne_nationalite)


def modifadress():
    w7.showMaximized()
    w7.modifier.clicked.connect(modifier_adresse)


def modiftel():
    w2.showMaximized()
    w2.modif.clicked.connect(modifier_tel)


def recherchepmalpource():
    w19.showMaximized()
    w19.affiche.clicked.connect(afficher_pourcentage)


def recherchepmalper():
    wrm.showMaximized()
    wrm.affiche.clicked.connect(afficher_par_cin)


def recherchepmal():
    w18.showMaximized()
    w18.affiche.clicked.connect(afficher_par_nom_maladie)


def suppmaladie():
    ws.showMaximized()
    ws.supprimer.clicked.connect(supprimerm)


def ajoutp():
    w.showMaximized()
    w.Ajouter.clicked.connect(ajouter)


def afficherp():
    waffp.showMaximized()
    # waffp.affper.clicked.connect(affpersonne)
    affpersonne()


def ajoutm():
    wm.showMaximized()
    wm.Ajouter.clicked.connect(ajouterm)


def affichermaladies():
    waffm.showMaximized()
    waffm.affm.clicked.connect(afficherm)


def suppressionp1():
    wsp.showMaximized()
    wsp.supprimer1.clicked.connect(supprimer_pers)


def suppressionp2():
    wsp2.showMaximized()
    wsp2.suppression.clicked.connect(supprimerp2)


def suppressionp3():
    wsp3.showMaximized()
    wsp3.supp3.clicked.connect(supprimerp3)


def affrisque():
    w5.showMaximized()
    w5.affiche.clicked.connect(afficher_personnes_a_risque)


window.actionAjouter.triggered.connect(ajoutp)
window.actionpersonnes_a_risque.triggered.connect(affrisque)
window.actiondicper.triggered.connect(afficherp)
window.actionajoutm_2.triggered.connect(ajoutm)
window.actioncontenu_du_dictionnaire_maladies_2.triggered.connect(affichermaladies)
window.actionsupprimer_une_maladie_2.triggered.connect(suppmaladie)
window.actionrecherche_par_une_maladie.triggered.connect(recherchepmal)
window.actionrecherche_maladie_d_une_personne.triggered.connect(recherchepmalper)
window.actionrecherche_le_pourcentage_de_chaque_maladie_2.triggered.connect(recherchepmalpource)
window.actiontelephone.triggered.connect(modiftel)
window.actionadresse.triggered.connect(modifadress)
window.actionsupp1.triggered.connect(suppressionp1)
window.actionsupp2.triggered.connect(suppressionp2)
window.actionsupp3.triggered.connect(suppressionp3)
window.actiontfgbhy.triggered.connect(mofifann)
window.action4_recherche_par_nationalite.triggered.connect(affnatiop)
window.actionpersonne_en_quarantaine.triggered.connect(personnequarant)
window.action5_recherche_des_personnes_decedes.triggered.connect(persdec)
window.action6_recherche_des_personnes_non_decedes.triggered.connect(persnondec)
window.action2_recherche_par_numero_telephone.triggered.connect(recherchenumtel)
window.action3_recherche_par_indicatif.triggered.connect(rechindica)
window.actionafficher_par_nationalite.triggered.connect(affnatio2)
window.actionpersonnes_decedes.triggered.connect(afficherDeces)

window.showMaximized()
app.exec_()
