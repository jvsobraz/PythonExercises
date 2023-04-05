avista = float(input("Informe valor do iptu a vista: "))

parcela = float(input("Informe valor da parcela: "))

aprazo = parcela * 10

porcentual = 1 - avista / aprazo

print("O valor do desconto foi de ", porcentual * 100)