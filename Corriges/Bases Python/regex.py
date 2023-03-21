# Fichier d'exemples de regex.
import re

# Utilisation.
texte = "Je m'appel Paul"
print("Paul" in texte)
resultat = re.findall(r"kevin\d+", texte)
print(resultat)

texte = "Je m'appelle Paul Paul33 Paul444 Paul9"
modele = r"Paul[0-9]+"
resultat = re.findall(modele, texte)
print(resultat)

# Reconnaitre un email.
# Test si l'email saisi est ok.
chaine = input("Saisir un email : ")
modele = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net|fr)"
if(re.search(modele, chaine)): print("Email valide")
else: print("Email non valide")

# Trouver toutes les dates.
texte = "On est le 15-03-2022 ou le 16/03/2022."
# Modèle simple
modele = r"\d{2}-\d{2}-\d{4}"
# Modèle amélioré
modele = r"\b\d{2}(?:-|/)\d{2}(?:-|/)\d{4}\b"
c = re.compile(modele)
print(c.findall(texte))

# Rechercher une chaîne de caractères comportant une lettre a suivi de zéro ou plusieurs lettre b.
def correspondanceTexte(texte):
    modeles = r"ab*"
    if re.search(modeles,  texte):
        return "Correspond !"
    else:
        return "Correspond pas !"

print(correspondanceTexte("bc"))
print(correspondanceTexte("ac"))
print(correspondanceTexte("abc"))
print(correspondanceTexte("abbc"))

# Suppression des zéros de tête d'une adresse IP.
ip = "006.008.094.196"
modele = r"\b0+(\d)"
resultat = re.sub(modele, r"\1", ip)
print(resultat)

# Trouver un mot dans une chaine de caractères.
texte = "Python exercices, PHP exercices, C# exercices"
modele = "exercices"
for match in re.findall(modele, texte):
    print(f"Trouvé : {match}")

# Vérifier qu'une chaîne de caractères ne contient qu'un certain ensemble
# de caractères (dans ce cas, a-z, A-Z et 0-9).
def caracteresAutorise(chaine):
    c = re.compile(r"[^a-zA-Z0-9]")
    resultat = c.search(chaine)
    return not bool(resultat)

print(caracteresAutorise("ABCDEFabcdef123450")) 
print(caracteresAutorise("*&%@#!}{"))

# Vérifier qu'une chaîne de caractères ne contient que des lettres majuscules,
# minuscules, des chiffres et des caractères de soulignement.
def correspondanceTexte2(chaine):
    modeles = r"^[a-zA-Z0-9_]*$"
    # Modèle simplifié avec le token \w
    modeles = r"^\w*$"
    if re.search(modeles, chaine):
        return "Correspond !"
    else:
        return "Correspond pas !"

texte = "Le renard est dans le poulailler !"
print(correspondanceTexte2(texte))
print(correspondanceTexte2("Exercice_Python_1"))

# Rechercher certaines chaînes littérales dans une chaîne de caractères.
modeles = ["renard", "poulailler", "cheval"]

for modele in modeles:
    if re.search(modele, texte):
        print(f"{modele} dans {texte} -> Trouvé !")
    else:
        print(f"{modele} dans {texte} -> Pas trouvé !")

# Insérer des espaces entre les mots commençant par une majuscule.
def espace_mot_capitale(chaine):
    modele = r"(\w)([A-Z])"
    separe_groupe = r"\1 \2"
    return re.sub(modele, separe_groupe, chaine)

print(espace_mot_capitale("Python"))
print(espace_mot_capitale("PythonExercices"))
print(espace_mot_capitale("PythonExercicesSolutionPossible"))

