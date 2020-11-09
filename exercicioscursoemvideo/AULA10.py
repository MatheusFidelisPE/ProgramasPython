#aula de ocndições
#se carro.esquerda() blobo verdadeiro verde
#senão bloco falso vermelho
#se -> if carro.esquerda:
#           bloco verdadeiro
#senão -> else:
#       bloco falso
#
#
#
#
#
#
#
#
#
'''''''''
tempo=int(input('Quantos anos tem o seu carro?'))

if tempo<=3:
    print('carro novo')
else:
    print('carro velho')

print('carro novo'if tempo<=3 else'carro velho')

'''''''''
'''''''''

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))

m=(n1+n2)/2
if m>6.0:
    print('Parabéns!!! você passou')
    if m>9.0:
        print('Sua nota foi excelente')
if m<6.0:
    print("voce foi para a recuperação")

'''''''''

#Desafio 1 ---> joguinho para saber se o usuario acertou o número
'''''''''
import random
num= random.randint(1,5)
escolha=int(input('Digite sua aposta de 0 a 5: '))

if escolha==num:
    print('Parabéns! você acertou!')
else:
    print('Você errou o numero era {}'.format(num))

print('******FIM********')
'''''''''''

#Desafio 2 ----> mostrar se o carro foi multado.
'''''''''''
km=7
lim=80

vel=float(input('Informe a velocidade do seu carro: '))
valor=7*(vel-lim)
if vel>=lim:
    print('Olha a velocidade, fresco. tu foi é mutado, corno!')
    print('vai pagar {} reais'.format(valor))
else:
    print('Tudo certo cidadão. Pode passar.')
'''''''''''
#Desafio 3 ---> Mostra se o numero é par ou impar
'''''''''''
num=int(input('Digite um número: '))
if num%2==0:
    print('Número é par')
else:
    print('Seu número é impar')
'''''''''''
#Desafio 4 ---> calculando o preço da passagem de onibus
'''''''''''
num=0.50
acima=0.45
distancia=float(input('Informe a distância da sua viagem: '))

if distancia<=200:
    print(distancia*0.5,' reais')
else:
    print(distancia*0.45,'reais')
'''''''''''
#Desafio 5 ---> descobre se o ano é bissexto4
'''''''''''
ano=int(input('Informe o ano: '))

if ano%4==0:
    print('O ano escolhido é bissexto!')
else:
    print('O ano esclhido não é bissexto!')
'''''''''''
'''''''''''

#Desafio 6 ---> leitor de numeros e informa qual é o menor e qual é o menor
n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
n3=int(input('Digite o terceiro numero: '))

if n1>n2 and n1>n3:
    maior=n1
if n2>n1  and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
else:
    maior='dois numeros iguais'
if n1<n2 and n1<n3:
    menor=n1
if n2<n1 and n2<n3:
    menor =n2
if n3<n1 and n3<n2:
    menor=n3
else:
    menor='dois numeros iguais'
print(maior,menor)

'''''''''''
#Desafio 7 ----> Calculando o valor do aumento do funcionario
'''''''''''

au1=1.10
au2=1.15
sal=float(input('Informe o seu salário: '))

if sal>1250:
    print('Seu novo salário é de {:.2f} reais'.format(au1*sal))
else:
    print('Seu novo salário é de {:.2f} reais'.format(au2*sal))
print('Parabéns seu novo salário!!!!')
'''''''''''
#Desafio 8 ---> retas que formam ou não um triângulo
r1=float(input('Informe o tamanho do segmento da primeira reta: '))
r2=float(input('Informe o tamanho do segmento da segunda reta: '))
r3=float(input('Informe o tamanho do segmento da terceira reta: '))

if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:

    print('Suas retas formam um triângulo')#if r1<r2-r3 or r2>r3-r1 or r3>r1-r2:
 #   print('Impossível formar este triângulo.')
else:

    print('Impossível formar este triângulo.')














