#Estruturas de repetição
#aprendendo o uso do while
#while not variavel:
#or while variavel:
#
#
#
#
#
#
#

#Prática aula 14
'''''''''
for c in range (1,10):
    print(c)
c=0
while c<10:
    print(c)
    c+=1
'''''''''''
#Desafio 1 ---> faça um programa que leia o sexo de uma pessoa e só permita o fim se digitar o valor correto
'''''''''''
sexo=''
while sexo!='F' and sexo!='M':
    sexo=str(input('Informe seu sexo[F/M]')).upper()
print('\t\t\t\tFIM'
'''''''''''
#Desfio 2 ---> criar um jogo e deixar a pessoa tentar adivinhar o número de 0 a 10
'''''''''''
import random
escolha=0
n=''
while n!='N':
    escolha=int(input('Escolha um número de 1 a 100 '))
    num = random.randint(1, 100)

    while num!=escolha:

        if escolha>num:
            print('MENOS')
        else:
            print('MAIS')
        escolha=int(input(''))
    n=str(input('CONTINUAR?[S/N]'))
'''''''''''
#Desafio 3 ---> crie um programa que leia dois valores e crie um menu que possa somar, multiplicar, dividit, subtrair e sair do programa ou pegar outros numeros
'''''''''''
menu=''
while menu!='S':
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    print('\t\t\t\t\t\t\t\t\t\t\t MENU\n\n\n\t[SO]SOMA\t[MU]MULTIPLICAR\t[MA]MAIOR\t[ME]MENOR\t[NN]NOVOS NÚMEROS\t[S]SAIR\n')
    menu=str(input('Escolha o que fazer com os números'))
    if menu=='SO':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif menu=='MU':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif menu=='MA':
        if n1>n2:
            print(n1,'>',n2)
        else:
            print(n1, '<', n2)
    elif menu=='NN':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    else:
        break
'''''''''''
#Desafio 4 ---> leia um número qualquer e calcular o fatorial do número
'''''''''''
n1=int(input('Informe o número: '))
n=n1-1
while n>0:
    n1*=n
    n-=1
print(n1)
'''''''''''
#Desafio 5 ---> ler o primeiro termo e a razão da PA e mostrar os 10 primeiros termos usando while
'''''''''''
termo=int(input('Informe o primeiro termo: '))
razao=int(input('Informe a razão: '))
n=0
valor=termo
while n<10:
   print('{} '.format(valor), end='')
   valor+=razao
   n+=1
'''''''''''
#Desafio 6 ---> fazer o 5 novamente e mostrar quantos termos a mais a pessoa vai querer
'''''''''''
termo=int(input('Informe o primeiro termo: '))
razao=int(input('Informe a razão: '))
n=0
valor=termo
i=0
while n<10+i-1:
   print('{} '.format(valor), end='')
   valor+=razao
   n+=1
   if n==9:
       i=int(input('\nQuantos termos mais você tem interesse? '))
print('\nFIM')
'''''''''
#Desafio 7 ---> mostrar a sequencia de fibonacci dos n elementos requeridos
'''''''''
n=int(input('Quantos elementos você tem interesse? '))
c=0
termo=0
termoa=1
termoant=1
print('0->1->1->', end='')
while c<n:
    termo=termoa+termoant
    print('{}'.format(termo), end='')
    termoant = termoa
    termoa=termo
    if n-1==c:
        print('',end='')
    else:print('->', end='')
    c+=1
    '''''
#Desafio 8 ---> crie um programa que leia varios números inteiros e só para quando a pessos digitar 999
'''''''''
num=0
soma=0
while num!=999:
    num=int(input('NÚMERO:'))
    soma+=num
print(soma-999)
'''
#Desafio 9 ---> pegar varios números de um teclado fazer a média  mostrar o maior e o menor valor lido

num=0
sair=''
nummaior=0
nummenor=0
soma=0
n=1

num=int(input('NÚMERO: '))
nummenor=num
nummaior=num

while sair!='S':

    if n>1:
        num = int(input('NÚMERO: '))
    soma += num

    if num>nummaior:
        nummaior=num
    if num<nummenor:
        nummenor=num
    sair = str(input('Sair?')).upper()
    n+=1
print('Média={} Maior={} Menor={}'.format(soma/(n-1),nummaior,nummenor))














