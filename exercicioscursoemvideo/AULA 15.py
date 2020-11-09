#
#
#
#
#
#
#
#
'''''''''
n=0
while True:
    n+=1
    print(n)
    if n>=30:
        break
'''''
#Desafio 1 ---> pegar varios numeros até 999 e somar esses numeros sem somar 999
'''''

n=soma=0
while True:
   n=int(input('NÚMERO: '))
   if n==999:break
   soma+=n
print(soma)
'''''
#Desafio 2 ---> fazer uma tabuada de vários números e terminará quando o npumero digitado for negativo
'''''''''
n=x=0
while True:
    x=0
    n=int(input('Digite o número: '))
    if n<0:break
    while x<=10:
        print('{}*{}={}'.format(x,n,x*n))
        x+=1
'''
#Desafio 3 ---> fazer um jogo de par ou impar e só parar quando o jogador perder mostrando o total de vitoria consecutivas que ele conquistou
'''''''''
import random
mac=g=n=0
while True:
    mac=random.randint(0,10)
    print(mac)
    lado=str(input('Escolha impar ou par: ')).lower()
    n=int(input('NÚMERO: '))
    if lado=='i' and (mac+n)%2==0:
        print('perdeu')
        break
    elif lado=='p' and (mac+n)%2!=0:
        print(perdeu)
        break
    g+=1
print('voce ganhou {} vezes'.format(g))
'''''''''
#Desafio 4 ---> leia a idade e o sexo de varias pessoas perguntando se quer ou não continuar mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e mulheres com menos de 20 anos
'''''''''
mm=ho=maior=0
while True:
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO: ')).upper()
    if idade>18:
        maior+=1
    if sexo=='M':
        ho+=1
    if sexo=='F' and idade<20:
        mm+=1
    sair=str(input('Deseja sair?'))
    if sair=='s':
        break

print('{} Pessoas tem mais de 18 anos\nForam cadastrados {} homens\n{} Mulheres tem menos de 20 anos'.format(maior,ho,mm))
'''''''''
#Desafio 5 ---> leia o nome o preço de varios produtos. Qual é o total gasto na compra, quantos produtos custam mais de 1000 reais, e produtos mais barato
'''''''''
soma=caro=precomenor=a=0
barato=''
while True:
    nome=str(input('Nome do produto: '))
    preco=int(input('preço do produto: '))
    soma+=preco
    if a==0:precomenor=preco
    if preco>1000:
        caro+=1
    if preco<=precomenor:
        precomenor=preco
        barato=nome
    sair=str(input('Deseja finalizar a compra? '))
    if sair=='s':
        print('total a pagar----------------------------------{}\ntotal de produtos acima de 1000 reais----------{}\nproduto mais barato----------------------------{}'.format(soma,caro,barato))
        break
    a+=1
'''''''''
#Desafio 6 ---> pergunte o valor a ser sacado, o programa vai informar quantas cedulas de cada valores serão entregues com cédulas de 100, 50, 20, 10, 2 e 1
v=int(input('Qual o valor a ser sacado? '))
ncem=ncin=nvin=ndez=ncinc=ndoi=num=0
while True:
    if v>=100:
        v-=100
        ncem+=1
    elif v<100 and v>=50:
        v-=50
        ncin+=1
    elif v<50 and v>=20:
        v-=20
        nvin+=1
    elif v<20 and v>=10:
        v-=10
        ndez+=1
    elif v<10 and v>=5:
        v-=5
        ncinc+=1
    elif v<5 and v>=2:
        v-=2
        ndoi+=1
    else:
        v-=1
        num+=1
    if v==0:break
print('100--------{}\n50---------{}\n20---------{}\n10---------{}\n5----------{}\n2----------{}\n1----------{}'.format(ncem,ncin,nvin,ndez,ncinc,ndoi,num))