# Exercice 5
# Écrivez un programme qui convertisse en mètres par seconde une vitesse
# fournie par l’utilisateur en Km/h
# Demander à l’utilisateur de rejouer.
# « Voulez-vous rejouer ? » Réponse possible oui ou non

def main():
    reponse = ""

    while reponse.upper() != "NON":
        valeur = input("Indiquer vitesse en Km/h : ")
        print(f"la vitesse en m/s est : {float(valeur) / 3.6}")
        reponse = input("Voulez-vous rejouer ? ")

if __name__ == "__main__":
    main()