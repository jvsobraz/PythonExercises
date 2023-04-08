soma = 0
divisor = 1

num = int(input("Informe o número: "))

while divisor < num:
    if num % divisor == 0:
        soma = soma + divisor
    divisor = divisor + 1

if soma == num:
    print(num, "é perfeito")
else:
    print(num, "não é perfeito")