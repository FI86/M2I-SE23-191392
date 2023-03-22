# Fichier d'exemples pour les classes

class Classe1():
    def methode1(self):
        print("Classe 1 - methode 1")

    def methode2(self, chaine):
        print(f"Classe 1 - methode 2 : {chaine}")


class Classe2(Classe1):
    def methode1(self):
        print("Classe 2 - methode 1")

    def methode3(self):
        Classe1.methode1(self)
        print("Classe 2 - methode 3")


# Classe avec Constructeur
class Velo:
    # Attribut de classe (utiliser le nom de la classe ou cls)
    # Attention car utilisable comme un attribut d'objet selon le prefixe utilise
    nbRoues = 2

    # Constructeur
    def __init__(self, marque, prix, poids):
        # Attributs d'instances (objets)
        self.marque = marque
        self.prix = prix
        self.poids = poids

    def rouler(self):
        print(f"Je roule avec un vélo {self.marque} !")

    # Methode de classe
    @classmethod
    def combien(cls):
        print(f"Je roule avec un vélo à {cls.nbRoues} roues !")
        cls.nbRoues += 1
     
    # combien = classmethod(combien)

    # Methode static. cette methode n'utilise ni cls ni self.
    # Bonne pratique : prefixe l'appel de la fonction avec le nom de la classe.
    @staticmethod
    def afficher():
        print("Je suis une methode statique !")

    # afficher = staticmethod(afficher)

# Exemple Rectangle avec heritage de classe
class Rectangle(): 
    """Classe de rectangles"""

    def __init__(self, longueur = 0, largeur = 0):
        """Constructeur"""
        self.L = longueur 
        self.l = largeur 
        self.nom = "rectangle" 

    def perimetre(self): 
        return "({0:d} + {1:d}) * 2 = {2:d}" \
            .format(self.L, self.l, (self.L + self.l)*2) 

    def surface(self): 
        return "{0:d} * {1:d} = {2:d}".format(self.L, self.l, self.L*self.l) 
        
    def mesures(self): 
        print("Un {0} de {1:d} sur {2:d}".format(self.nom, self.L, self.l)) 
        print("a une surface de {0}".format(self.surface())) 
        print("et un périmètre de {0}\n".format(self.perimetre())) 


class Carre(Rectangle): 
    """Classe de carrés"""
    
    def __init__(self, cote): 
        # super().__init__(cote, cote)
        Rectangle.__init__(self, cote, cote) 
        self.nom = "carré"


def main():
    c1 = Classe1()
    c1.methode1()
    c1.methode2("ma chaine")
    c2 = Classe2()
    c2.methode1()
    c2.methode2("une chaine")
    c2.methode3()

    v1 = Velo("mbk", 120, 10)
    v2 = Velo("bike", 100, 13)
    v1.rouler()
    v2.rouler()
    print(f"Velo 1 possède {v1.nbRoues} roues")
    print(f"Velo 2 possède {v2.nbRoues} roues")
    # Mauvaise pratique
    v1.nbRoues = 3
    v2.nbRoues = 4
    print(f"Velo 1 possède {v1.nbRoues} roues")
    print(f"Velo 2 possède {v2.nbRoues} roues")
    # Bonne pratique
    Velo.nbRoues = 5
    print(f"Velo 1 possède {Velo.nbRoues} roues")
    print(f"Velo 2 possède {Velo.nbRoues} roues")
    print(f"Velo 1 possède {v1.nbRoues} roues")
    print(f"Velo 2 possède {v2.nbRoues} roues")    
    v1.combien()
    v2.combien()
    # Mauvaise pratique
    v1.afficher()
    v2.afficher()
    # Bonne pratique
    Velo.afficher()
    print()

    # Exemple Rectangle avec heritage de classe
    r1 = Rectangle(15, 30) 
    r1.mesures() 
    c1 = Carre(13) 
    c1.mesures()

if __name__ == "__main__":
    main()
