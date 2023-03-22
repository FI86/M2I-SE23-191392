# Exercice 14b
# Écrivez un nouveau script qui récupère le code de (compte bancaire) en l’important comme un module.  
# Définissez-y une nouvelle classe CompteEpargne(), dérivant de la classe CompteBancaire() importée, 
# qui permette de créer des comptes d’épargne rapportant un certain intérêt au cours du temps.
# Pour simplifier, nous admettrons que ces intérêts sont calculés tous les mois. 
# Le constructeur de votre nouvelle classe devra initialiser un taux d’intérêt mensuel par défaut 
# égal à 0,3 %. Une méthode changeTaux(valeur) devra permettre de modifier ce taux à volonté. 
# Une méthode capitalisation(nombreMois) devra : 
# • afficher le nombre de mois et le taux d’intérêt pris en compte ; 
# • calculer le solde atteint en capitalisant les intérêts composés, pour le taux et le nombre de 
# mois qui auront été choisis.

from Ex14_CompteBancaire import CompteBancaire

class CompteEpargne(CompteBancaire):
    """Compte Epargne"""

    def __init__(self, nom = "Dupont", solde = 1000, tauxMensuel = 0.3):
        super().__init__(nom, solde)
        self.tauxMensuel = tauxMensuel

    def changeTaux(self, nouveauTaux):
        self.tauxMensuel = nouveauTaux

    def capitalisation(self, nombreMois):
        print(f"Capitalisation sur {nombreMois} mois avec un taux d'interet mensuel de {self.tauxMensuel} %.")
        
        for _ in range(nombreMois):
            self.solde *= (100 + self.tauxMensuel) / 100

def main():
    ce1 = CompteEpargne()
    ce2 = CompteEpargne("yop", 5000, 0.5)
    ce1.affiche()
    ce2.affiche()
    ce2.depot(400)
    ce1.retrait(150)
    ce1.affiche()
    ce2.affiche()
    ce2.capitalisation(10)
    ce2.affiche()
    ce1.changeTaux(0.5)
    ce1.capitalisation(4)
    ce1.affiche()
    ce2.affiche()
    
if __name__ == "__main__":
    main()