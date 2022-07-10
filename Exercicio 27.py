# Mostrar o primeiro e ultimo nome de uma pessoa

nome = str(input("Qual o seu Nome? ").strip())
nome_separado = nome.split()

print(f'Primeiro Nome: {nome_separado[0]}')
print(f'Ultimo Nome: {nome_separado[-1]}')

print('Fim Do programa, adeus {}.'.format(nome_separado[0]))
