#desafio1 programa que leia 5 valores numericos e guarde-os em uma lista. Mostre o maior, o menor e suas respectivas posições na lista
#desafio2 programa para adicionar varios valores numericos e cadastre os em uma lista se o numero já exista na lista ele não será adicionado. no final serão exibidos todos os valores únicos digitados em ordem crescente
#desafio3 programa que o usuario digite 5 valores numericos e cadastre-os em uma lista já na posição correta de inserção e no final mostre a lista ordenada na tela
#desafio4 programa que ler varios numeros e mostrar quantos numeros foram digitados, lista de ordenada de forma decreescetes e se o 5 foi digitado
#desafio5 programa que ler varios numeros e guarde os em uma lista e depois guardar todos os pares em uma lista e todos os impares em outra lista e mostrar as tres listas
#desafio6 programa que pega uma expressão e mostre se os parenteses estão na fechados na forma correta


#                                   RESOLUÇÃO DOS EXERCÍCIOS

#1)programa que leia 5 valores
#numericos e guarde-os em uma lista. Mostre o maior,
#o menor e suas respectivas posições na lista
num=[]
'''
for c in range(0,5):
    num.append(int(input('Informe o valor: ')))
print(f'O maior valor é {max(num)} que está na posição {num.index(max(num))+1}')
print(f'O menor valor é {min(num)}, que está na posição {num.index(min(num))+1}')
num.sort()
for c in num:
    print(f'{c}...', end='')
print('\n')
'''

#2)programa para adicionar varios valores numericos
#e cadastre os em uma lista se o numero já exista
#a lista ele não será adicionado.
#no final serão exibidos todos os valores únicos digitados em ordem crescente
'''
saida=''
numcomposto=[]
num=0
while saida!='N':
    num=int(input('Informe um valor: '))
    if num in numcomposto:
        print('O número digitado já foi adicionado')
    else:
        numcomposto.append(num)
    saida=str(input('Deseja continuar?[S/N]')).upper()
numcomposto.sort()
print('\t\tA lista completa sem repetições é composta por ')
for c in numcomposto:
    print(f'{c}...', end='')
'''
#3)programa que o usuario digite 5 valores numericos e cadastre-os
#em uma lista já na posição correta de inserção e no final mostre
#a lista ordenada na tela
# A FUNÇÃO INSERT TEM O PRIMEIRO PARAMETRO O VALOR E O SEGUNDO O ÍNDICE DA LISTA ONDE VAI O VALOR
# USANDO O ENUMARATE(LISTA) EM UM FOR TEMOS O PRIMEIRO VALOR REFERENTE AO INDICE E O SEGUNDO AO VALOR GUARDADO NO RESPECTIVO INDICE
'''posso pegar uma variavel e testar ela nos cinco quando encontrar um valor menor que ela o valor será apagado e agora colocado o valor da variavel e o valor anterior será colocado'''
'''
lista=[]
n=0
for c in range(0,5):

    n=int(input('Informe o valor: '))
    if(c==0 or n>=(lista[len(lista)-1])):
        lista.append(n)
        print('Pertence a ultima posição')
    else:

        for indice in range(0,len(lista)):

            if(n<=lista[indice]):
                lista.insert(indice,n)
                print(f'Pertence a {indice+1}º posição')
                break

print(lista)
'''
#desafio4
'''
num=[]
cont=numa=0
saida=''
while saida!='S':
    numa=int(input('Informe o valor: '))
    num.append(numa)
    saida=str(input('Desaja sair?[S/N]')).upper()
    cont+=1
num.sort(reverse=True)
print(f'Digitou-se {cont} valores.\nA lista ordenada de forma decrescente é:')
for c in  num:
    print(f'{c}...', end='')
if 5 in num:
    print('\nO 5 foi encontrado na lista')
else:
    print('\nO 5 não foi encontrado na lista')
'''
#6)
'''
num=[]
numimpar=[]
numpar=[]
numa=cont=0
saida=''
while saida!='S':
    numa=int(input('Informe o valor: '))
    num.append(numa)
    saida=str(input('Desaja sair?[S/N]')).upper()
    cont+=1
num.sort()
print(len(num))
for c in num:
    if(c%2==0):
        numpar.append(c)

    else:
        numimpar.append(c)
    print(f'{c}...', end='')

print(f'\nTemos a lista par formada por {numpar}\nTemos lista impar formada por {numimpar}\n')
'''

#6)
expressão=str(input('Informe a expressão: '))
lista=[]

for simb in expressão:
    if simb=='(':
        lista.append('(')
    elif simb==')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append('  ')
            break
if len(lista)==0:
    print('SUA EXPRESSÃO ESTA CORRETA')
else:
    print('SUA EXPRESSÃO ESTÁ INCORRETA')


