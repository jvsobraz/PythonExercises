n = int(input("Informe a qtd de números da sequência: "))
conta = 1

contaPos = 0
contaNeg = 0

while conta <= n:
    num = float(input("Informe um número da sequência: "))
    if num < 0:
        contaNeg = contaNeg + 1
    elif num > 0:
        contaPos = contaPos + 1

print("{} foi a qtd de números negativos.".format(contaNeg))
print("{} foi a qtd de números positivos.".format(contaPos))