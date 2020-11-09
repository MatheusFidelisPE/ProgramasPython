#laços de repetição
#o uso do da estrutura de repetição FOR
#o FOR é um laço com variável de controle
# for variável in range(1,10):
#for variável in range (0,10,x)
#o zero significa o inicio do range
#o dez o fim do range
#e o x significa o que será atribuido a soma da primeira variavel
#
#
#

#for c in range(0,10):
 #   print('\t'*c,'oi')
#print('oi\t'*c)
''

#Desafio 1 ---> contagem regressiva para estouro de gofos de artifício de 10 até 0 com 1 segundo de delay
'''''''''
import time
print('É O FIM DO ANO!!!')
for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print('BUMMMMMMM!!! FELIZ ANO NOVO.')
'''''''''
#Desafio 2 ---> programa que calcule a soma de todos os números impares que são multiplos de 3 entre 1 e 500
'''''''''
soma=0
for c in range(0,500,3):
    if c%2!=0:
        soma+=c
print(soma)
'''''''''
#Desafio 3 ---> Criar uma tabuada usando repetição
'''''''''
num=int(input('Digite o número: '))

for c in range(0,11):
    print('{}*{}={}'.format(num,c,num*c))
'''''''''
#Desafio 4 ---> ler seis numeros inteiros e mostre a soma dos números pares
'''''''''
soma=0
for c in range(0,6):
    num=int(input('Digite o número: '))
    if num%2==0:
        soma+=num
print(soma)
'''''''''
#Desafio 5 ---> ler o primeiro termo da PA e a razão e mostrar os 10 primeiros termos
'''''''''
termo=int(input('Informe o primeiro termo da PA: '))
r=int(input('Informe a razão: '))
for c in range(termo,(termo+r*10),r):
    print(c)
'''''''''
#Desafio 6 ---> indicar se o número é primo ou não
'''''''''
num=int(input('Informe o número: '))
pri=0
for c in range(2,num):
    if num%c==0:
        pri+=1
if pri>0:
    print('Não é primo')
else:
    print('É primo!')
'''''''''
#Desafio 7 ---> identificar se a frase lida é um palindromo
#apos a sopa a sacada da casa a torre da derrota o lobo ama  o bolo anotaram a data da maratona
'''''''''
frase=str(input('Digite uma frase: '))
espa=frase.count(' ')
int(espa)
frasediv=frase.split(' ')
frasejunt=''
print(frasediv,'\tespaços',espa)

for c in range(0,espa+1):
    frasejunt+=frasediv[c]

    print(frasediv[c])

fraseinvert=frasejunt[::-1]

print(fraseinvert)

if frasejunt==fraseinvert:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
'''''''''
#Desafio 8 ---> leitor da idade de 7 pessoas e mostrar quantas já são de maiores e quantas não são
'''''''''
menor=0
maior=0

for c in range(0,6):
    idade=int(input('Digite a idade: '))
    if idade<18:
        menor+=1
    else:
        maior+=1
print('{} são maiores de idade e {} são menores de idade.'.format(maior,menor))
'''''''''
#Desafio 9 --->Leitor de peso de 5 pessoas e mostrar qual foi o maior e o menor
'''''''''
pesoa=0
pesao=0
for c in range (0,6):
    peso = int(input('Informe seu peso: '))
    if peso>pesoa:
        pesao=peso
    pesoa=peso
print(pesao)
'''''''''
#Desafio 10 ---> ler o nome, a idade e sexo de 4 pessoas e o programa mostrar a média de idades, o nome do homem mais velho, quantas mulheres tem menos de 20 anos
'''''''''
idadea=0
soma=0
nova=0

for c in range(0,4):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo com (M/F): ')
    soma=soma+idade
    if idade>idadea and sexo=='M':
        nomevelho=nome
    idadea=idade
    if sexo=='F' and idade<20:
        nova+=1
    print('\n')
print('A média de idade do grupo é {}\n{} é o homem mais velho\nHá no grupo {} mulheres com menos de 20 anos'.format(soma/4,nomevelho,nova))
'''''''''






