# Se connecter avec un mot de passe puis ouvrir des fenêtres
"""Module d'exemple de multi fenêtrage"""

from tkinter import Tk, Button, Label, messagebox, Entry, Toplevel

def fenetre1():
    """Création de la fenêtre de test 1"""
    fen1 = Toplevel()
    fen1.transient(fen1.master)
    fen1.geometry("300x300+200+200")
    Label(fen1, text="Fenetre 1").pack()
    Button(fen1, text="Quitter", command=fen1.destroy).pack()
    fen1.bind("<Escape>", fen1.quit)

def fenetre2():
    """Création de la fenêtre de test 2"""
    fen2 = Toplevel()
    fen2.transient(fen2.master)
    fen2.geometry("200x200+800+500")
    Label(fen2, text="Fenetre 2").pack()
    Button(fen2, text="Quitter", command=fen2.destroy).pack()
    fen2.bind("<Escape>", fen2.quit)

# Fenêtre principale.
def fenetre_principale():
    """Création de la fenêtre principale"""
    root2 = Tk()
    root2.title('Fenêtre principale')
    root2.geometry('800x600+500+300')
    Label(root2, text='Le mot de passe est correct, \
Bienvenue à la fenêtre principale.', wraplength=250).pack()
    Button(root2, text="Fenetre 1", command=fenetre1).pack()
    Button(root2, text="Fenetre 2", command=fenetre2).pack()
    root2.bind("<Escape>", quit)
    root2.mainloop()

# Fenêtre de connexion
# *evenement permet de binder la fonction à un widget (demande un paramètre)
# et à la commande du bouton ok qui ne demande pas de paramètre.
def test_ok(*evenement):
    """Test du mot de passe"""
    if entry.get() == 'abc123':
        # Ferme la fenêtre de connexion.
        root1.destroy()
        # Création de la fenêtre principale.
        fenetre_principale()
    else:
        messagebox.showwarning("Attention", "Mauvais mot de passe !")

root1 = Tk()
root1.title('Fenêtre de connexion')
root1.geometry('300x150+600+200')
Label(root1, text='Veuillez saisir le mot de passe : abc123').pack()
entry = Entry(root1)
entry.bind("<Return>", test_ok)
entry.pack()
# Déterminer si le mot de passe est correct.
Button(root1, text="Ok", command=test_ok, width=15).pack(pady=5)
# Ferme la fenêtre de connexion.
Button(root1, text="Quitter", command=root1.destroy, width=15).pack(pady=5)
# Attend d'accepter la fenetre de connexion
# avant d'ouvrir la fenêtre principale.
root1.mainloop()
