num = int(input("Informe o numero: "))

numOriginal = num
resp = 0

while num != 0:
    d = num % 10
    num = num // 10
    resp = resp * 10 + d

if numOriginal == resp:
    print("É palíndrome")
else:
    print("Não é palíndrome")