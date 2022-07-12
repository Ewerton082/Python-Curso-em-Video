# Analizar Triangulos

while True:
    try:
        a1 = float(input("Digite Aqui o \033[95mPrimeiro\033[m Segmento: "))
        while True:
            try:
                a2 = float(input("Digite Aqui o \033[95mSegundo\033[m Segmento: "))
                while True:
                    try:
                        a3 = float(input("Digite Aqui o \033[95mTerceiro\033[m Segmento: "))
                        break
                    except:
                        print('\033[91m Digite Um Valor Válido\033[m')
                break
            except:
                print('\033[91m Digite Um Valor Válido\033[m')
        break
    except:
        print('\033[91m Digite Um Valor Válido\033[m')

if a1 > a2 + a3 and a2 > a1 + a3 and a3 > a1 + a2:
    print("É Possivel \033[92mSim\033[m Formar um Triângulo com Estes Angulos")
else:
    print("\033[91mNão\033[m é Possivel Formar um Triãngulo")
