# Analizar Menor e maior valor 

numeros = list()

for numb in range(1,4):

    while True:

        try:
            num = int(input("Digite o \033[95m{}º\033[m Número: ".format(numb).strip()))
            numeros.append(num)
            break

        except:
            print("Digite um Valor Válido\n")

print('\n')
print(f"O Maior número foi: {max(numeros)}")
print(f"O Menor número foi: {min(numeros)}")
