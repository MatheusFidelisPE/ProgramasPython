#desafio1 programa que tenha uma tupla totalmente preenchida de 0 a 20 e receba um valor de 0 a 20 e mostrar por extenso
#desafio2 tupla como os 20 primeiros colocados da tabela do brasileiro e mostre os 5 primeiros colocados, os ultimos 4, lista com ordem alfabetica e posição do sport
#desafio3 programa que gere cinco numeros aleatorios e guardar em uma tupla e mostrar o menor e o maior valor na tupla
#desafio4 ler programa que guarde 4 valores no teclado e guarde em uma tupla, quantas vezees apareceu o 9, em que posição apareceu o 3 e quais os numeros pares
#desafio5 programa com uma tupla unica com nomes de produtos e seus respectivos preços na sequencia no final mostre os dados em uma forma tabular
#desafio6 programa que tenha um a tupla com varias palavras e mostrar as vogais de cada palavra
#RESOLUÇÃO
#1)
'''
intervalo=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
valor=0
extenso=('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezeoito', 'dezenove', 'vinte')
while True:

    valor=int(input('INFORME O VALOR: '))
    if valor>=0 and valor<=20:
        print(extenso[valor])
        break

    if(valor<0 or valor>20):
        print('DIGITOU UM VALO INVALIDO. DIGITE ENTRE 0 E 20')
'''
#2)
'''
tabela=('palmeiras', 'flamengo', 'internacional', 'gremio', 'sao paulo', 'atletico MG', 'atletico PR', 'cruzeiro', 'botafogo', 'santos','bahia', 'fluminense', 'corinthians', 'chapecoense', 'ceara','vasco', 'sport', 'america', 'vitoria', 'parana')
c=0
for c in range(0, len(tabela)):
    if(c<5):
        print(f'{c+1}º colocado----{str(tabela[c]).upper()}')
    if(c>=16):
        print(f'{c+1}º colocado---{str(tabela[c]).upper()}')
    if(tabela[c]=='sport'):
        print('SPORT ESTÁ NA POSIÇÃO {}'.format(c+1))
print(sorted(tabela))
'''
#3)
'''
import random

var1=random.randint(0,10)
var2=random.randint(0,10)
var3=random.randint(0,10)
var4=random.randint(0,10)
var5=random.randint(0,10)
array=(var1, var2, var3, var4, var5)
valormenor=valormaior=0
valormenor=var1
for c in array:
    if(c>valormaior):
        valormaior=c
    if(c<valormenor):
        valormenor=c
print(array)
print(f'O valor maior é {valormaior}\nO valor menor é {valormenor}')
'''
#4)
'''
tres=x=0
num1=int(input('INFORME UM VALOR: '))
num2 = int(input('INFORME UM VALOR: '))
num3 = int(input('INFORME UM VALOR: '))
num4 = int(input('INFORME UM VALOR: '))

dupla=(num1, num2, num3, num4)


for x in range(0, len(dupla)):
    if(dupla[x]==9):
        print(f'{x}º posição apareceu o 9')
x=0
for x in range(0, len(dupla)):
    if (dupla[x] == 3):
        tres+=1
print(f'APARECERAM {tres} na dupla')
x=0
for x in range(0, len(dupla)):
    if (dupla[x]%2 == 0):
        print(f'{dupla[x]}')
'''
#5)

#lista_de_compras=('feijão', '3.5', 'arroz', '3.2', 'macarrão', '2.0', 'carne', '16.69', 'leite', '3.70', 'fubá', '1.50', 'biscoito', '2.80')
#print('\t\t\t****************\n\t\t\tLISTA DE COMPRAS\n\t\t\t****************')
#for c in (0, len(lista_de_compras)/2):
#    print(f'\t\t\t{str(lista_de_compras[c]).upper()}--------{str(lista_de_compras[c+1])}')
#6)
'''
palavras=('CASA', 'CARRO', 'CANETA', 'COMPUTADOR', 'TECLADO', 'ESTOJO', 'MOUSE', 'LAMPADA', 'LAPIS', 'DEDO', 'BRAÇO', 'MAO')

for palavra in palavras:
    print('\n',palavra,'--->', end=' ')
    for x in palavra:
        if x.lower() in 'aeiou':
           print(x, end=' ')
'''
