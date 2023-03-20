# Exercice 2
# Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. 
# Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
# le plus grand élément de cette liste à la valeur 75.

def main():
    liste = [32, 5, 12, 8, 3, 75, 2, 15]
    valMax = liste[0]

    for val in liste:
        if val > valMax: valMax = val

    print(f"le plus grand élément de cette liste a la valeur {valMax}")

if __name__ == "__main__":
    main()