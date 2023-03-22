# Exercice 13
# Définissez une classe Cercle(). Les objets construits à partir de cette classe seront des 
# cercles de tailles variées. En plus de la méthode constructeur 
# (qui utilisera donc un paramètre rayon), vous définirez une méthode surface(), 
# qui devra renvoyer la surface du cercle.
# Définissez ensuite une classe Cylindre() dérivée de la précédente. Le constructeur de cette nouvelle 
# classe comportera les deux paramètres rayon et hauteur. 
# Vous y ajouterez une méthode volume() 
# qui devra renvoyer le volume du cylindre (rappel : volume d’un cylindre = surface de section × hauteur).

# Exemple d’utilisation de cette classe :
# >>> cyl = Cylindre(5, 7)
# >>> print(cyl.surface())
# 78.54
# >>> print(cyl.volume())
# 549.78

import math

class Cercle():
    """ Définition d'un cercle """
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return math.pi * self.rayon ** 2

class Cylindre(Cercle):
    """ Définition d'un cylindre """
    def __init__(self, rayon, hauteur):
        # Cercle.__init__(self, rayon)
        super().__init__(rayon) # avec la fonction super() on ne met pas le self en parametre
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur
        # return super().surface() * self.hauteur # ou avec la fonction super() puisque surface appartient a la classe mere

def main():
    cyl = Cylindre(5, 7)
    print(f"surface : {round(cyl.surface(), 2)}")
    print(f"volume : {round(cyl.volume(), 2)}")

if __name__ == "__main__":
    main()