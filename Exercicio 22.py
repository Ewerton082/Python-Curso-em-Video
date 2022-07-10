# Analizar o Nome de uma pessoa

nome = str(input("Digite aqui seu nome completo: ").strip())

print(f"Nome em Maíusculo: {nome.upper()}")

print(f"Nome sem Espaços: {nome.replace(' ', '')}")

separado_nome = nome.split()

print(f"Seu Primeiro Nome: {separado_nome[0]}")
