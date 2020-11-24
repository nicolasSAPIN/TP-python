
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
