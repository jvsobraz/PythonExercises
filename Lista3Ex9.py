import math

aux = input("Digite a: ")

a = float(aux)
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = b * b - 4 * a * c

if delta < 0:
    print("A equacao nao possui raizes reais")
else:
    raiz1 = -b + math.sqrt(delta)
    raiz1 = raiz1 / (2 * a)

    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    print("Raiz 1", raiz1)
    print("Raiz 2", raiz2)