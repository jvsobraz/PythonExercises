n = int(input("Qual numero de Fibonacci voce quer: "))

anterior = 1
atual = 1

if n <= 2:
    print(1)
else:
    i = 3
    while i <= n:
        proximo = atual + anterior
        anterior = atual
        atual = proximo
        i = i + 1

print(atual)