# Exercice 12
# Utilisez https://regex101.com pour faire des tests.

import re
chaine = "Retrouvez tous les mots dans une chaine de Caracteres"

# 1 - Retrouvez tous les mots dans une chaine de caractères.
def mots(chaineTest):
    modele = r"\w+"
    return re.findall(modele, chaineTest)

# 2 – Retrouver tous les mots qui se terminent par un caractère donné.
def motsTerminePar(c, chaineTest):
    modele = r"\w*\B" + c
    return re.findall(modele, chaineTest)

# 3 – Retrouver tous les mots qui commencent par un caractère donné.
def motCommencePar(c, chaineTest):
    modele = r"\b[" + c.upper() + c.lower() + r"][a-zA-Z]+\b"
    return re.findall(modele, chaineTest)

# 4 - Retrouver tous les mots qui contiennent au moins trois caractères.
def motContientUnCaractere(chaineTest):
    modele = r"\b\w{3,}"
    return re.findall(modele, chaineTest)

# 5 - Retrouver tous les mots qui possèdent exactement n caractères.
def motPossedeNCaractere(n, chaineTest):
    modele = r"\b\w{" + str(n) + r"}\b"
    modele = fr"\b\w{{{n}}}\b"
    return re.findall(modele, chaineTest)
    
if __name__ == "__main__":
    print("1 -", mots(chaine))
    print("-" * 20)
    print("2 -", motsTerminePar("s", chaine))
    print("-" * 20)
    print("3 -", motCommencePar("c", chaine))
    print("-" * 20)
    print("4 -", motContientUnCaractere(chaine))
    print("-" * 20)
    print("5 -", motPossedeNCaractere(4, chaine))