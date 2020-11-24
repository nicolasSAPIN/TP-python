"""
TP 2 : Creation d'un logiciel de caisse
Auteur(s) : Nicolas SAPIN
"""
#on demande a l'utilisateur de saisir un prix HT ainsi qu'une quantite

prix = 0
Quantite = 0
tabResult = {}
PrixTotHT = 0
PrixTotalTTC = 0
PrixTotalHT=0
PrixArtHt = 0
stop=0
i=0

NbrArticles = input("Combien d\'articles différents souhaitez-vous saisir?" )


for i in range (1, int(NbrArticles)+1):

    # Saisie du prix
    Valeur_saisi1 = input('Entrez un Prix : ')
    Prix = float(Valeur_saisi1)
    while Prix <= 0:
        print("Erreur de saisi: votre prix doit etre positif")
        Valeur_saisi1 = input('Entrez un Prix : ')
        Prix = float(Valeur_saisi1)
    # Saisie de la Quantité
    Valeur_saisi2 = input('Entrez une Quantité : ')
    Quantite = float(Valeur_saisi2)
    while Quantite <= 0:
        print("Erreur de saisi: votre Quantite doit etre positif")
        Valeur_saisi2 = input('Entrez une Quantité : ')
        Quantite = float(Valeur_saisi2)

    # Calculer et afficher le prix total, sur la base d’une TVA de 20%
    # TVA a 20%: multiplier le total par 1.20 revient a faire x*20/100
    if Prix > 0 or Quantite > 0:
        Prix_TTC = (Prix * Quantite) * 1.20
        print("Pour L'article n° ", i ,", Le prix HT est de:", Prix * Quantite)
        print("Pour L'article n° ", i ,", Le prix TTC est de:", Prix_TTC)
        # Si le total dépasse les 200€, vous effectuerez une remise de 5%
        if (Prix_TTC >= 200):
            Prix_TTC = Prix_TTC * 0.95  # 0.95 signifie 5%
            print("Pour L'article n° ", i ,", Le prix TTC  avec remise de 5 % est de:", Prix_TTC)

    # Vous prendrez soin de vérifier les saisies utilisateurs : un prix et une quantité ne peuvent pas être nul ou négatif.

PrixTotal=PrixTotal+Prix_TTC
print("------------------------------------------------")
print("Le prix total de votre achat est de: ", PrixTotal)

#on aurai tres bien pu n'appliquer la TVA et la remise a la fin, le resutat aurait ete le même