timeCasa = input("Time da casa:")
timeVisitante = input("Time visitante:")
golCasa = int(input("Gols da casa:"))
golVisitante = int(input("Gols do visitante:"))

if golCasa > golVisitante:
    print("Time da casa venceu!")
elif golCasa < golVisitante:
    print("Time visitante venceu!")
else:
    print("Houve empate")

print(timeCasa," ",golCasa," X ",golVisitante," ",timeVisitante)