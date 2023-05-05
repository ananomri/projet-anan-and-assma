import csv
'''
dic={}
dic_ren={'12569'🙁'Golf','Noir','10/02/2010'],'19999'🙁'Mercedes','Rouge','10/02/2019'],'16999'🙁'BMW','Blanc','10/02/2022']}
dic_ren['9999']=['Aston Martin','Black','04/04/2022']
dic_test={}
'''

def existe(d,x):
    for k in d.keys():
        if k==x:
            return True
    return False


def remplir_dic():
    dic={}    
    while True:
        mat=input("Saisit la Matricule :")
        if(existe(dic,mat)==True):
            print("La matricule deja existe !")
            continue
        mod=input("Saisit le Modele : ")
        col=input("Saisit la Couleur :")
        dat=input("Saisit la Date d'achat : ")
        dic[mat]=[mod,col,dat]
        while True:
            rep=input("Voulez-vous Ajoutez une Voiture (Y/N) : ")
            if rep=='Y' or rep=='N':
                break
        if rep=='N':
            break
    return dic


def literal_eval(ch):
    d= dict()
    ch = ch.replace("'", "").replace('"', '').replace("{", "").replace("}", "")
    for i in ch.split(","):
        if(i.strip() != ''):
            cle, val = i.split(":")
            cle = cle.strip()#[1:-1]
            val = val.strip()#[1:-1]
            d[cle] = val
    if(len(d.items())>0):
        return d
def toList(ch):
    ch = ch[1:-1]
    ch = "".join(ch.split())
    print(ch)
    #print(ch.split("},"))
    if "}," in ch:
        return [i+"}" for i in ch.split("},")]
    else:
        return [ch]
    
def chargement(ch):
    dic=dict()
    with open(ch) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            l = literal_eval(row[1])
            dic[row[0]]= l if l != None else {}
    return dic

def chargementMaladies(ch):
    dic=dict()
    with open(ch) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            dic[row[0]]=[literal_eval(i) for i in toList(row[1]) if literal_eval(i) != None]
    return dic


def enregistrement(dic, ch):
    print("saving...")
    with open(ch, 'w',newline='\n') as f:
        writer = csv.writer(f, delimiter=';')
        for cle,val in dic.items():
            ch=[cle, val]
            writer.writerow(ch)
    print("saved!")


def aff_dic(x):
    for cle,val in x.items():
        print(cle,val)
        
        
#dic_test=remplir_dic()
#enregistrement(dic_test)
#dic_test=chargement()
#aff_dic(dic_test)
#enregistrement(dic_ren)
#chargement(dic_test)