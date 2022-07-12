# Calcular Anos Bissesxtos

while True:
    try:
        ano= int(input("Digite Qual ano quer saber se é \033[93mBissexto\033[m: ").strip())
        
        if ano % 4 == 0 or ano % 400 == 0:
            print(f" O ano de \033[92m{ano}\033[m foi sim Bissexto")
        else:
            print(f"O ano de \033[91m{ano}\033[m não é bissexto")
        
        break

    except:
        print("Digite um valor válido!!")
        