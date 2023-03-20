# Exercice 3
# Ecrivez un programme qui donne la somme des tous les nombres supérieurs à 10 se trouvant dans une liste.
# si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], 
# ce programme devrait afficher: la somme demandée est 134

def main():
    liste = [32, 5, 12, 8, 3, 75, 2, 15]
    somme = 0

    for val in liste:
        if val > 10:
            somme += val

    print(f"la somme demandée est {somme}")

if __name__ == "__main__":
    main()