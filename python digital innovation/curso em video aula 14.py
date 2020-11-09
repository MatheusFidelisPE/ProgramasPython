#desafio1 programa que leria o sexo de uma pessoa e só aceite f ou m se estiver errado
#peça para digitar novamente até que esteja correto
#desafio2 o computer vai pensar em um numero e o jogador jogará até que vc acerte
#desafio3 programa que leia dois valores e mostre um menu 1-somar, 2-subtrair, 3-maior, 4-novos, 5 -sair
#desafio4 faça um programa que revele o fatorial de um número
#desafio5 ler o primeiro termo e a razão de uma pa e mostre os 10 termos
#desafio6 rafazer o desafio 5 e pergunte agora se ele quer ver mais termos até que o usuario digite 0
#desafio7 programa que leia um n inteiro e escreva os n primeiros termos de uma sequencia de fibonacci
#desafio8 programa para pegar varios numeros até que digite 999 e some esses valores e quantos valores foram
#desafio9 ler varios valores e imprimir a média o maior e o menor valores
#RESOLUÇÃO
import math
import random
#1)
'''
c=''
while (c!='F' and c!='M'):
   print(c)
   c=str(input('Informe seu sexo[F/M]: ')).upper()
print('Seu sexo é {}'. format(c))
'''
#2)
'''
counter=0
apos=0
ini=int(input('Informe o inicio: '))
fim=int(input('Informe o fim: '))
num=random.randint(ini,fim)
while (num-apos!=0):
    apos=int(input('Informe o valor apostado: '))
    counter+=1
print('PARABÉNS VOCÊ GANHOU!!!\n\t\tVocê precisou de {} apostas para ganhar.'.format(counter))
'''
#3)
'''
num1=num2=escolha=0
while escolha!=5:
    escolha=0
    num1=int(input('informe o valor 1: '))
    num2=int(input('Informe o valor 2: '))
    while escolha!=4 and escolha!=5:
        escolha=int(input('Informe sua escolha\n[1]SOMAR\n[2]SUBTRAIR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR\n'))
        if(escolha==1):
            print('A soma de {} e {} é igual a {}'.format(num2, num1, num2+num1))
        elif(escolha==2):
            print('A subtração de {} e {} é igual a {}'.format(num1, num2,num1-num2))
        elif(escolha==3):
            if(num1>num2):
                print('O {} é maior que o {}'.format(num1, num2))
            elif(num2>num1):
                print('O {} é maior que o {} '.format(num2,num1))
            else:
                print('Os valores são iguais')

print('FIM DE PROGRAMA')
'''
#4)
'''
memo=num=int(input('Informe o termo do fatorial: '))
fato=1

while(num>0):
    print('{}'.format(num))
    fato *= num
    num-=1

print('O fatorial de {} é {}'.format(memo, fato))
'''
#5)
'''
pri=int(input('Informe o primeiro termo: '))
raz=int(input('Informe a razão da PA: '))
c=1
print(pri)
while c<10:
   termo=pri+c*raz
   print(termo)
   c+=1'''
#6)
'''
pri=int(input('Informe o primeiro termo: '))
raz=int(input('Informe a razão da PA: '))
c=mais=n=1
print(pri)
while c<10 and mais!=0:
    termo=pri+c*raz
    print(termo)
    c+=1
    while mais!=0 and c>=10:
        mais=int(input('Queres imprimir mais quantos valores? '))
        while n<=mais:
            termo=termo+raz
            print(termo)
            n+=1
'''
#7)
'''
num=int(input('Informe quantos termos da sequência vc deseja: '))
term1=term2=1
print('1\n1')
while num>0:
    valor=term1+term2
    print('{}\t{}\t{}\t'.format(valor,term1,term2))
    term1 = term2
    term2=valor
    num-=1
'''
#8)
'''
num=soma=c=0

while num!=999:
    num=int(input('Valor: '))
    soma+=num
    c+=1
soma-=num
c-=1
print('foi digitado {} termos tendo soma igual {}'.format(c,soma))
'''
#9)
'''
num=soma=x=numenor=nummaior=0
c=''
while c!='N':
    num=int(input('Valor: '))
    soma+=num
    x+=1
    c=str(input('Queres continuar?[S/N]')).upper()
    if(num>nummaior):
        nummaior=num
    if(num<numenor or x==1):
        numenor=num

print('A média dos termos é {}\nO maior valor digitado foi {}\nO menor valor digitado foi {}'.format(soma/x,nummaior,numenor))
'''

