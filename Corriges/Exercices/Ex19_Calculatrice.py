# Exercice 19
# Calculatrice simple avec les opérations de base (+, -, *, /).

import tkinter as tk
from tkinter import END, EW

root = tk.Tk()
root.title("Mini calculatrice")
root.config(borderwidth = 5)
operation = ""
nombre1 = 0
nombre2 = 0
cliqueEgale = False
affichage = tk.Entry(root, width = 60, borderwidth = 5)
affichage.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def boutonRAZ():
    affichage.delete(0, END)

def boutonClick(chiffre):
    global cliqueEgale

    # Ne fait rien si le chiffre cliqué est 0 et que l'afficheur est vide ou nul.
    if affichage.get().strip("0") == "" and chiffre == 0: return

    cliqueEgale = False
    nombre = affichage.get()
    boutonRAZ()
    affichage.insert(0, str(nombre) + str(chiffre))

def boutonOperation(op):
    global cliqueEgale, operation, nombre1

    # Valide l'opération si un nombre est saisie
    if affichage.get().strip("0") not in ["", "."]:
        cliqueEgale = False
        operation = op
        nombre1 = float(affichage.get())
        boutonRAZ()

def boutonEgale():
    global cliqueEgale, nombre1, nombre2

    # Test si une operation a été choisi et si un 2eme nombre est saisie
    if operation != "" and affichage.get().strip("0") not in ["", "."]:
        # Si le bouton égale n'a pas déjà été cliqué
        if cliqueEgale == False:
            cliqueEgale = True
            nombre2 = float(affichage.get())
    
        # Verifie s'il y a division par 0.
        if (operation != "/" or nombre2 != 0):
            boutonRAZ()
            resultat = eval(str(nombre1) + operation + str(nombre2))
            nombre1 = resultat
            # Si le resultat est un entier, on affiche l'opération sans virgule
            # Sinon on affiche l'operation avec la virgule
            if  resultat == int(resultat):
                affichage.insert(0, str(int(resultat)))
            else:
                affichage.insert(0, str(resultat))

def boutonVirgule():
    if affichage.get().find(".") == -1:
        affichage.insert(END, ".")

def quitter():
    root.quit()

def clavier(event):
    touche = event.keysym
    print(touche)
    if touche == "1": boutonClick(1)
    if touche == "2": boutonClick(2)
    if touche == "3": boutonClick(3)
    if touche == "4": boutonClick(4)
    if touche == "5": boutonClick(5)
    if touche == "6": boutonClick(6)
    if touche == "7": boutonClick(7)
    if touche == "8": boutonClick(8)
    if touche == "9": boutonClick(9)
    if touche == "0": boutonClick(0)
    if touche == "c": boutonRAZ()
    if touche == "plus": boutonOperation("+")
    if touche == "minus": boutonOperation("-")
    if touche == "slash": boutonOperation("/")
    if touche == "asterisk": boutonOperation("*")
    if touche == "equal" or touche == "Return": boutonEgale()
    if touche == "comma" or touche == "period": boutonVirgule()

# Programme principal
# Solution avec création des boutons selon un dico défini.
# dico contenant tout les parametres
# (row, col, padx, pady, colspan, sticky, fonction)
# (padx, pady, fonction, row, col, colspan, sticky)
dicoBoutons = {
    "1": (40, 20, "lambda db = db: boutonClick(int(db))", 3, 0, 1, EW),
    "2": (40, 20, "lambda db = db: boutonClick(int(db))", 3, 1, 1, EW),
    "3": (40, 20, "lambda db = db: boutonClick(int(db))", 3, 2, 1, EW),
    "4": (40, 20, "lambda db = db: boutonClick(int(db))", 2, 0, 1, EW),
    "5": (40, 20, "lambda db = db: boutonClick(int(db))", 2, 1, 1, EW),
    "6": (40, 20, "lambda db = db: boutonClick(int(db))", 2, 2, 1, EW),
    "7": (40, 20, "lambda db = db: boutonClick(int(db))", 1, 0, 1, EW),
    "8": (40, 20, "lambda db = db: boutonClick(int(db))", 1, 1, 1, EW),
    "9": (40, 20, "lambda db = db: boutonClick(int(db))", 1, 2, 1, EW),
    "0": (40, 20, "lambda db = db: boutonClick(int(db))", 4, 1, 1, EW),
    "+": (40, 20, "lambda db = db: boutonOperation(db)", 4, 3, 1, EW),
    "-": (40, 20, "lambda db = db: boutonOperation(db)", 3, 3, 1, EW),
    "*": (40, 20, "lambda db = db: boutonOperation(db)", 2, 3, 1, EW),
    "/": (40, 20, "lambda db = db: boutonOperation(db)", 1, 3, 1, EW),
    "=": (185, 20, "boutonEgale", 5, 0, 4, EW),
    "C": (40, 20, "boutonRAZ", 4, 0, 1, EW),
    ",": (40, 20, "boutonVirgule", 4, 2, 1, EW),
    "Exit": (20, 10, "quitter",6, 0, 4, None)}

