# Exercice 20
# Notre application doit faire apparaître une fenêtre comportant un dessin de la résistance,
# ainsi qu’un champ d’entrée dans lequel l’utilisateur peut encoder une valeur numérique. 
# Un bouton <Montrer> déclenche la modification du dessin de la résistance, de telle façon que 
# les trois bandes de couleur se mettent en accord
# avec la valeur numérique introduite. 
# Contrainte : Le programme doit accepter toute entrée numérique fournie sous forme entière ou réelle, 
# dans les limites de 10 à 1e11 Ω. Par exemple, une valeur telle que 4.78e6 doit être acceptée et 
# arrondie correctement, c’est-à-dire convertie en 4800000 Ω.

# Pour rappel, la fonction des résistances électriques consiste à s’opposer 
# (à résister) plus ou moins bien au passage du courant. Les résistances 
# se présentent concrètement sous la forme de petites pièces tubulaires cerclées de 
# bandes de couleur (en général 3). Ces bandes de couleur indiquent la valeur numérique de la 
# résistance, en fonction du code suivant :
# Chaque couleur correspond conventionnellement à l’un des chiffres de zéro à neuf :
# Noir = 0, Brun = 1, Rouge = 2, Orange = 3, Jaune = 4, Vert = 5, Bleu = 6, Violet = 7, Gris = 8, Blanc = 9.
# On oriente la résistance de manière telle que les bandes colorées soient placées à gauche. 
# La valeur de la résistance – exprimée en ohms (Ω) – s’obtient en lisant ces bandes colorées 
# également à partir de la gauche : les deux premières bandes indiquent les deux premiers chiffres 
# de la valeur numérique ; il faut ensuite accoler à ces deux chiffres un nombre de zéros égal 
# à l’indication fournie par la troisième bande.
# Exemple concret : supposons qu’à partir de la gauche, les bandes colorées soient jaune, 
# violette et verte. La valeur de cette résistance est 4700000 Ω, ou 4700 kΩ, ou encore 4,7 MΩ.

import tkinter as Tk

class Resistance:
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root = Tk.Tk()
        self.root.title('Code des couleurs')
        self.dessineResistance()
        Tk.Label(self.root, text = "Entrez la valeur de la résistance, en ohms : ").grid(row = 2)
        Tk.Button(self.root, text = "Montrer", command = self.changeCouleurs).grid(row = 3, sticky = "W") 
        Tk.Button(self.root, text = "Quitter", command = self.root.quit).grid(row = 3, sticky = "E")
        self.entree = Tk.Entry(self.root, width = 14)
        self.entree.grid(row = 3)
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.couleurs = ["black", "brown", "red", "orange", "yellow", "green", "blue", "purple", "grey", "white"]
        self.root.mainloop()
        
    def dessineResistance(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.can = Tk.Canvas(self.root, width = 250, height = 100, bg = "ivory")
        self.can.grid(row = 1, pady = 5, padx = 5)
        self.can.create_line(10, 50, 240, 50, width = 5)  # fils
        self.can.create_rectangle(65, 30, 185, 70, fill = "light grey", width = 2) # resistance
        self.ligne = [] # on mémorisera les trois lignes dans 1 liste  
        # Dessin des trois lignes colorées (noires au départ) :
        for x in range(85, 150, 24):
            self.ligne.append(self.can.create_rectangle(x, 30, x + 12, 70, fill = "black", width = 0))

    def changeCouleurs(self):
        """Affichage des couleurs correspondant à la valeur entrée"""
        self.valeurSaisie = self.entree.get()   # la méthode get() renvoie une chaîne

        if self.valeurSaisie.isdigit() == True:
            valeur = int(self.valeurSaisie)   # conversion en valeur numérique
            err = 0
        else: 
            valeur = 0
            err = 1                         # erreur : entrée non numérique

        if err == 1 or valeur < 10 or valeur > 1e11 :
            self.signaleErreur()            # entrée incorrecte ou hors limites
        else:
            li = [0] * 3                    # liste des 3 codes à afficher, [0, 0 ,0] par defaut
            longeurNombre = len(self.valeurSaisie) - 1
            ordre_grandeur = 10 ** longeurNombre
            # extraction du premier chiffre significatif :
            li[0] = valeur // ordre_grandeur  # partie entière
            decim = round(valeur / ordre_grandeur - li[0] , 1)  # partie décimale
            # extraction du second chiffre significatif :
            li[1] = int(decim * 10)
            # nombre de zéros à accoler aux 2 chiffres significatifs :
            li[2] = longeurNombre - 1                                 
            # Coloration des 3 lignes :
            for n in range(3):
                # itemconfigure permet de changer une propriété d'un objet tkinter deja affiché.
                self.can.itemconfigure(self.ligne[n], fill = self.couleurs[li[n]])
            
    def signaleErreur(self):
        self.entree.configure(bg = "red")		# colorer le fond du champ
        self.root.after(1000, self.videEntree)	# après 1 seconde, effacer
        
    def videEntree(self):
        self.entree.configure(bg = "white")		# rétablir le fond blanc
        self.entree.delete(0, "end")		    # enlever les car. présents

# Programme principal :        
def main():
    f = Resistance()		# instanciation de l'objet application

if __name__ == "__main__":
    main()