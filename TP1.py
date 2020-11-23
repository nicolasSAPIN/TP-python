"""
TP 1 : Creation d'un logiciel de caisse
Auteur(s) : Nicolas SAPIN
"""
#on demande a l'utilisateur de saisir un prix HT ainsi qu'une quantite

Valeur_saisi1 = input('Entrez un Prix : ')
Prix= float(Valeur_saisi1 )

Valeur_saisi2 = input('Entrez une Quantité : ')
Quantite=float(Valeur_saisi2 )


if Prix <= 0:
    print("Erreur de saisi: votre prix doit etre positif")
    Valeur_saisi1 = input('Entrez un Prix : ')
    Prix = int(Valeur_saisi1)

if Quantite <= 0:
    print("Erreur de saisi: votre prix doit etre positif")
    Valeur_saisi2 = input('Entrez une Quantité : ')
    Quantite = float(Valeur_saisi2)


# Calculer et afficher le prix total, sur la base d’une TVA de 20%
# TVA a 20%: multiplier le total par 1.20 revient a faire x*20/100
if Prix >0 or Quantite >0:
    Prix_TTC = (Prix * Quantite) * 1.20
    print("Votre prix HT est de:", Prix * Quantite)
    print("Votre prix TTC est de:", Prix_TTC)
    # Si le total dépasse les 200€, vous effectuerez une remise de 5%
    if (Prix_TTC >= 200):
        Prix_TTC = Prix_TTC * 0.95  # 0.95 signifie 5%
        print("Votre prix TTC  avec remise de 5 % est de:", Prix_TTC)

# Vous prendrez soin de vérifier les saisies utilisateurs : un prix et une quantité ne peuvent pas être nul ou négatif.