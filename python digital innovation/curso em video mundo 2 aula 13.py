import time
#desafio 1 programa que mostre na tela a contagem regressiva para o estouro de fogos
#desafio 2 mostrar todos os numeros pares entre 1 e 50
#desafio 3 programa para calcular a soma de todos os numeros imapares, multiplos de 3 entre 1 e 500
#desafio 4 fazer uma tabuada com um laço for
#desafio 5 programa que leia 6 numeros inteiros e mostrar a soma dos números pares
#desafio 6 programa que leia o primeiro termo e a razão de uma pa e mostrar os 10 primeiros termos de uma PA
#desafio 7 programa que leia um numero inteiro e diga se é ou não primo
#desafio 8 programa que leia uma frase qualquer e diga se é um palindromo
#desafio 9 programa que leia 7 anos de nascimento e diga quantos atingiram a maior idade 21 anos
#desafio 10 programa que leia o peso de 5 pessoas e mostre o maior e o menor peso
#desafio 11 desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas e mostre a média de idade, o nome do mais velho e quantas mulheres tem menos de 20 anos
#RESOLUÇÃO
#1)
'''''''''
for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print('****FELIZ ANO NOVO!!*****')
'''''''''''
#2)
'''''''''
for c in range(2,50+1,2):
    print(c)
'''
#3)
'''''''''
for c in range(1,500,2):
    if(c%3==0):
        print(c)
'''
#4)
'''''''''
num=int(input('Infome o valor: '))
for c in range(0,11):
    print('{} x {} = {}'.format(num, c, num*c))
'''''
#5)
'''''''''
soma=0
num=0
for c in range(0,6):
    num=int(input('Informe o valor: '))
    if(num%2==0):
        soma+=num
print(soma)
'''''
#6)
'''''''''
n=int(input('Informe o primeiro termo da PA: '))
r=int(input('Informe a razão da PA: '))
b=n+10*r
for c in range(n,b,r):
    print(c)
''''' \
#7)
'''''''''    
x=0
num=int(input('Informe um numero: '))

for c in range (2,num):
    if(num%c==0):
        x+=1
if(x>0):
    print("O valor {} não é um primo".format(num))
else:
    print('O valor {} é um número primo'.format(num))
'''
#8)
frase=str(input('Digite a frase: ')).strip().upper()
separados=str.split(frase)
juntos=''.join(separados)
inverso=''

for letra in range(len(juntos)-1,-1,-1):

    inverso+=juntos[letra]
print(' A frase digitada {} tem inverso igual a {}'.format(juntos,inverso))
if(inverso==juntos):
    print('É um palindromo')
else:
    print('Não é um palidromo')
print('FIM DE PROGRAMA')
#9)
'''''''''
atual=2020
x=0
for c in range(0,7):
    ano=int(input('Informe o ano que você nasceu: '))
    if(atual-ano>=21):
        x+=1
print('{} pessoas tem 21 ou mais anos de idade.'.format(x))
'''
#10)
'''''''''
pesopesado=0
pesomenor=0
for c in range(0,10):
    peso=int(input('Informe seu peso: '))
    if(peso>pesopesado):
        pesopesado=peso
        if (c == 0):
            pesomenor=peso
    if(peso<pesomenor):
        pesomenor=peso
print('O maior peso nas pessoas lidas é {}\nO menor peso tem {}'.format(pesopesado,pesomenor))
''''' \
#11)
'''''''''    
soma=0
idadea=0
nomevelho=""
mulhervelha=0
for c in range(0,4):
    nome=input('Informe seu nome: ')
    idade=int(input('Informe sua idade: '))
    sexo=input('Informe seu sexo com F ou M: ')
    soma+=idade
    if(idade>idadea):
        nomevelho=nome
        idadea=idade
    if(sexo=='F' and idade>21):
        mulhervelha+=1
print('A média de idade das pessoas é {}\n{} é a pessoa mais velha\nNeste grupo temos {} mulheres acima de 21 anos'.format((soma/4),nomevelho,mulhervelha))
'''

