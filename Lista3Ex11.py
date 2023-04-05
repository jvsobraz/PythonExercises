mediaPrimSem = float(input("Primeiro semestre: "))
mediaSegSem = float(input("Segundo semestre: "))

mediaFinal = (4 * mediaPrimSem + 6 * mediaSegSem) / 10

aulasDadas = int(input("numero de aulas dadas: "))
aulasAssistidas = int(input("numero de aulas assistidas: "))

frequencia = aulasAssistidas / aulasDadas * 100

print("A media final foi de {}".format(mediaFinal))
situacao = "Aprovado"

if mediaFinal < 4 or frequencia < 70:
    situacao = "Reprovado"

if mediaFinal >= 4 and mediaFinal < 6:
    situacao = "Exame"

    print("O aluno foi ", situacao)