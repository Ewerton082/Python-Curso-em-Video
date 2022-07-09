import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")

requisicao_dic = requisicao.json()

cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
cotacao_euro = float(requisicao_dic['EURBRL']['bid'])

real = str(input('Digite aqui seu valor em Real R$:')).replace(',', '.')
real = float(real)

print(f'''
{real:.2f} R$ Equivale á

{real / cotacao_dolar:.2f} $ em Dólar
{real / cotacao_euro:.2f} € em Euro''')
