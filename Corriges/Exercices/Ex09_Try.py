# Exercice 9
# Ecrire un programme qui demande à l’utilisateur de saisir une liste d’entiers puis à l’aide 
# de parcours successifs de la liste effectuer les actions suivantes:
# 1) Afficher la liste
# 2) Afficher la liste en colonne de manière à afficher l’index et le contenu
# 3) Créer une nouvelle liste qui sera chaque éléments de la liste multiplié par 3
# en utilisant une fonction lambda
# 4) Obtenir le plus grand nombre de la liste
# 5) Obtenir le plus petit nombre de la liste 
# 6) Compter le nombre des nombres pairs présents dans la liste
# 7) Calculer la somme de tous les nombres impairs de la liste
# NB: le programme doit gérer les exceptions au niveau de la saisie des données de l’utilisateur

def main():
    liste = []
    listeMultiple3 = []
    sommeImpaire = 0
    nbPair = 0
    reponse = ""

    while reponse.upper() != "FIN":
        reponse = input("Entrez un nombre entier : ")

        try:
            liste.append(int(reponse))
        except Exception as e:
            if reponse.upper() != "FIN":
                print("Saisissez un nombre entier.")

    print(f"1 - liste : {liste}")

    for num, val in enumerate(liste):
        print(f"2a - liste en colonne : {num + 1} - {val}")
        if val % 2 == 0: nbPair += 1
        else: sommeImpaire += val
    
    for x in range(len(liste)):
        print(f"2b - liste en colonne : {x + 1} - {liste[x]}")

    for x in liste:
        print(f"2c - liste en colonne : {liste.index(x) + 1} - {x}")

    listeMultiple3 = list(map(lambda x: x * 3, liste))
    print(f"3 - Liste Multiplie par 3 : {listeMultiple3}")
    print(f"4 - Nombre le plus élevé : {max(liste)}")
    print(f"5 - Nombre le moins élevé : {min(liste)}")
    print(f"6a - Nombre de nombre pairs : {nbPair}")
    nbPair = len(list(filter(lambda x: x % 2 == 0, liste)))
    print(f"6b - Nombre de nombre pairs : {nbPair}")
    print(f"7a - Somme des nombres impairs : {sommeImpaire}")
    sommeImpaire = sum(list(filter(lambda x: x % 2 == 1, liste)))
    print(f"7b - Somme des nombres impairs : {sommeImpaire}")

if __name__ == "__main__":
    main()