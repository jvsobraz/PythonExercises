
somaPar = 0
num = int(input("Informe num da sequência"))

while num != 0:
    if num % 2 == 0:
        somaPar = somaPar + num
    num = int(input("Informe num da sequência"))

print("A soma dos pares é {}".format(somaPar))