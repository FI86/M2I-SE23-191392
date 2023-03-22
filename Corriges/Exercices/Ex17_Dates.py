# Exercice 17
# Écrivez un script qui calcule combien de jours avant le prochain poisson d'avril ?
from datetime import date

def main():
    aujoudhui = date.today()
    avril = date(aujoudhui.year, 4, 1)

    if avril < aujoudhui: avril = date(aujoudhui.year + 1, 4, 1)

    print(f"Date du prochain poisson d'avril : {avril.day:>02d}/{avril.month:>02d}/{avril.year}")
    print(f"Nombre de jours avant le prochaine poisson d'avril : {(avril - aujoudhui).days}")

    print("_" * 40)
    input("Appuyer sur <Entrée> pour terminer !")

    
if __name__ == "__main__":
    main()