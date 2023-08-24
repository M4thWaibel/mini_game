import Adivinha
import Forca

print("**********************************")
print("******* Escolha o Jogo! **********")
print("**********************************\n")

print(" [1] - Adivinha \n [2] - Forca")

opção = int(input("\nQual jogo deseja jogar: "))

if(opção == 1):
    print("\n")
    Adivinha.Jogar()
elif(opção == 2):
    print("\n")
    Forca.Jogar()
else:
    print("ERROR")