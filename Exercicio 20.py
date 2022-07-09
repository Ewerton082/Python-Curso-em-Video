# Sortear a Ordem de uma lista

from random import shuffle

grupo = []

for pessoa in range(1, 5):
    while True:
        nome = str(input(f'{pessoa}ª Pessoa: '))
        if nome.isalpha:
            grupo.append(nome)
            break
        else:
            print("Dados Invalídos")

shuffle(grupo)

print("=+" * 13)

for posicao, nome in enumerate(grupo):
    print(f"A {int(posicao) + 1}ª Pessoa é {nome}")

