# Fichier d'exemples de géomertrie Tkinter
from tkinter import E, S, W, EW, Tk, ttk, BOTH, Label
root = Tk()

# Taille fenetre x*y + posx + posy par rapport à l'écran
root.geometry("640x480+200+200")

# Geometry
# Pack
# justify fonctionne lorsqu'il y a plusieurs ligne dans le label, anchor pour une seule ligne.
# Label centre le texte par defaut, ttk.Label aligne à gauche par defaut.
Label(root, text = 'Hello, Tkinter!', background = 'blue', ancho = W).pack(fill = BOTH, expand = True)
ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow', anchor = E).pack(fill = BOTH, expand = True)
label = ttk.Label(root, text = 'Hello, Tkinter!',background = 'green', anchor = S)
label.pack(fill = BOTH, expand = True)

# Grid
ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 0, sticky=EW)
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 0, column = 1, sticky=EW)
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 1, column = 0, sticky=EW)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 1, column = 1, sticky=EW)

# Place
# (Si besoin de la position exacte)
# ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)


root.mainloop()