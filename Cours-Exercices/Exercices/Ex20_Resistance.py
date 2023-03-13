# Exercice 20
# Notre application doit faire apparaître une fenêtre comportant un dessin de la résistance,
# ainsi qu’un champ d’entrée dans lequel l’utilisateur peut encoder une valeur numérique. 
# Un bouton <Montrer> déclenche la modification du dessin de la résistance, de telle façon que 
# les trois bandes de couleur se mettent en accord
# avec la valeur numérique introduite. 
# Contrainte : Le programme doit accepter toute entrée numérique fournie sous forme entière ou réelle, 
# dans les limites de 10 à 1e11 Ω. Par exemple, une valeur telle que 4.78e6 doit être acceptée et 
# arrondie correctement, c’est-à-dire convertie en 4800000 Ω.

# Pour rappel, la fonction des résistances électriques consiste à s’opposer 
# (à résister) plus ou moins bien au passage du courant. Les résistances 
# se présentent concrètement sous la forme de petites pièces tubulaires cerclées de 
# bandes de couleur (en général 3). Ces bandes de couleur indiquent la valeur numérique de la 
# résistance, en fonction du code suivant :
# Chaque couleur correspond conventionnellement à l’un des chiffres de zéro à neuf :
# Noir = 0, Brun = 1, Rouge = 2, Orange = 3, Jaune = 4, Vert = 5, Bleu = 6, Violet = 7, Gris = 8, Blanc = 9.
# On oriente la résistance de manière telle que les bandes colorées soient placées à gauche. 
# La valeur de la résistance – exprimée en ohms (Ω) – s’obtient en lisant ces bandes colorées 
# également à partir de la gauche : les deux premières bandes indiquent les deux premiers chiffres 
# de la valeur numérique ; il faut ensuite accoler à ces deux chiffres un nombre de zéros égal 
# à l’indication fournie par la troisième bande.
# Exemple concret : supposons qu’à partir de la gauche, les bandes colorées soient jaune, 
# violette et verte. La valeur de cette résistance est 4700000 Ω, ou 4700 kΩ, ou encore 4,7 MΩ.

def main():
    pass

if __name__ == "__main__":
    main()