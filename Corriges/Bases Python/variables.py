# Fichier d'exemples pour les variables

# DECLARER UNE VARIABLE ET L'INITIALISER
# Integer
a = 5
print("a =", a)

# Float
b = 3.7
print("b =", b)

# Boolean
c = True
print("Boolean =", c)

# Incrementation
a = a + 1
a += 1

# Assignation paralleles et réaffection dynamique de c
c, d = 3, "ma valeur d"
print("mes valeurs paralleles =", c, d)

# Echange
c, d = d, c
print(c, d)

# Assignation multiple
e = f = 5
print("mes valeurs multiples =", e, f)

# String
g = "ma chaine de caractères"
print("ma string = ", g)

# String multiligne
chaine = "une chaine de caractères tres \
très longue"
print("machaine =", chaine)

# Avec \n
print("mon texte \nmon deuxieme texte")

# La re-declaration des variables est possible
a = "5"
print("a =", a)

# Obtenir le type d'une variable
print("type de a = ", type(a))

# Caster
print("int a =", int(a))
print(type(a))
a = int(a)
print(type(a))

# Erreur: Les variables des types différents ne peuvent être combinées
# print("str a = " + a) # erreur de conatenation car a n'est pas str
print("str a = " + str(a))

# OPERATION SUR LES STRING
# Concatenation
texte1 = "mon premier texte "
texte2 = "Mon deuxieme texte"
texte = texte1 + texte2
print(texte)

# Longueur de la chaine
print("longueur texte =", len(texte))

# Remplacer un element dans le texte
print(texte.replace(" ", "-"))

# Split Chaine
print(texte.split("mon"))

# Mettre texte en majuscule
print(texte.upper())

# Mettre texte en miniscule
print(texte.lower())

# Mettre en majuscule la première lettre de la phrase de texte
print(texte.capitalize())

# Mettre à texte une majuscule à chaque début de mot
print(texte.title())

# Inverser une chaine de caractère
print(texte[::-1])