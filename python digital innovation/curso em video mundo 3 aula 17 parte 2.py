#desafio1 programa que leia nome e peso de varias pessoas guardando tudo em uma lista e mostre quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as mais leves
#desafio2 programa onde o usuario pode digitar 7 valores numericos coloque-os em uma lista separados por pares e impares e mostre-os de forma crescente
#desafio3 programa que leia uma matriz de ordem 3 e preencha com os valores lidos no teclado
#desafio4 aprimorar o desafio anterior, mostrando a soma de todos os valores pares , a soma dos valores da terceira coluna e o maior valor da segunda linha
#desafio5 programa que ajude o jogador da megasena a criar palpites, perguntando quantos jogos serão gerados e sortear 6 numeros entre 1 e 60 cadastrando tudo em uma lista composta
#desafio6 programa que leia nome e 2 notas de varios alunos e guarde tudo em uma lista composta no final mostre o boletm mostrando o contendo a media de cada aluno e que possa mostrar individulamente as notas de cada aluno
import random
import time

#              RESOLUÇÃO
#1)
'''
pessoa=list()
galera=list()
saida=''
while saida!='S':
    pessoa.append(str(input('Informe o nome: ')))
    pessoa.append(int(input('Informe seu peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    saida=str(input('Deseja sair?[S/N]')).upper()
maiorp=menorp=galera[0][1]              #colocando como maior e menor peso o primeiro peso digitado na lista.
pesomaior=list()                        #caso tenha mais de uma pessoa com o maior peso guardar todos os nomes
pesomenor=list()                        #caso tenha mais de uma pessoa com o menor peso guardar todos os nomes
for p in galera:
    if p[1]>=maiorp:
        maiorp=p[1]
        pesomaior.append(p[0])
    if p[1]<menorp:
        menorp=p[1]
        pesomenor.append(p[0])
print(f'Na listagem chegamos a {len(galera)} pessoas cadastradas\nO maior peso foi {maiorp} correspondente a {pesomaior}\nO menor peso foi {menorp} correspondente a {pesomenor}')
'''
#2)
#guardar 7 valores dentro de uma lista composta por duas listas uma para pares e outra para impares
#primeira lista pares/segunda lista impares
'''
lista=[[],[]]
valor=0
for c in range(0,7):
    valor=int(input('Informe valor: '))
    if valor%2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(sorted(lista[0]),sorted(lista[1]))
'''
#3)
'''
matriz=[]
linha=[]
valor=0
for c in range(0,3):
    for d in range(0,3):
       valor=int(input(f'Valor [{c}][{d}]:'))
       linha.append(valor)
    matriz.append(linha[:])
    linha.clear()
for linha in matriz:
    for col in range(0,3):
        print(f'[{linha[col]}]', end='')
    print('\r')

print('FIM DO PROGRAMA')
'''
#4)
'''
matriz=[]
linha=[]
valor=pares=col3=0
for c in range(0,3):
    for d in range(0,3):
       valor=int(input(f'Valor [{c}][{d}]:'))
       linha.append(valor)
    matriz.append(linha[:])
    linha.clear()
for linha in matriz:
    for col in range(0,3):
        print(f'[{linha[col]}]', end='')
        if linha[col]%2==0:
            pares+=linha[col]
        if col==2:
            col3+=linha[col]
    print('\r')
print(f'A soma dos valores pares é {pares}\nA soma dos valores da terceira coluna é {col3}\nO maior valor na segunda linha é {max(matriz[1])}')
print('FIM DO PROGRAMA')
'''
#5)
'''
jogos=[]
aposta=[]
quantidade=int(input('Informe o número de jogos: '))
for c in range(0,quantidade):
    while (len(aposta)<6):
        numero=random.randint(1,60)
        while numero in aposta:
            numero=random.randint(1,60)
        aposta.append(numero)
    jogos.append(aposta[:])
    aposta.clear()
print('-='*18)
for x in range(0,(len(jogos))):
    print(f'{x+1}º jogo-->{sorted(jogos[x])}')
    time.sleep(1)
print('-='*18)
pri nt(10*' ','FIM DE PROGRAMA')
'''
#6)
'''
tabela=list()
aluno=list()
notas=list()
#é uma lista com termo composto por uma lista com um dos termos formados por ela sendo uma lista
saida=nome=''
nota=0


while saida!='S':
    nome=str(input('Informe o nome: '))             #COLETANDO O NOME DO ALUNO
    nota=int(input('Informe a primeira nota: '))      #COLETANDO A PRIMEIRA NOTA
    notas.append(nota)                              #GUARDANDO A PRIMEIRA NOTA NA LISTA DE NOTAS
    nota = int(input('Informe a segunda nota: '))     #COLETANDO A SEGUNDA NOTA
    notas.append(nota)                              #GUARDANDO A SEGUNDA NOTA NA LISTA DE NOTAS
    #JUNTANDO NOTAS E NOME EM APENAS UMA LISTA
    aluno.append(nome)                              #GUARDANDO O NOME DO ALUNO
    aluno.append(notas[:])                          #GUARDANDO AS NOTAS DO ALUNO
    tabela.append(aluno[:])                         #GUARDANDO O ALUNO NA TABELA DE ALUNOS
    aluno.clear()                                   #APAGANDO A LISTA, PARA QUE NA PRÓXIMA VEZ QUE CARREGAR ALUNO EM TABELA TER APENAS UM TERMO
    notas.clear()                                   #APAGANDO A LISTA, PARA QUE NA PRÓXIMA VEZ QUE CARREGAR NOTAS EM ALUNO TER APENAS UM TERMO
    saida=str(input('Desaja sair?[S/N]')).upper()   #PERGUNTA PARA SAIR OU NÃO.
media=0
saida=''
print('\tNU. ALUNO\t\t\t\tNOTAS')
for v,estudante in enumerate(tabela):
    for c in range(0,2):
        media+=(estudante[1][c])
    print(f'\t{v+1}   {estudante[0]}\t\t\t\t {media/2}',end='\n')
    media=0
unico=0
while saida!='S':
    unico=int(input('Qual aluno você deseja ver as notas[999 para sair]:'))
    unico-=1
    if unico==998:
        break
    else:
        for z in range(0,2):
            print(f'NOTA 1 = {tabela[unico][1][z]}')
'''