# Par ou Impar

while True: 
    try:
        numb = int(input("Digite um \033[94mnúmero inteiro\033[m: ").strip())
        
        if numb % 2 == 0:
            print(f"O número \033[92m{numb}\033[m é PAR!!")
            break
        else:
            print(f"O número \033[91m{numb}\033[m é IMPAR!!")
            break
    
    except:
        print('\033[91mDigite um número válido!')
