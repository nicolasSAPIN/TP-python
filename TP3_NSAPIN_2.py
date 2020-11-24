"""
TP  : Creation d'un logiciel de caisse avec tableau et dictionnaire
Auteur(s) : Nicolas SAPIN

REMPLACE le TP3_NSAPIN
"""
tabResult = {}
tabResult = []
PrixTotalHT = 0

Articles= [{'nom':'banane', 'prix':4},{'nom':'pomme', 'prix':2},{ 'nom':'orange', 'prix':4},{'nom':'poire', 'prix':3}]

#choix du nombre d'articles
NbrArticles = input("Combien d\'articles différents souhaitez-vous saisir?" )
PrixTotal=0
for i in range (1, int(NbrArticles)+1):
    #affichage du tableau pour le choix------
    print("|Saisissez   |   Produit    |    prix   |")
    for j in range(0,4):
        print(j+1,
              "             ",
              Articles[j]['nom'],
              "              ",
              Articles[j]['prix'])

    # Saisie du prix------
    try:
        choix = int(input('Faites  votre choix: '))
    except ValueError:
        print("Votre choix ne peut etre que 1, 2, 3 ou 4.")

    # Saisie de la Quantité----
    try:
        Quantite = float(input('Entrez une Quantité : '))
    except ValueError:
        print("Quantite doit etre un chiffre!!")
    #Calcul du total HT par article----
    PrixArtHt = Articles[choix-1]['prix'] * Quantite #choix -1 car liste commence a index 0

    #Creation du tableau de resultat (1 ligne a chaqur boucle)
    tabResult.append({'nom': Articles[choix-1]['nom'],#choix -1 car liste commence a index 0
                      'prix': Articles[choix-1]['prix'], #choix -1 car liste commence a index 0
                      'Quantite': [Quantite],
                      'Total_HT': [PrixArtHt]})
    # Calcul du prix total_HT qui s'incremente a chaque boucle
    PrixTotalHT = PrixTotal + Articles[choix-1]['prix'] * Quantite

#affichage tableau de resultat
for k in range(0, len(tabResult)):
    print (k)
    print(tabResult[k])
    #print(tabResult[k]['nom']," ", tabResult[k]['prix']," ", tabResult[k]['Quantite'], " ", tabResult[k]['Total_HT'])

#Affichage du prix total HT
print("Prix total HT est de: ",PrixTotalHT)


#Calcul et affichage du prix TTC
PrixTotalTTC=PrixTotal*1.2
print("Prix TTC est de: ",PrixTotalTTC)

#Calcul de ma remise si Prix depasse 200
if (Prix_TTC > 200):
    Prix_TTC = Prix_TTC * 0.95  # 0.95 signifie 5%
    Remise = Prix_TTC*0.05
    print("Remise de 5% de: ", Remise)
    print("Prix après remise: ", Prix_TTC)
