# Mostrar Média do Aluno

notas = list()

for nota in range(1, 5):
    valor = float(input(f"Qual a {nota}ª Nota: ").replace(',','.'))
    notas.append(valor)

print(f" A média das notas {notas} é : {sum(notas) / len(notas)}")