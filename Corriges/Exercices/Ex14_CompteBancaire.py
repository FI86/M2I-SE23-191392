# Exercice 14a
# Définissez une classe CompteBancaire(), qui permette d’instancier des objets tels que compte1, 
# compte2, etc. 
# Le constructeur de cette classe initialisera deux attributs d’instance nom et solde, avec les 
# valeurs par défaut ’Dupont’ et 1000. 
# Trois autres méthodes seront définies : 
# • depot(somme) permettra d’ajouter une certaine somme au solde ; 
# • retrait(somme) permettra de retirer une certaine somme du solde ; 
# • affiche() permettra d’afficher le nom du titulaire et le solde de son compte.

class CompteBancaire():
    """Compte Bancaire"""
    def __init__(self, nom = "Dupont", solde = 1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme
    
    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print(f"Nom : {self.nom}")
        print(f"Solde : {self.solde}")
 

def main():
    cb1 = CompteBancaire()
    cb2 = CompteBancaire(solde = 5000, nom = "yop")
    cb2 = CompteBancaire("yop", 5000)
    cb1.affiche()
    cb2.affiche()
    cb1.depot(1500)
    cb2.retrait(550)
    cb1.affiche()
    cb2.affiche()

    print("_" * 40)
    input("Appuyer sur la touche <Entrée> pour fermer")

if __name__ == "__main__":
    main()