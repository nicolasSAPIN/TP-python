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
import TP2_3NSAPIN_FactorFonction as FonctImp

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------

Articles = [{'nom': 'banane', 'prix': 4},
            {'nom': 'pomme', 'prix': 2},
            {'nom': 'orange', 'prix': 4},
            {'nom': 'poire', 'prix': 3}]
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
#					Début du PROGRAMME
#-------------------------------------------------------



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
    FonctImp.creaPanier(Articles[choix - 1]['nom'], Articles[choix - 1]['prix'], Quantite, PrixArtHt, PrixTotalHT)

    # tabResult.append({'nom': Articles[choix - 1]['nom'],
    #                   'prix': Articles[choix - 1]['prix'],
    #                   'Quantite': [Quantite],
    #                   'Total_HT': [PrixArtHt]})# choix -1 car liste tabResultcommence a index 0

    # Calcul du prix total_HT qui s'incremente a chaque boucle
    PrixTotalHT =FonctImp.IncrementTotalHT(PrixTotalHT, Articles[choix -1]['prix'], Quantite)
    # PrixTotalHT = PrixTotalHT + Articles[choix]['prix'] * Quantite

# affichage tableau de resultat

FonctImp.affichTabResult(tabResult)

# for k in range(0, len(tabResult)):
#     print(k)
#     print(tabResult[k])
#     # print(tabResult[k]['nom']," ", tabResult[k]['prix']," ", tabResult[k]['Quantite'], " ", tabResult[k]['Total_HT'])

# Affichage du prix total HT

FonctImp.AffichPrixTotalHT(PrixTotalHT)
# print("Prix total HT est de: ", PrixTotalHT)

#  Calcul et affichage du prix TTC
PrixTotalTTC =FonctImp.TotalTTC(PrixTotalHT)
# PrixTotalTTC = PrixTotalHT * 1.2
print("Prix TTC est de: ", PrixTotalTTC)

# Calcul de ma remise si Prix depasse 200
# print(test_remise(PrixTotalTTC,200, 0.05))
remise=FonctImp.test_remise(PrixTotalTTC,200, 0.05)
# if (PrixTotalTTC > 200):
#     Prix_TTC = PrixTotalTTC * 0.95  # 0.95 signifie 5%
#     Remise = Prix_TTC * 0.05
#     print("Remise de 5% de: ", Remise)
#     print("Prix après remise: ", Prix_TTC)