dinheiro = float(input("Montante: "))
juros = float(input("Juros: "))
tempo = int(input("Tempo aplicação: "))

while t > 0:
    dinheiro = dinheiro * (1 + juros / 100)
    t = t - 1

print("O valor final aplicado é de {:.2f}".format(dinheiro))