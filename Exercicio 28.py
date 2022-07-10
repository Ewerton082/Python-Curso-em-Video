from time import sleep
from random import randint as escolha


print('\033[93m=\033[0m\033[95m-\033[0m' * 24)
print('\033[94mPensei em um número de | 0 a 5| Tente adivinhar')
print('\033[93m=\033[0m\033[95m-\033[0m' * 24)

number = escolha(0, 5)

while True:
    try:
        jogador = int(input("Qual Número é: ").strip())
        if jogador > 5:
            print('Digite um valor válido')
        else:
            break
    except:
        print('Digite um valor válido')

print('\033[96mAnalizando...\033[0m')
sleep(.8)

if jogador == number:
    print("\033[92mParabêns Você acertou, o numero q tinha pensado era {}\033[m".format(number))
else:
    print(f"\033[91mQue pena você errou, o numero certo era {number}\033[0m")
