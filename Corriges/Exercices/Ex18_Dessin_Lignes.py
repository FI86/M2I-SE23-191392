# Exercice 18
# Créer une fenêtre comportant trois boutons et un canevas. 
# Suivant la terminologie de tkinter, un canevas est une surface rectangulaire délimitée,
# dans laquelle on peut installer ensuite divers dessins et images à l’aide de méthodes 
# spécifiques. Lorsque l’on clique sur le bouton <Tracer une ligne>, une nouvelle ligne 
# colorée apparaît sur le canevas, avec à chaque fois une inclinaison différente de la précédente.
# Si l’on actionne le bouton <Autre couleur>, une nouvelle couleur est tirée au hasard dans une série 
# limitée et sera affichée dans un Entry. Cette couleur est celle qui s’appliquera aux tracés suivants.
# On affichera les coordonnées de début et fin de la ligne dans un Entry
# La couleur de la ligne sera aleatoire au commencement du programme.
# Le bouton <Quitter> va terminer l’application en refermant la fenêtre.

import tkinter as Tk
from random import choice
from math import sin, cos, radians

def traceLigne():
    global angle, coord
    x1 = int(cos(radians(angle)) * RAYON + CENTRE)
    y1 = int(sin(radians(angle)) * RAYON + CENTRE)
    x2 = int(-cos(radians(angle)) * RAYON + CENTRE)
    y2 = int(-sin(radians(angle)) * RAYON + CENTRE)

    can1.create_line(x1, y1, x2, y2, fill=couleur)
    coord.set(f"({x1}, {y1}) - ({x2}, {y2})")
    angle = (angle + 5) % 180

def autreCouleur():
    global couleur
    liste = ["red", "black", "grey", "green", "yellow", "maroon", "purple", "cyan", "orange", "blue"]
    couleur = choice(liste)
    strCouleur.set(f"{couleur}")

# Programme principal
TAILLE = 300
CENTRE = int(TAILLE / 2)
RAYON = CENTRE - 5
angle = 0
couleur = ""
root = Tk.Tk()
coord = Tk.StringVar()
strCouleur = Tk.StringVar()

autreCouleur()

can1 = Tk.Canvas(root, bg="dark grey", height=TAILLE, width=TAILLE)
button1 = Tk.Button(root, text="Quitter", command=root.destroy, width=20)
button2 = Tk.Button(root, text="Tracer une ligne", command=traceLigne, width=20)
button3 = Tk.Button(root, text="Autre couleur", command=autreCouleur, width=20)

can1.pack(side=Tk.LEFT)
button1.pack()
button2.pack()
button3.pack()

Tk.Entry(root, textvariable=coord, width=23).pack()
Tk.Entry(root, textvariable=strCouleur, width=23).pack()

# Gestions d'événements
root.bind("<Escape>", quit)

root.mainloop()