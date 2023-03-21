# Exercice 7
# Définissez une fonction maximum(n1, n2, n3) qui renvoie le plus grand de 3 nombres n1, n2, n3 
# fournis en arguments. Par exemple, l’exécution de l’instruction :
# print(maximum(2,5,4)) doit donner le résultat : 5.

def maximum(n1, n2, n3):
    return max(n1, n2, n3)

def maximum2(n1, n2, n3):
    n = n1
    if n2 > n: n = n2
    if n3 > n: n = n3
    return n

def main():
    print(maximum(25, 20, 40))
    print(maximum2(25, 20, 40))

if __name__ == "__main__":
    main()