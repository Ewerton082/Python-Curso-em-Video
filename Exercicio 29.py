# Radar eletronico 80KM limite maximo e multar  7,00R$ por KM ultrapassado

while True:
    try:
        kilometragem = int(input('Á quantos Km/H você estava pilotando?').strip())

        if kilometragem > 80:
            print(f'Você ultrapassou o limite de velocidade, e recebeu uma multa de \033[94m{(kilometragem - 80) * 7},00 R$\033[m')
            break
        else:
            print('Você está andando nos limites, \033[92mTenha um ótimo dia\033[m')
            break

    except:
        print('\033[91mDigite um Valor Válido\033[m')
    