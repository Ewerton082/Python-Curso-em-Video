# Custo de Viagens

while True:
    try:
        quilometros = float(input("Quantos Quilometros de distancia tem está viagem? ").replace(',', '.').strip())
        
        if quilometros >= 200:
            passagem = 0.45
            print(f"O valor total de sua viagem é: \033[95m{quilometros * passagem:.2f} R$\033[m")
            break 
        else:
            passagem = 0.50
            print(f"O valor total de sua viagem é: \033[95m{quilometros * passagem:.2f} R$\033[m")
            break 

    except:
        print('\033[91m Digite Uma Quilometragem Válida\033[m')
        