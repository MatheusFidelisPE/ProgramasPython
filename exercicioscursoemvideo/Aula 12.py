#------->Estruturas de condição aninhadas<---------
#Uma estrutura condicional dentro de uma outra estrutura condicional.
#if primeiro_bloco:...
#elif segundo_bloco:...
#elif terceiro_bloco:...
#else:...
#precisa ter primerio um if para que tenha um elif
#
#
#
#
#
#
'''''''''
nome=str(input('Qual o seu nome? '))
nome.lower()
if nome.lower()=='matheus':
    print('Que nome bonito, Matheus')
elif nome.lower()=='carlos':
    print('Que nome normal, Carlos')
elif nome.lower() == 'paulo':
    print('Seu nome é bem feio paulo')
else:
    print('Teu nome é muito estranho')
'''''''''
#Desafio 1 ---> aprovando o emprestimo bancario para a compra de uma casa
#pegar o valor do salário, valor da casa, quantos anos para quitar a casa e negar se o valor da prestação mensal for maior que 30% do salário do indivíduo
'''''''''
sal=float(input('Informe o seu salário: '))
casa=float(input('Informe o valor da casa: '))
parcelas=int(input('Informe o número de parcelas que você deseja: '))
if (casa/parcelas)> sal*0.3:
    print('Infelizmente não poderemos ceder o financiamento. Tente aumentar o número de parcelas.')
else:
    print('Parabéns! segundo suas informações você está apto para receber o financiamento.')
'''''''''
#Desafio 2 ---> menu de escolha de conversão para octal, binário ou hexadecimal
'''''''''
num=int(input('Informe um número: '))
print('\t\t\t1-Octal\t\t\t2-Binário\t\t\t3-Hexadecimal\n')
escolha=int(input('Qual a base de conversão desejada? '))

if escolha==1:
    print('{} em octal corresponde a {}'.format(num,oct(num)))
elif escolha ==2:
    print('{} em binário corresponde a {}'. format(num,bin(num)))
elif escolha==3:
    print('{} em hexadecimal corresponde a {}'.format(num, hex(num)))
else:
    print('Suas escolha foi inválida.')
'''''''''
#Desafio 3 ---> receber dois números e informar qual deles é maior ou se são iguais
'''''''''
num1=int(input('Informe o primeiro número: '))
num2=int(input('Informe o segundo número: '))

if num1>num2:
    print('O primeiro número é maior que o segundo número.')
elif num1<num2:
    print('O segundo número é maior que o primeiro número.')
else:
    print('Os valores são iguais.')
'''''''''
#Desafio 4 ---> receber o ano de nascimento de um jovem e informar sua situação perante o serviço militar
#mostrar o quanto tempo falta ou quanto tempo passou do prazo
'''''''''
from datetime import datetime
agora=datetime.now()
nascimento=input('Informe a data de nascimento:(dd/mm/aaaa) ')
nascimento=nascimento.split('/')
dia=int(nascimento[0])
mes=int(nascimento[1])
ano=int(nascimento[2])

if agora.year-ano>18:
    print('Você já deveria ter se alistado. Há {} anos'.format((agora.year-ano)-18))
elif agora.year-ano<17:
    print('Você ainda não está em idade para alistamento. Faltando {} anos para o alistamento'.format(18-(agora.year-ano)))
'''''''''
#Desafio 5 ---> mostre a média de um aluno pegando duas notas e mostrando sua situação, acima de 7 ele passa
'''''''''
nota1=float(input('Informe a sua primeira nota: '))
nota2=float(input('Informe a sua segunda nota: '))
media=(nota1+nota2)/2
if media>=7:
    print('Você foi aprovado.')
elif media>= 4 and media<7:
    print('Você precisará fazer a recuperação final.')
elif media<4:
    print('Você foi reprovado.')
'''''''''
#Desafio 6 ---> leia a idade de um atleta para saber qual a categoria do atleta
#até 9 anos mirim, até 14 anos infantil, até 19 anos junior, até 20 anos sênior, acima master.
'''''''''
idade=int(input('Informe sua idade: '))
if idade<9:
    print('Você pertence a categoria \033[1;;46mMIRIM\033[1;;m')
elif idade>=9 and idade<=14:
    print('Você pertence a categoria \033[1;;46mINFANTIL\033[1;;m')
elif idade>14 and idade<19:
    print('Você pertence a categoria \033[1;;46mJUNIOR\033[1;;m')
elif idade>=19 and idade<20:
    print('Você pertence a categoria \033[1;;46mSÊNIOR\033[1;;m')
else:
    print('Você pertence a categoria \033[1;;46mMASTER\033[1;;m')
'''''''''
#Desafio 7 ---> pegar as dimensões de retas para saber se elas formam um triangulo e formando informe se ele é equilatero, isósceles ou escaleno
r1=int(input('Informe o tamanho da primeira reta: '))
r2=int(input('Informe o tamanho da segunda reta: '))
r3=int(input('Informe o tamanho da terceira reta: '))

