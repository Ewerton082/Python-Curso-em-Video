# Separar os Digitos de um numero

numero = input('Digite um número: ')
numero_BR = numero.replace(numero,'000'+numero)

print(f'Unidade: {numero_BR[-1]}')
print(f' Dezena: {numero_BR[-2]}')
print(f'Centena: {numero_BR[-3]}')
print(f' Milhar: {numero_BR[-4]}')