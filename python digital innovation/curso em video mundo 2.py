#Exercicios de python fornecidos na aula 12 do curso em vídeos

#desafio 1-Escreva um programa para aprovar um emprestimo bancario para a conta de uma casa
#O programa vai receber o valor da casa, o salario, e quantos anos de pagamento.
#cálcule o valor da prestação mensal sabendo que ela não poderá exceder 30% do salário
#desafio 2-Leitura de um inteiro e escolher a base de conversão 1-bina, 2-octal e 3-hexa
#desafio 3-leitura de dois numeros inteiros e compare-os (o primeiro é maior ou o segundo é o maior ou os dois são iguais)
#desafio 4-programa para saber se o jovem ainda terá que se alistar, ou se ele deve se alistar, ou  se já passou da hora
#desafio 5-crie um programa que leia duas notas do aluno e informe se ele foi reprovado, passou ou esta de recuperação
#desafio 6-receber o ano de nascimento de um atleta de natação até 9anos é mirim, até 14 é infantil, até 19 anos é junor
#até 20 anos é senior e acima é master
#desafio 7-ler tres segmentos de reta e informar se forma um triangulo e se ele é equilatero, isóceles ou escaleno
#desafio 8-programa para ler o peso e a altura de uma pessoa e calcule o imc, abaixo de 18.5 é abaixo do peso
#até 25 peso ideal, até 30 sobrepeso, até 40 obesidade acima de 40 obesidade morbida
#desafio 9-pegue o preço do produto e escolha a forma de pagamento, a vista 105 de desconto,
#a vista no cartão 5% de desconto, 2x no cartão preço normal, 3x ou mais no cartão 20% de juros
#desafio 10-fazer um jogo jokenpô homem contra maquina
#***************RESOLUÇÃO:
#1)
'''''''''
nome=input('Informe seu nome: ')
valor=int(input('informe o valor da casa: '))
salario=int(input('Informe o valor do seu salario: '))
tempo=int(input('informe quantos anos passará pagando: '))

equ=((valor/tempo)/12)
if(equ>(0.3)*salario):
    print('Infelizmente seu emprestimo foi negado, {}'.format(nome))
else:
    print('Parabéns seu imprestimo foi aceito,{}. \nvocê pagará uma mensalidade de {}'.format(nome,equ))
'''''
#2)
'''''''''
num=int(input('Informe o valor:'))
escolha=int(input('Qual a sua escolha?\n\t1-Binario\t2-Octal\t 3-Hexadecimal\n'))
if(escolha==1):
    print('o valor {} tem valor binario de {}'.format(num,bin(num)))
elif(escolha==2):
    print('O valor {} tem valor octal de {}'.format(num, oct(num)))
elif(escolha==3):
    print('O numero {} tem valor hexadecimal de {}'.format(num, hex(num)))
else:
    print('VOCÊ ESCOLHEU UM VALOR DIFERENTE DOS AUTORIZADOS.')
'''''
#3)
'''''''''
num1=int(input('Informe o primeito numero: '))
num2=int(input('Informe o segundo numero: '))

if(num1>num2):
    print('O {} é maior que {}'.format(num1, num2))
elif(num2>num1):
    print('O {} é meior que o {}'.format(num2, num1))
else:
    print('O {} é igual a {}'.format(num2, num2))
'''''''''''





