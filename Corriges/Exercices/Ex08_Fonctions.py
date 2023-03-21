# Exercice 8
# Ecrire une fonction cube qui retourne le cube de son argument.
# Ecrire une fonction volumeSphere qui calcule le volume d’une sphère de rayon r
# fourni en argument et qui utilise la fonction cube.
# Tester la fonction volumeSphere par un appel dans le programme principal.

def cube(x):
    return x ** 3

def volumeSphere(r):
    return 4/3 * 3.14 * cube(r)

def main():
    reponse = ""

    while reponse.upper() != "NON":
        rayon = float(input("Indiquez le rayon d'une sphere : "))
        print(f"Le volume de la sphere est de : {volumeSphere(int(rayon))}")

        reponse = input("Voulez-vous continuer oui / non ? ")

if __name__ == "__main__":
    main()