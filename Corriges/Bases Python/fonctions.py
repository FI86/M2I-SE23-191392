# Fichier d'exemples pour les fonctions

# Ecrire une fonction basique
def fonction1():
    print("Je suis une fonction")

# Variables locales et variables globales
varg = 5

def uneFonction():
    # global varg
    varg = 10
    print(varg)

uneFonction()
print(varg)

# Fonction qui prend plusieurs arguments
def fonction2(arg1, arg2):
    print(arg1, arg2)

# Fonction qui retourne une valeur
def cube(x):
    return x ** 3

# Fonction avec une valeur par défaut dans ses arguments
# (arguments nommés permet aussi d'envoyer dans le désordre)
def puissance(num, x = 1):
    resultat = num
    for _ in range(1, x):
        resultat *= num
    return resultat

# Fonction avec un nombre variable d'arguments
def argsMultiple(*args):
    resultat = 0
    for x in args:
        resultat += x
    return resultat

# Argument nommé obligatoire pour être modifier
def uneFonctionSup(num = 1, x = 1, *, valide = True):
    # Test si valide est booléen
    if isinstance(valide, bool) == False:
        print("valide n'est pas un booléen !")
        return -1

    if valide == True:
        return num + x
    else:
        return 0

# Fonction principale
def main():
    fonction1()
    fonction2(10, 20)
    print(cube(3))
    print(puissance(2))
    print(puissance(2, 3))
    print(puissance(x = 3, num = 2))
    print(argsMultiple(4, 5, 10, 4))
    print(uneFonctionSup(1, 2, valide = False))

# Appel fonction principale
if __name__ == "__main__":
    main()