for db in dicoBoutons:
    tk.Button(root, text = db, padx = dicoBoutons[db][0], pady = dicoBoutons[db][1], command = eval(dicoBoutons[db][2])).grid(row = dicoBoutons[db][3], column = dicoBoutons[db][4], columnspan = dicoBoutons[db][5], sticky = dicoBoutons[db][6])

# Solution simple sans dico
# tk.Button(root, text="1", padx=40, pady=20, command=lambda: boutonClick(1)).grid(row=3, column=0, sticky=EW)
# tk.Button(root, text="2", padx=40, pady=20, command=lambda: boutonClick(2)).grid(row=3, column=1, sticky=EW)
# tk.Button(root, text="3", padx=40, pady=20, command=lambda: boutonClick(3)).grid(row=3, column=2, sticky=EW)
# tk.Button(root, text="4", padx=40, pady=20, command=lambda: boutonClick(4)).grid(row=2, column=0, sticky=EW)
# tk.Button(root, text="5", padx=40, pady=20, command=lambda: boutonClick(5)).grid(row=2, column=1, sticky=EW)
# tk.Button(root, text="6", padx=40, pady=20, command=lambda: boutonClick(6)).grid(row=2, column=2, sticky=EW)
# tk.Button(root, text="7", padx=40, pady=20, command=lambda: boutonClick(7)).grid(row=1, column=0, sticky=EW)
# tk.Button(root, text="8", padx=40, pady=20, command=lambda: boutonClick(8)).grid(row=1, column=1, sticky=EW)
# tk.Button(root, text="9", padx=40, pady=20, command=lambda: boutonClick(9)).grid(row=1, column=2, sticky=EW)
# tk.Button(root, text="0", padx=40, pady=20, command=lambda: boutonClick(0)).grid(row=4, column=1, sticky=EW)
# tk.Button(root, text="+", padx=40, pady=20, command=lambda: boutonOperation("+")).grid(row=4, column=3, sticky=EW)
# tk.Button(root, text="-", padx=40, pady=20, command=lambda: boutonOperation("-")).grid(row=3, column=3, sticky=EW)
# tk.Button(root, text="*", padx=40, pady=20, command=lambda: boutonOperation("*")).grid(row=2, column=3, sticky=EW)
# tk.Button(root, text="/", padx=40, pady=20, command=lambda: boutonOperation("/")).grid(row=1, column=3, sticky=EW)
# tk.Button(root, text="=", padx=185, pady=20, command=boutonEgale).grid(row=5, column=0, columnspan=4, sticky=EW)
# tk.Button(root, text="C", padx=40, pady=20, command=boutonRAZ).grid(row=4, column=0, sticky=EW)
# tk.Button(root, text=",", padx=40, pady=20, command=boutonVirgule).grid(row=4, column=2, sticky=EW)
# tk.Button(root, text="Exit", padx=20, pady=10, command=quitter).grid(row=6, column=0, columnspan=4)

# Gestions d'événements
root.bind("<Control-C>", quit)
root.bind("<Button-2>", quit, add="+")
root.bind("<F1>", quit, add="+")
root.bind("<Key>", clavier, add="+")

root.mainloop()