# Fichier d'exemples d'accès à une BDD
import sqlite3
import os

# Chemin et fichier
chemin = os.path.dirname(__file__)
fichier = os.path.join(chemin, "BDD.db")

# Liaison avec la BDD
# Le fichier n'exite pas au debut, il sera creer automatiquement.
connection = sqlite3.connect(fichier)

# Liaison avec la connection
cursor = connection.cursor()

# Requete de creation d'une table
cursor.execute("CREATE TABLE IF NOT EXISTS Utilisateurs (Nom TEXT, Age INT, Taille DOUBLE)")
connection.commit()

# Requete d'insertion dans une table
cursor.execute("INSERT INTO Utilisateurs VALUES ('Toto', 18, 170)")
connection.commit()

# Lire le contenu de la table Utilisateurs
# Requete de séléction de toutes les donnees
cursor.execute("SELECT * FROM Utilisateurs")
enr = cursor.fetchall()

# Affichage des infos lues en BDD
print(enr)

for e in enr:
    print(e)

# Lecture BDD avec une selection (WHERE)
# Requete de selection de donnees (attention à la casse de la variable)
nom = "Toto"
cursor.execute(f"SELECT * FROM Utilisateurs WHERE nom = '{nom}'")
# fetchone affiche le premier element de la liste retournée par le curseur
# et pointe sur le suivant au prochain fetchone s'il exite.
# S'il n'existe pas, cela retourne None.
# L'execution d'un nouveau execute() reinitialitise la position du curseur
# au début des enregistrements disponible.
r = cursor.fetchone()
print(r)
r = cursor.fetchone()
print(r)

cursor.execute(f"SELECT * FROM Utilisateurs WHERE nom = '{nom}'")
r = cursor.fetchone()
print(r)
r = cursor.fetchone()
print(r)

# Fermeture des liaisons du curseur et de la connection.
cursor.close() # Pas obligatoire sauf pour changer vers une autre connection
connection.close()