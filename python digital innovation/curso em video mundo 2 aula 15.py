#desafio1 pegar varios numeros até que o 999 seja digirado e mostre a soma sem o flag e a quantidade de numeros
#desafio2 programa para mostrar a tabuada de um valor se o valor for negativo a pessoa não quer ver mais tabuadas
#desafio3 jogo de par ou impar e o jogo será interrompido quando o jogador perder
#desafio4 programa que leia a idade, sexo de varias pessoas e mostre quantas pessoas tem mais de 18 anos
#quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos
#desafio5 programa que ler o nome e o preço de varios produtos e pergunte se o usuario quer continuar
#e mostre o total gasto, quantos produtos custam mais de 1000 e qual é o nome do produto mais barato
#desafio6 programa que simule caixa eletronico recebendo o valor a ser sacado e quantas cedulas de cada valor será entregue

#RESOLUÇÃO
#1)
'''
s=n=count=0

while n!=999:
    s+=n
    count += 1
    n=int(input('Informe o valor: '))
print(f'A soma  dos {count} resultou {s}')
'''
#2)
'''
n=x=0
c=1

while 1:
    n=int(input('Informe o valor: '))
    if (n<0):
        break
    for x in range(1,10):
        print(f'{n}x{x}={n*x}')

'''
#3)
'''
import random
c=x=0
n=''
while True:
    computer=random.randint(0,10)
    n=str(input(' Impar ou par?[P/I] ')).upper()
    c=int(input('Informe a aposta: '))
    print(computer)
    if(computer+c)%2==0 and n=='P':
        print('VOCÊ GANHOU!!')
        x+=1
    else:
        print('VOCÊ PERDEU!!')
        break
print(f'VOCÊ GANHOU {x} VEZES')
'''
#4)
'''
s=''
idade=pessoas=homem=mulher=adulto=0

while True:
    s=str(input('Informe seu sexo: ')).upper()
    idade=int(input('Informe sua idade: '))
    if idade>=18:
        adulto+=1
    if s=='M':
        homem+=1
    if s=='F' and idade>20:
        mulher+=1
    sair=str(input('Desseja sair?[S/N]')).upper()
    pessoas+=1
    if sair=='S':
        break
print('o grupo tem {} pessoas\nCom {} homens\nE {} mulheres maiores de 20 anos\n E {} adultos'.format(pessoas,homem,mulher,adulto))
'''
#5)
'''
produto=barato=sair=''
preco=numpro=precomenor=caros=soma=0
while True:
    produto=str(input('Informe o nome do produto: '))
    preco=float(input('Informe o valor do produto: '))

    if preco>=1000:
        caros+=1
    if preco<precomenor or numpro==0:
        precomenor=preco
        barato=produto
    numpro+=1
    soma+=preco
    sair=str(input('Deseja sair[S/N]:')).upper()
    if sair=='S':
        break;
print('{} tiveram preço acima dos R$1000,00\nO produto com menor valor é {}\nForam digitados {} produtos\nA conta total foi de {:.2}'.format(caros,barato,numpro,soma))
'''


