# TP 1
# Écrivez un programme qui analyse un par un tous les éléments d’une 
# liste de mots (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'])
# pour générer deux nouvelles listes.  L’une contiendra les mots comportant moins de 6 caractères, 
# l’autre les mots comportant 6 caractères ou davantage

def main():
    liste = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
    liste1 = []
    liste2 = []

    for element in liste:
        if len(element) < 6: liste1.append(element)
        else: liste2.append(element)

    print(liste1)
    print(liste2)
    
if __name__ == "__main__":
    main()