if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
    print('\t\tSUAS RETAS FORMAM UM TRIÂNGULO!')
    if r1==r2 and r2==r3:
        print('Seu triângulo é equilatero.')
    if r1!=r2 and r1!=r3 and r2!=r3:
        print('Seu triângulo é escaleno.  ')
    if r1==r2 and r2!=r3 or r2==r3 and r1!=r3:
        print('Seu triângulo é isósceles. ')
else:
    print('Suas retas não formam um triângulo. ')


#Desafio 8 ---> ler o peso e altura de uma pessoa e calcule o IMC e mostre o status
#até 18.5 abaixo do peso, entre 18.5 e 25 peso ideal, de 25 até 30 sobrepeso, de 30 até 40 obesidade, acima de 40 obesidade morbida
'''''''''
peso=float(input('Informe seu peso: '))
altura=float(input('Informe sua altura: '))
imc=peso/(altura*altura)
if imc<18.5:
    print('Você está abaixo do peso.')
elif imc>18.5 and imc<25:
    print('Seu peso é o ideal. ')
elif imc>25 and imc<30:
    print('Você tem sobrepeso. ')
elif imc>30 and imc<40:
    print('Você tem obesidade.')
else:
    print('Você tem obesidade morbida. ')
'''''''''
#Desafio 9 ---> receba o preço normal do produto e a condição de pagamaento. informe o valor do pagamento.
#à vista dinheiro ou cartão de débito 10% de desconto, em até 2x no cartão preço normal, acima de 3x no cartão juros de 20%
'''''''''
preco=float(input('Informe o preço do produto: '))
pagamento=str(input('De que forma você pretende pagar?'))
deb=int(pagamento.find('débito'))-int(pagamento.find('debito'))

if pagamento.find('dinheiro')!=-1 or deb!=0:
    print('O valor do produto é {}'.format(preco*0.9))

elif pagamento.find('crédito')!=-1:
    parcelas=int(input('Informe a quantidade de parcelas:'))
    if parcelas<=2:
        print('O valor do produto permanece os mesmos {} reais.'.format(preco))
    elif parcelas>2:
        print('O valor do produto será {} reais'.format(preco*1.20))
'''''''''
#Desafio 10 ---> faça um programa que jogue pedra papel e tesoura
'''''''''
import random
jogou=random.choice(['PEDRA','PAPEL','TESOURA'])
jogue=str(input('ESCOLHA: '))

if jogue.lower()=='papel' and jogou=='PEDRA':
    print('\tGANHOU')
elif jogue.lower()=='papel' and jogou=='PAPEL':
    print('\tEMPATOU')
elif jogue.lower() =='papel'and jogou=='TESOURA':
    print('\tPERDEU')
elif jogue.lower()=='tesoura' and jogou=='PEDRA':
    print('\tPERDEU')
elif jogue.lower()=='tesoura' and jogou=='PAPEL':
    print('\tGANHOU')
elif jogue.lower()=='tesoura' and jogou=='TESOURA':
    print('\tEMPATOU')
elif jogue.lower()=='pedra' and jogou=='PAPEL':
    print('\tPERDEU')
elif jogue.lower()=='pedra'and jogou=='TESOURA':
    print('\tGANHOU')
elif jogue.lower()=='pedra' and jogou=='PEDRA':
    print('\tEMPATOU')
else:
    print('ESSA PALAVRA NÃO PERTENCE AO JOGO. É BURRO?PQP!')

print('MACHINE\t\t  EU\n{}\t\t{}'.format(jogou.upper(), jogue.upper()))
'''''''''
