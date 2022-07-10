# Ver se o nome escritopelo usuário tem 'Silva'

nome = str(input("Qual seu nome Completo? ").strip().lower())
nome_sep = nome.split()

for ordem, nome in enumerate(nome_sep):
    if nome == 'silva':
        print(f"O seu {ordem + 1}º Nome é \033[92mSilva\033[m")
        break
    
    elif ordem == len(nome_sep) - 1 and nome != 'silva':
        print('Infelizmente não há \033[91mSilva\033[m em seu nome')
