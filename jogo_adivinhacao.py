import random

print("jogo de adivinhação")
nivel = 0
pontuacao = 1000
tentativas = 0
numero_sorteado = random.randrange(1, 101)
valor = 0
print("o numero_sorteado foi",numero_sorteado)


print("digite o nivel de dificuldade 1 para facil, 2 para medio ou 3 para dificil")

while((nivel < 1) or (nivel > 3)):
    nivel = int(input("qual o nivel voce escolhe?"))
    if nivel == 1:
        print("voce escolheu o nivel facil")
        tentativas = 20
        print("voce tem", tentativas)
    elif nivel == 2:
        print("voce escolheu o novel medio")
        tentativas = 10
        print("voce tem", tentativas)
    elif nivel == 3:
        print("voce escolheu o nivel dificil")
        tentativas = 5
        print("voce tem", tentativas)
    else:
        print("voce deve escolher 1, 2 ou 3")

while tentativas > 0:
    print("voce tem ", tentativas)
    valor = int(input("digite o valor"))
    if valor == numero_sorteado:
        print("voce acertou")
        break
    elif valor > numero_sorteado:
        print("o numero secreto é menor do que", valor)
        tentativas = tentativas - 1
    elif valor < numero_sorteado:
        print("o numero secreto é maior do que", valor)
        tentativas = tentativas - 1
else:print("voce perdeu, acabou as tentativas")


