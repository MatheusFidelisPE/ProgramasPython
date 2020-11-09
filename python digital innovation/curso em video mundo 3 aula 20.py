#desafio 1 faça um programa que tenha uma função área, que receba as dimensões de um terreno retangular e mostre a área
#desafio 2 Programa que tenha uma função escreva que recebe um texto qualquer no parametro e mostre linhas acima e abaixo no tamano da string
#desafio 3 Programa que tenha uma função contador() que receba três parametros inicio, fim e passo. E faça tres contagens de 1 até 10 e 1 em 1, de 10 até 0 de 2 em 2 e uma contagem personalizada
#desafio 4 Programa que tenha uma função chamada maior() que recebe varios parametros e mostre quantos valores foram digitados e qual o maior valor
#desafio 5 Programa que tem uma lista e duas funções sorteia() sorteia 5 numeros e coloca na lista e somapar() que soma todos os valores pares

#                           RESOLUÇÃO
#1)
'''
def area(alt, lag):
    print(f'Temos uma profundidade igual a {alt}m e largura de {lag}m. Assim temos uma área de {alt*lag}m^2.')


altura=float(input('Informe a profundidade do retângulo: '))
largura=float(input('Informe a largura do retângulo: '))
area(altura, largura)
'''
#2)
'''
def tio(tamanho):
    (print('~~~', end='')
    print('~' * tamanho, end='')
    print('~~~', end=''))=> tamanho=len(frase)+4; print('~'*tamaho);


def escreva(txt, tamanho):
    tio(tamanho)
    print(f'\n{txt:^{(tamanho+6)}}')
    tio(tamanho)
    print()

frase='PYTHON É MUITO FORTE'
escreva(frase,len(frase))
frase='ESSE CURSO DO CURSO EM VÍDEO É MASSA!'
escreva(frase,len(frase))
frase='DEU TUDO CERTO!!'
escreva(frase,len(frase))
'''
#3)
'''
import time

def contador(inicio, fim, passo):
    passoreal=passo

    #INPRIMINDO O QUE SERÁ FEITO NA CONTAGEM
    linha()
    if passo<0:
        passo=passo.__neg__()
    print(f'CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}')
    linha()
    #IMPRIMIDO O QUE SERÁ FEITO NA CONTAGEM

    if inicio>fim and passo>0:
        passoreal=(passo.__neg__())
        fim-=1
    else:
        fim+=1
    for c in range(inicio, fim, passoreal):
        print(f'{c}...', end='')
        time.sleep(0.5)
    print()
    linha()


def linha():
    print('-='*20)


contador(1,10,1)
contador(10,0,-2)

inicio=int(input('INÍCIO: '))
fim=int(input('FIM: '))
passo=int(input('PASSO: '))
contador(inicio,fim,passo)
'''
#4)
'''
def maior(lista):
    print(f'Foram digitados {len(lista)} números e o maior foi {max(lista)}')


lista=list()
while True:
    numero=int(input('Informe o número: '))
    saida=str(input('Deseja sair[S/N]? '))
    lista.append(numero)
    if saida in 'Ss':
        break
maior(lista)
'''
#5)
'''
from random import randint
from time import sleep
def somapar(lista):
    soma=0
    for c in lista:
        if c%2==0:
            soma+=c
    print(f'Na lista sorteada temos {soma} como o valor da soma dos pares.')
    print('\r')

def aleatorio(lista):
    for c in range(0,5):
        num=randint(1,10)
        lista.append(num)
    print('TEMOS COMO LISTA TOTAL OS VALORES (', end='')
    for c in lista:
        print(f'{c}...',end='')
        sleep(0.5)
    print(')\r')

lista= list()
aleatorio(lista)
somapar(lista)
'''







