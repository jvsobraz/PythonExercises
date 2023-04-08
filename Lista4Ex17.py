num = float(input("Informe o numero: "))

aproximacao = 0

while aproximacao * aproximacao < num:
    aproximacao = aproximacao + 0.001

print("A raiz quadrada de ", num, "é", aproximacao)