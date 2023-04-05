dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

dataValida = True

if dia < 1 or dia > 31 or mes < 1 or mes > 12: #DATAS INEXISTENTES
    dataValida = False

if dia == 31 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Entrou aqui")
    dataValida = False

if mes == 2 and dia > 28:
    if dia == 29:
    #aqui vamos verificar se o ano e bissexto
        if ano % 4 != 0:
            dataValida = False
        elif ano % 100 == 0 and ano % 400 != 0:
            dataValida = False

    else: #situacao para os dias 30 e 31 de fevereiro
        dataValida = False


#if dataValida == True:
if dataValida:
    print("Data valida")
else:
    print("Data invalida")