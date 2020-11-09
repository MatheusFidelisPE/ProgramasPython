#desafio 1 programa que tenha uma função leia_int() incluindo agora a possibilidade de digitar um numero invalido
#desafio 2 programa que tente acessar o site pudim.com.br e informe se tem capacidade de acessar o site
#desafio 3 programa que cadastra nome e idade de pessoas e guardar em um arquivo de texto

'''
def leia_int():

    while True:
        try:
            valor=int(input('informe o valor: '))
        except:
            print('ERRO: Digite um valor correto.')
        else:
            print('O valor digitado foi correto.')
            break
    return valor


def leia_float():
    while True:
        try:
            valor=float(input('Informe o valor: '))
        except:
            print('ERRO: Digite um valor correto.')
        else:
            print('Valor digitado foi correto.')
            break
    return valor


numero1 = leia_int()
numero2 = leia_float()
print(f'O valor {numero1} foi o INTEIRO e o valor {numero2} foi o REAL')
'''
'''
from requests import get
try:
    pudim=get('https://www.pudim.com.br')
except:
    print('IMPOSSIVEL')
else:
    print('ACESSIVEL')
'''
import urllib
import urllib.request
try:
    pudim=urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('IMPOSSIVEL ACESSAR')
else:
    print('POSSIVEL ACESSAR')