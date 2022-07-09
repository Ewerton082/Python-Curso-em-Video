# Calcular Seno Cosseno e Tangente 

def cos_sen_tan(grau=0):
    """
    --> Está função irá retornar um pequeno texto mostrando
     o Seno, Cosseno e a Tangente do angulo em Graus
    :param grau: o grau do ángulo no formato int()
    :return: uma str() com as informações colocadas em cima
    """
    from math import cos, tan, sin, degrees

    print(f'''
     Cosseno de {grau}° é : {cos(degrees(grau)):.2f}
        Seno de {grau}° é : {sin(degrees(grau)):.2f}
    Tangente de {grau}° é : {tan(degrees(grau)):.2f}''')


num = int(input('Quantos Graus é o ângulo: ').strip())
cos_sen_tan(num)