"""
TP  : Creation d'un logiciel de caisse avec tableau et dictionnaire

Auteur(s) : Nicolas SAPIN
"""



produits ={1:{ 'nom':'banane', 'prix':4},
           2:{'nom':'pomme', 'prix':2} ,
           3:{ 'nom':'orange', 'prix':4},
           4:{ 'nom':'poire', 'prix':3}}


tabResult = {}
PrixTotal = 0
stop=0
i=0

while stop == 0:
    #affichage du tableau "produits"
    print("|Saisissez   |   Produit    |    prix   |")
    for j in range(1, 5):
        print(j, "             ", produits[j]['nom'], "          ", produits[j]['prix'])

    # Saisie du prix

    choix = int(input('Faites  votre choix: '))
    while choix <= 0:
        print("Erreur de saisi: votre prix doit etre positif")
        choix = int(input('Faites  votre choix: '))

    # Saisie de la Quantité
    Valeur_saisi2 = input('Entrez une Quantité : ')
    Quantite = float(Valeur_saisi2)
    while Quantite <= 0:
        print("Erreur de saisi: votre Quantite doit etre positif")
        Valeur_saisi2 = input('Entrez une Quantité : ')
        Quantite = float(Valeur_saisi2)

    #
    # while True:
    #     try:
    #         choix = int(input("Quel article souhaitez vous choisir? " ))
    #         choix = int(math.fabs(choix))
    #         break
    #     except ValueError:
    #         print("Choisissez une valeur correcte  ")
    #
    # # saisi de la quantite
    #
    # try:
    #     Quantite = float(input('Quelle Quantité : '))
    #     if(Quantite<=0)
    #         raise ValueError
    #     break
    #     except ValueError:
    #     print('Veuillez entrer un nombre positif.')
    # except:
    #     print('Quelle Quantité : ')

    #Calcul du prix HT
    Total_Ht = produits[choix]['prix'] * Quantite
    i = i + 1  # i sert a la creation du dictionnaire
    tabResult = {i: {'nom': produits[choix]['nom'], 'prix': produits[choix]['prix'], 'Quantite': Quantite,'Total_HT': Total_Ht }}

    #Calcul du prix total HT au fur est a meusure que l utilisateur ajoute des articles
    PrixTotal = PrixTotal+ (produits[choix]['prix'] * Quantite)

    #Demande a lutilisateur si il veut continuer ou continuer
    # La boucle principal s'arrete si Stop passe à 1
    ValeurContinu = input("Souhaitez-vous choisir un nouvel article? (1) pour Oui ou 0(Zero) pour Non")
    Arret = int(ValeurContinu)
    if Arret==0 : stop=1

    #Création et affichage du tableau de resultats au fur et a meusure

print("| Produit    |    prix   | Quantité |  Prix HT |")

for k in range(1, i+1):
    print(tabResult[k]['nom']," ", tabResult[k]['prix']," ", tabResult[k]['Quantite'], " ", tabResult[k]['Total_HT'])
# for k in range(1, i+1):
#     print (tabResult[k])


#Affichage du prix total HT
print("Prix total HT est de: ",PrixTotal)

#Calcul et affichage du prix TTC
Prix_TTC=PrixTotal*1.2
print("Prix TTC est de: ",Prix_TTC)

#Calcul de ma remise si Prix depasse 200
if (Prix_TTC > 200):

    Prix_TTC = Prix_TTC * 0.95  # 0.95 signifie 5%
    Remise = Prix_TTC*0.05
    print("Remise de 5% de: ", Remise)
    print("Prix après remise: ", Prix_TTC)