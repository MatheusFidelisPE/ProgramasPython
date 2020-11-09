import math
def leitura_float():
    valor=''

    while not (valor.isnumeric()):
        potencia = 0
        valor=str(input('INFORME O VALOR: '))
        if '.' in valor:
            potencia=len(valor)-(valor.find('.')+1)
            valor = valor.replace('.','')
        elif ',' in valor:
            potencia=len(valor)-(valor.find(',')+1)
            valor = valor.replace(',','')
        if valor.isnumeric():
            print('teste 1')
            return float(int(valor)/exponenciação(10,potencia))
        else:
            print(f'VOCÊ DIGITOU VALOR ERRADO\nDIGITE UM VALOR DO TIPO FLOAT')


def exponenciação(valor,potencia):
    if potencia==0:
        return 1
    for c in range(0,potencia-1):
        valor*=valor
    print(valor)
    return valor
