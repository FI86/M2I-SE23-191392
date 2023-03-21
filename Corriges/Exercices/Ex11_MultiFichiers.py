# Exercice 11
# À partir de deux fichiers préexistants A et B, construisez un fichier C 
# qui contienne alternativement un élément de A, un élément de B, un élément de A... 
# et ainsi de suite jusqu’à atteindre la fin de l’un des deux fichiers originaux. 
# Complétez ensuite C avec les éléments restant sur l’autre.

import os

def main():
   chemin = os.path.dirname(__file__)
   
   # Solution 1
   # listeC = []
   # elemA = ""
   # elemB = ""
   # elem = 0

   # with open(chemin + "/a.txt", "rt") as fa:
   #    listeA = fa.readlines()

   # with open(chemin + "/b.txt", "rt") as fb:
   #    listeB = fb.readlines()

   # while elemA != None or elemB != None:
   #    if elem < len(listeA): listeC.append(listeA[elem].strip("\n")) 
   #    else: elemA = None
      
   #    if elem < len(listeB): listeC.append(listeB[elem].strip("\n"))
   #    else: elemB = None

   #    elem += 1

   # with open(chemin + "/c.txt", "wt") as fc:
   #    for elem in listeC:
   #       fc.write(elem + "\n")

   # Solution 2
   # fa = open(chemin + "/a.txt", "rt")
   # fb = open(chemin + "/b.txt", "rt")
   # fc = open(chemin + "/c.txt", "wt")
   with  open(chemin + "/a.txt", "rt") as fa,  \
         open(chemin + "/b.txt", "rt") as fb, \
         open(chemin + "/c.txt", "wt") as fc:

      while True:
         ligneA = fa.readline().strip("\n")
         ligneB = fb.readline().strip("\n")

         if ligneA == "" and ligneB == "": break
         if ligneA != "": fc.write(ligneA + "\n")
         if ligneB != "": fc.write(ligneB + "\n")

   # fa.close()
   # fb.close()
   # fc.close()


if __name__ == "__main__":
    main()