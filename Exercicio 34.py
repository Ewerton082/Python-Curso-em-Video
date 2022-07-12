# Aumento de salarios

while True:
    try:
        salario = float(input("Quanto você Recebe de sálario? ").strip().replace(',', '.'))

        if salario <= 1250.00:
            print(f"O seu sálario antes era {salario:.2f}R$ e agora é : {salario + (salario * 0.15)} R$")

        else:
             print(f"O seu sálario antes era {salario:.2f}R$ e agora é : {salario + (salario * 0.10)} R$")
        
        break

    except:
        print("Digite um Valor Válido!")
