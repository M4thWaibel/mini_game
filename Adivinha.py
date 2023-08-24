

def Jogar():

    import random

    print("**********************************")
    print("********** Adivinha! *************")
    print("**********************************\n")

    Número_Sorteado = random.randrange(1, 101)
    # print(Número_Sorteado)
    # print("\n")
    Pontos = 100

    print("Qual dificuldade deseja jogar?")
    print("[1]-Facil  [2]-Medio  [3]-Dificil")
    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        Tentativas = 20
    elif(nivel == 2):
        Tentativas = 10
    else:
        Tentativas = 5

    Rodada = Tentativas

    Tentativas = 0

    while(Rodada > 0):
        Tentativas+=1
        chute_str = input("Digite um numero: ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if(chute <= 0 or chute > 100):
            print("Valor invalido, por favor chute um numero entre 0 e 100")
            continue
        elif(chute == Número_Sorteado):
            print("Voce acertou!!")
            print("Voce acertou em {} tentativas".format(Tentativas))
            print("Voce fez um total de {} pontos".format(Pontos))
            break
        elif(chute > Número_Sorteado):
            print("Voce errou, tente um numero mais baixo!")
            Rodada -= 1
            pontos_perdidos = 5 * nivel
            Pontos -= (pontos_perdidos)
        else:
            print("Voce errou, tente um numero mais alto!")
            Rodada -= 1
            pontos_perdidos = 5 * nivel
            Pontos = Pontos - (pontos_perdidos)
        
        if(Rodada == 0):
            Pontos = 0
            print("Suas chances acabaram, o numero secreto era {} ".format(Número_Sorteado))
            print("Pontuação Final: ", Pontos )
            break

    print("Fim de Jogo")

if(__name__ == "__main__"):
    Jogar()