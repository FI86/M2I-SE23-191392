# Exercice 16
# Complément de l’exercice précédent : définir deux joueurs A et B. 
# Instancier deux jeux de cartes (un pour chaque joueur) et les mélanger. 
# Ensuite, à l’aide d’une boucle, tirer 52 fois une carte de chacun des deux 
# jeux et comparer leurs valeurs. Si c’est la première des deux qui a la valeur 
# la plus élevée, on ajoute un point au joueur A. Si la situation contraire se présente, 
# on ajoute un point au joueur B. Si les deux valeurs sont égales, on passe au tirage suivant. 
# Au terme de la boucle, comparer les comptes de A et B pour déterminer le gagnant.
 
from Ex15_JeuDeCartes import JeuDeCartes

def main():
    jeuA = JeuDeCartes()
    jeuB = JeuDeCartes()

    jeuA.melanger()
    jeuB.melanger()

    pointA = pointB = 0

    for _ in range(len(jeuA.cartes)):
        carteA = jeuA.tirer()
        carteB = jeuB.tirer()

        if carteA != None and carteB != None:
            if jeuA.valeurs.index(carteA[0]) > jeuB.valeurs.index(carteB[0]): pointA += 1
            if jeuA.valeurs.index(carteA[0]) < jeuB.valeurs.index(carteB[0]): pointB += 1

    print(f"A obtient {pointA} et B obtient {pointB}")

if __name__ == "__main__":
    main()