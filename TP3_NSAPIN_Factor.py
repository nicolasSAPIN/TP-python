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

import  TP3_NSAPIN_FactotFonction as factFonct

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------
produits ={1:{ 'nom':'banane', 'prix':4},
           2:{'nom':'pomme', 'prix':2} ,
           3:{ 'nom':'orange', 'prix':4},
           4:{ 'nom':'poire', 'prix':3}}


tabResult = {}
PrixTotal = 0
stop=0
i=0


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------


def saisichoix():
    choix = input("Entrer l'id produit : ")
    return int(choix)

def saisiQuantite():
    Quantite= input("Entrer la quantite du produit: ")
    return float(Quantite)

#Excpetinputs
def controlQuantite(Quantite):
    try:
       Quantite = input('Entrez une Quantité : ')

    except ValueError:
        print("Quantite doit etre un chiffre!!")

def controlChoix(choix):
    if not (1 <= choix <= 4):
        raise ValueError("x n'est pas dans[1..4]")
    input('Entrez une Quantité : ')
    # try:
    #      choix = int(input('Faites  votre choix: '))
    #
    # except ValueError:
    #     print("Votre choix ne peut etre que 1, 2, 3 ou 4.")


# Calcul du total HT par article----
def CalculPrixArtHt(prix, quantite):
    PrixArtHt = prix * quantite
    return PrixArtHt

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

#affiche le tableau de Choix
def affichTabChoix(Articles):
    print("|Saisissez   |   Produit    |    prix   |")
    for j in range(0, 4):
        print(j + 1,"             ",Articles[j]['nom'],"              ",Articles[j]['prix'])

# affichage tableau de resultat
def affichTabResult(tabResult):
    for k in range(0, len(tabResult)):
        print(tabResult[k])

def IncrementTotalHT(TotalHT,prix,Qtite):
    TotalHT=TotalHT+(prix*Qtite)
    return TotalHT



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
    factFonct.affichTabChoix(Articles)
    # print("|Saisissez   |   Produit    |    prix   |")
    # for j in range(0, 4):
    #     print(j + 1,
    #           "             ",
    #           Articles[j]['nom'],
    #           "              ",
    #           Articles[j]['prix'])


    choix=saisichoix()
    Quantite=saisiQuantite()

    # Saisie du prix------
    # try:
    #     choix = int(input('Faites  votre choix: '))
    # except ValueError:
    #     print("Votre choix ne peut etre que 1, 2, 3 ou 4.")
    #
    # # Saisie de la Quantité----
    # try:
    #     Quantite = float(input('Entrez une Quantité : '))
    # except ValueError:
    #     print("Quantite doit etre un chiffre!!")

    # Calcul du total HT par article----
    PrixArtHt = CalculPrixArtHt(Articles[choix - 1]['prix'], Quantite)
   # PrixArtHt = Articles[choix - 1]['prix'] * Quantite  # choix -1 car liste commence a index 0

    # Creation du tableau de resultat (1 ligne a chaqur boucle)
    tabResult.append({'nom': Articles[choix - 1]['nom'],  # choix -1 car liste commence a index 0
                      'prix': Articles[choix - 1]['prix'],  # choix -1 car liste commence a index 0
                      'Quantite': [Quantite],
                      'Total_HT': [PrixArtHt]})
    # Calcul du prix total_HT qui s'incremente a chaque boucle
    PrixTotalHT =IncrementTotalHT(PrixTotalHT, Articles[choix - 1]['prix'], Quantite)
    # PrixTotalHT = PrixTotal + Articles[choix - 1]['prix'] * Quantite




# affichage tableau de resultat

affichTabResult(tabResult)
# for k in range(0, len(tabResult)):
#     print(k)
#     print(tabResult[k])
#     # print(tabResult[k]['nom']," ", tabResult[k]['prix']," ", tabResult[k]['Quantite'], " ", tabResult[k]['Total_HT'])



# Affichage du prix total HT
print("Prix total HT est de: ", PrixTotalHT)

#  Calcul et affichage du prix TTC
PrixTotalTTC =factFonct.TotalTTC(PrixTotalHT)
# PrixTotalTTC = PrixTotal * 1.2
print("Prix TTC est de: ", PrixTotalTTC)


# Calcul de ma remise si Prix depasse 200
print(factFonct.test_remise(PrixTotalTTC,200, 0.05))
#remise=test_remise(PrixTotalTTC,200, 0.05)
# if (PrixTotalTTC > 200):
#     Prix_TTC = PrixTotalTTC * 0.95  # 0.95 signifie 5%
#     Remise = Prix_TTC * 0.05
#     print("Remise de 5% de: ", Remise)
#     print("Prix après remise: ", Prix_TTC)
