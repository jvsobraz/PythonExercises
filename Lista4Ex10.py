n = int(input("Informe n: "))

fatorial = 1

while n > 0:
    fatorial = fatorial * n
    n = n - 1

print("O fatorial vale {}".format(fatorial))