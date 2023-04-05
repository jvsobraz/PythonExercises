import math

# coloque aqui o resto do seu codigo
# tudo na frente do sustenido eh
# considerado um comentario em Python
numero = float(input("Digite um numero: "))
if numero < 0:
    print("Numero negativo. Impossivel calcular raiz quadrada")
else:
    resultado = math.sqrt(numero)
    print("Raiz quadrada de ", numero, " e ", resultado)
