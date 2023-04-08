import random

sorteado = random.randint(1, 1001)
#print(sorteado)
tentativas = 1
chute = int(input("Tentativa: "))

while chute != sorteado:
    if chute < sorteado:
        print("Tente um número maior!")
    elif chute > sorteado:
        print("Tente um número menor!")
    chute = int(input("Tentativa: "))
    tentativas = tentativas + 1

print("Parabéns, você acertou!")
print(tentativas, " chutes")