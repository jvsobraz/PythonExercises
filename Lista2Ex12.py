rm = int(input("Informe RM: "))

soma = 0

 #repito essas instrucoes 5 vezes
 #um para cada digito do rm
digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

print("A soma vale ", soma)