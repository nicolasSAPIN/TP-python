"""
TP  : Creation d'un logiciel de caisse avec tableau et dictionnaire

Auteur(s) : Nicolas SAPIN
"""

# -----------------------------------------------------------------------------
#   TP3 refactorisé
#
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------
import math


#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------
produits ={1:{ 'nom':'banane', 'prix':4},
           2:{'nom':'pomme', 'prix':2} ,
           3:{ 'nom':'orange', 'prix':4},
           4:{ 'nom':'poire', 'prix':3}}
prix = 0
Quantite = 0
tabResult = {}
PrixTotHT = 0
PrixTotalTTC = 0
PrixTotalHT=0
PrixArtHt = 0
stop=0
i=0
j=0
k=0

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------
#affiche le tableau de Choix
def affichTabChoix(Articles):
    print("|Saisissez   |   Produit    |    prix   |")
    for j in range(0, 4):
        print(j + 1,"             ",Articles[j]['nom'],"              ",Articles[j]['prix'])


def saisichoix():
    choix = input("Entrer l'id produit : ")
    return int(choix)

def controlChoix(choix):
    if not (1 <= choix <= 4):
        raise ValueError("x n'est pas dans[1..4]")
    input('Entrez une Quantité : ')
    # try:
    #      choix = int(input('Faites  votre choix: '))
    #
    # except ValueError:
    #     print("Votre choix ne peut etre que 1, 2, 3 ou 4.")

def saisiQuantite():
    Quantite= input("Entrer la quantite du produit: ")
    return float(Quantite)
#Excpetinputs
def controlQuantite(Quantite):
    try:
       Quantite = input('Entrez une Quantité : ')

    except ValueError:
        print("Quantite doit etre un chiffre!!")


# Calcul du total HT par article----
def CalculPrixArtHt(prix, quantite):
    PrixArtHt = prix * quantite
    return

def creaPanier(nomArt,prix,quantite,totArtHT,PrixTotHT):
    tabResult.append({'nom': [nomArt],  # choix -1 car liste commence a index 0
                      'prix': [prix],  # choix -1 car liste commence a index 0
                      'Quantite': [quantite],
                      'Total_HT': [totArtHT]})
    # Calcul du prix total_HT qui s'incremente a chaque boucle
    PrixTotalHT = IncrementTotalHT(PrixTotHT,prix, quantite)

def IncrementTotalHT(TotalHT,prix,Qtite):
    TotalHT=TotalHT+(prix*Qtite)
    return TotalHT

def AffichPrixTotalHT(PrixTotalHT):
    print("Prix total HT est de: ", PrixTotalHT)

# affichage tableau de resultat
def affichTabResult(tabResult):
    for k in range(0, len(tabResult)):
        print(tabResult[k])


#  Calcul prix TTC
def TotalTTC(montantHT):
    PrixTTC=montantHT*1.2
    return PrixTTC

# Calcul de ma remise si Prix depasse 200
def test_remise(montant,limite, prct):
    prixRemise = 0
    if (montant > limite):
        prixRemise = montant * (1 - prct)  # 0.95 signifie 5%
        print ("Prix après remise: ", prixRemise)
    else:
        print ("Remise de 5% seulement a partir de 200€")

#-------------------------------------------------------
#					Début du PROGRAMME
#-------------------------------------------------------

tabResult = {}
tabResult = []
PrixTotalHT = 0

Articles = [{'nom': 'banane', 'prix': 4}, {'nom': 'pomme', 'prix': 2}, {'nom': 'orange', 'prix': 4},
            {'nom': 'poire', 'prix': 3}]

# choix du nombre d'articles
NbrArticles = input("Combien d\'articles différents souhaitez-vous saisir?")
PrixTotal = 0
for i in range(1, int(NbrArticles) + 1):
    # affichage du tableau pour le choix------

    #factFonct.affichTabChoix(Articles)

    print("|Saisissez   |   Produit    |    prix   |")
    for j in range(0, 4):
        print(j + 1,
              "             ",
              Articles[j]['nom'],
              "              ",
              Articles[j]['prix'])

    # choix=saisichoix()
    # Quantite=saisiQuantite()

    #Saisie du prix------
    try:
        choix = int(input('Faites  votre choix: '))
    except ValueError:
        print("Votre choix ne peut etre que 1, 2, 3 ou 4.")
    # Saisie de la Quantité
    try:
        Quantite = float(input('Entrez une Quantité : '))
    except ValueError:
        print("Quantite doit etre un chiffre!!")

    # Calcul du total HT par article----
    # PrixArtHt=CalculPrixArtHt(Articles[choix- 1]['prix'],Quantite)
    PrixArtHt = Articles[choix - 1]['prix'] * Quantite  # choix -1 car liste commence a index 0

    # Creation du tableau de resultat (1 ligne a chaqur boucle)
    creaPanier(Articles[choix - 1]['nom'], Articles[choix - 1]['prix'], Quantite, PrixArtHt, PrixTotalHT)

    # tabResult.append({'nom': Articles[choix - 1]['nom'],
    #                   'prix': Articles[choix - 1]['prix'],
    #                   'Quantite': [Quantite],
    #                   'Total_HT': [PrixArtHt]})# choix -1 car liste tabResultcommence a index 0

    # Calcul du prix total_HT qui s'incremente a chaque boucle
    PrixTotalHT =IncrementTotalHT(PrixTotalHT, Articles[choix -1]['prix'], Quantite)
    # PrixTotalHT = PrixTotalHT + Articles[choix]['prix'] * Quantite

# affichage tableau de resultat

affichTabResult(tabResult)

# for k in range(0, len(tabResult)):
#     print(k)
#     print(tabResult[k])
#     # print(tabResult[k]['nom']," ", tabResult[k]['prix']," ", tabResult[k]['Quantite'], " ", tabResult[k]['Total_HT'])

# Affichage du prix total HT

AffichPrixTotalHT(PrixTotalHT)
# print("Prix total HT est de: ", PrixTotalHT)

#  Calcul et affichage du prix TTC
PrixTotalTTC =TotalTTC(PrixTotalHT)
# PrixTotalTTC = PrixTotalHT * 1.2
print("Prix TTC est de: ", PrixTotalTTC)

# Calcul de ma remise si Prix depasse 200
# print(test_remise(PrixTotalTTC,200, 0.05))
remise=test_remise(PrixTotalTTC,200, 0.05)
# if (PrixTotalTTC > 200):
#     Prix_TTC = PrixTotalTTC * 0.95  # 0.95 signifie 5%
#     Remise = Prix_TTC * 0.05
#     print("Remise de 5% de: ", Remise)
#     print("Prix après remise: ", Prix_TTC)