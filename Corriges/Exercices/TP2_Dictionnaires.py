# TP 2
# Écrire une boucle de programme qui demande à l’utilisateur d’entrer des 
# notes d’élèves. La boucle se terminera seulement si l’utilisateur entre une 
# valeur négative. Avec les notes ainsi entrées, construire progressivement une liste.
# Après chaque entrée d’une nouvelle note (et donc à chaque itération de la boucle), 
# afficher le nombre de notes entrées, la note la plus élevée, la note la plus basse, 
# la moyenne de toutes les notes (informations stockées dans un dictionnaire).

def main():
    valeur = 0
    liste = []
    dico = {}

    while valeur >= 0:
        valeur = float(input("Entrez une note : "))

        if valeur >= 0:
            liste.append(valeur)

            dico["nombreNotes"] = len(liste)
            dico["max"] = max(liste)
            dico["min"] = min(liste)
            dico["moyenne"] = float(sum(liste) / len(liste))
            
            print(f"Nombre de notes entrées : {dico['nombreNotes']}")
            print(f"Note la plus élevée : {dico['max']}")
            print(f"Note la moins élevée : {dico['min']}")
            print(f"Moyenne : {dico['moyenne']}")


if __name__ == "__main__":
    main()