preco = float(input("Informe o preco do produto: "))

opcao = int(input("Informe opcao de pagto: "))

novoPreco = 0.0
if opcao == 1:
    print("Recebeu desconto de 10%")
    novoPreco = preco * 0.9
elif opcao == 2:
    print("Recebeu desconto de 5%")
    novoPreco = preco * 0.95
elif opcao == 3:
    novoPreco = preco
else:
    print("Recebeu aumento de 7%")
    novoPreco = preco * 1.07

    print("Voce vai pagar {}", novoPreco)