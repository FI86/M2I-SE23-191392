# Exercice 4
chaine = "Retrouvez tous les mots dans une chaine de caractères"

# 1 - Retrouvez tous les mots dans une chaine de caractères sous forme de liste
print(chaine.split())
print("-" * 20)

# 2 – Retrouver tous les mots qui se terminent par un caractère donné
listeChaine = chaine.split()

for mot in listeChaine:
    if mot.endswith("s"):
        print(mot)

print("-" * 20)

# 3 – Retrouver tous les mots qui commencent par un caractère donné
for mot in listeChaine:
    if mot.startswith("c"):
        print(mot)

print("-" * 20)

# 4 - Retrouver tous les mots qui contiennent au moins 4 caractères
for mot in listeChaine:
    if len(mot) >= 4:
        print(mot)

print("-" * 20)

# 5 - Retrouver tous les mots qui possèdent exactement n caractères.
n = 4

for mot in listeChaine:
    if len(mot) == n:
        print(mot)