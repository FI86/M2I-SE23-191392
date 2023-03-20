# Exercice 1
# Soit une chaîne de caractères comprenant,
# trois champs séparés par des caractères ‘--’ , 
# comprenant à son tour trois champs séparés par des caractères ';' 
# (un numéro d’étudiant, un nom et un prénom). 
# Faites un algorithme qui retourne un dictionnaire dont les clés
# sont les numéros d’étudiants et les valeurs sont, pour chaque 
# numéro d’étudiant, une chaîne correspondant à la concaténation des 
# prénom et nom de la personne.

# 213615200;BESNIER;JEAN--213565488;DUPOND;MARC--214665555;DURAND;JULIE

def main():
    ch = "213615200;BESNIER;JEAN--213565488;DUPOND;MARC--214665555;DURAND;JULIE"
    dico = {}
    etudiant = ch.split("--")

    infos_etudiant0 = etudiant[0].split(";")
    infos_etudiant1 = etudiant[1].split(";")
    infos_etudiant2 = etudiant[2].split(";")

    dico[infos_etudiant0[0]] = infos_etudiant0[2] + " " + infos_etudiant0[1]
    dico[infos_etudiant1[0]] = infos_etudiant1[2] + " " + infos_etudiant1[1]
    dico[infos_etudiant2[0]] = infos_etudiant2[2] + " " + infos_etudiant2[1]

    print(dico)

if __name__ == "__main__":
    main()