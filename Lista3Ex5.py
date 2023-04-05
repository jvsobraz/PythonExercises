dias = int(input("Informe dias uteis: "))
horas_trab = int(input("Informe horas trabalhadas"))
salario_hora = float(input("Salario-hora: "))

salario = horas_trab * salario_hora
jornada = dias * 8
hora_extra = 0

if horas_trab > jornada:
#tem hora-extra para calcular
    hora_extra = (horas_trab - jornada) * salario_hora / 2

print("Salario: {:.2f}".format(salario))

if hora_extra > 0:
    print("Hora-extra: {:.2f}".format(hora_extra))
print("Salario Total: {:.2f}".format(salario + hora_extra))