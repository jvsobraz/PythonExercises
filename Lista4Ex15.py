n = int(input("Informe tamanho da sequência: "))

#leio o primeiro numero da sequencia fora do while
#estou supondo que n > 0, ou seja, existe pelo menos 1 numero na sequencia

num = int(input("Num: "))

maximo = 1
contadorMaximo = 1
contadorSequencia = 1
anterior = num

while contadorSequencia < n:
    num = int(input("Num: "))
    if num > anterior:
        contadorMaximo = contadorMaximo + 1
    else:
        if maximo < contadorMaximo:
            maximo = contadorMaximo
        contadorMaximo = 1
    anterior = num
    contadorSequencia = contadorSequencia + 1

print("O segmento crescente máximo tem tamanho", maximo)