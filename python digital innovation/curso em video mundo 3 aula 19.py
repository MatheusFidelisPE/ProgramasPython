#desafio1--> programa que pegue o nome e media de um aluno e guardando a situação em um dicionario no final mostre o conteudo da estrutura na tela
#desafio2--> programa onde 4 jogadores jogue um dado. guarde os dados em um dicionario, depois guardar o dicionario em ordem sabendo que o vencedor tirou o maior numero do dado
#desafio3--> programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os em um dicionario se a CTPS for diferente de ZERO o programa também receberá o ano de contratação e o salario, calcule além da idade, com quantos anos a pessoa vai se aposentar
#para se aposentar é preciso 35 anos de contribuição
#
#desafio4--> programa que gerencie o aproveitamento de jogador de futebol. O programa vai recebrer o nome do jogador, quantas partidas ele disputou, depois ler a quantidade de gols feitos em cada jogo e tudo isso será guardado em um dicionario incluindo o total de gols feitos durante o campeonato
#desafio5--> programa que leia o nome, sexo e idade de varias pessoas, guardando cada uma em um dicionario e os dicionarios em uma lista. No final mostre, quantas pessoas foram cadastradas, a média de idade das pessoas, uma lista com todas as mulheres e uma lista com todas as pessoas com idade acima da média
#desafio6--> aprimore o 93 e agora funcione para varios jogadores e incluso detalhes de aproveitamento


#                               RESOLUÇÃO

#1)
'''
aluno=dict()
aluno['nome']=str(input('Informe o nome do aluno: '))
aluno['media']=float(input('Informe a media do aluno: '))
if aluno['media']>=7:
    aluno['situação']='APROVADO'
else:
    aluno['situação']='REPROVADO'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')
'''
#2)
#jogo de dado
'''
import operator
from random import randint
from time import sleep
jogada={'jogador 1':randint(1,6),
        'jogador 2':randint(1,6),
        'jogador 3':randint(1,6),
        'jogador 4':randint(1,6)
}
ordem=list()
for k,v in jogada.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ordem=sorted(jogada.items(), key=operator.itemgetter(1), reverse=True)          #Usando a funçao sorted podemos ordenar da forma que queira, key=operator.itemgetter(1) escolhe no dicionario o valor de randint(1,6) para ordenar a partir dele e o reverse=True determina uma ordem inversa
print('-='*30, '\n\tPOS.\tRANKING DOS MELHORES VALORES SORTEADOS')
pos=1
for k,v in enumerate(ordem):
    print(f'\t{pos}º\tO {v[0]} sorteou {v[1]}')
    pos+=1
    sleep(1)
print('-='*30)
'''
#3)
'''
import datetime
dia=''

dados=dict()
dados['nome']=str(input('Informe seu nome: '))
dados['nascimento']=str(input('Informe data nascimento:[dd/mm/aaaa] '))
dados['ctps']=int(input('Informe sua CTPS: '))
#separando em dias, meses e anos.

dia=int(dados['nascimento'][0:2])
mes=int(dados['nascimento'][3:5])
ano=int(dados['nascimento'][6:])
dia_atual=datetime.date.today()
anoatual=dia_atual.year
mesatual=dia_atual.month
diaatual=dia_atual.day
#calculo de idade

if mesatual<mes:
    dados['idade']=(anoatual-ano)-1
elif mesatual==mes:
    if diaatual<dia:
        dados['idade'] = (anoatual - ano) - 1
    else:
        dados['idade']=(anoatual - ano)
else:
    dados['idade']=(anoatual-ano)

del dados['nascimento']

if dados['ctps']==0:
    print('-=' * 30, '\n\t\t','=>' * 6, 'DADOS', '<=' * 6)
    for k,v in dados.items():
        print(f'\t{k} é {v}  ')
else:

    dados['salario']=float(input('Informe seu salario: '))
    dados['contrato']=int(input('Ano de contrato: '))
    dados['idade de aposentadoraia']=dados['contrato']-ano+35
    print('-=' * 30,'\n\t\t','=>'*6,'DADOS','<='*6)
    for k,v in dados.items():
        print(f'\t{k} é {v}')
'''
#4)SOCCER PLAYER
'''
tudo=dict()
gols=list()
total=0
tudo['O nome é']=str(input('Nome do jogador: '))
tudo['Disputou']=int(input('Número de partidas jogadas:'))
for c in range(0,tudo['Disputou']):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    total+=gols[c]
tudo['gols_partida']=gols[:]
tudo['total de gols']=total
print('-='*7,f'RENDIMENTO DE {tudo["O nome é"]}','=-'*7)
for k,v in tudo.items():
    if k=='gols_partida':
        for x,y in enumerate(tudo['gols_partida']):
            print(f'\t=>Na partida {x+1} {tudo["O nome é"]} fez {y} gols')
    elif k=='Disputou':
        print(f'{tudo["O nome é"]} disputou {tudo["Disputou"]} partidas')
    else:
        print(f'{k} {v}')
print(f'{tudo["O nome é"]} teve um aproveitamento de {total/tudo["Disputou"]:.2f} gols por partida')
'''
#desafio5--> programa que leia o nome, sexo e idade de varias pessoas, guardando cada uma em um dicionario e os dicionarios em uma lista.
# No final mostre, quantas pessoas foram cadastradas, a média de idade das pessoas,
# uma lista com todas as mulheres e uma lista com todas as pessoas com idade acima da média
'''
pessoa=dict()
galera=list()
mulheres=list()
acima=list()

saida=''
media=count=0
while True:
    pessoa['nome']=str(input('\nInforme seu nome: ')).upper()
    pessoa['sexo']=str(input('Informe seu sexo: ')).upper()
    while pessoa['sexo']!='F' and pessoa['sexo']!='M':
        pessoa['sexo'] = str(input('Valor incorreto\nInforme seu sexo: ')).upper()
    pessoa['idade']=int(input('Informe sua idade: '))

    media+=pessoa['idade']                                      #SOMANDO AS IDADES DAS PESSOAS PARA SE TER UMA MÉDIA

    if pessoa['sexo'] == 'F':                                   #CRIANDO UMA LISTA DE MULHERES
        mulheres.append(pessoa['nome'])

    galera.append(pessoa.copy())

    saida=str(input('Desaja continuar?[S/N]')).upper()
    if saida=='N':
        break
print('-='*20)
print(f'\t=>Foram cadastradas {len(galera)} pessoas\n\t=>Tendo média de idade igual a {media/len(galera):.2f}')
print('--'*20,'\nLISTA DE MULHERES: ')
for x in galera:
    if x['idade'] > media / len(galera):
        acima.append(x['nome'])

    if x['sexo']=='F':
        print(f'\t=>{x["nome"]}')
print('--'*20,'\nLISTA DE PESSOAS ACIMA DA MÉDIA DE IDADE: ')
for z in acima:
    print(f'\t=>{z}')
print('--'*20)
'''
#6)aprimore o 93 e agora funcione para varios jogadores e incluso detalhes de aproveitamento
'''
tudo=dict()
gols=list()
total=0
jogadores=list()
sair=''
while True:
    tudo['nome']=str(input('Nome do jogador: '))
    tudo['partidas']=int(input('Número de partidas jogadas: '))
    for c in range(0,tudo['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
        total+=gols[c]
    tudo['gols_partida']=gols[:]
    tudo['total de gols']=total

    gols.clear()
    total=0

    jogadores.append(tudo.copy())
    sair=str(input('Desaja sair?[S/N]')).upper()
    if sair=='S':
        break
#printar uma tabela mostrando um indice para cada jogador,
# o nome do jogador, a lista dos gols e a quantidade de partidas jogadas
print('-='*33)
print(f'{"NUM":^10}{"JOGADOR":^16}{"LISTA DE GOLS":^20}{"JOGOS":>20}')
variavel=''
for c,v in enumerate(jogadores):
    variavel=','.join(map(str,v["gols_partida"]))
    print(f'{c+1:^10}{v["nome"]:^16}{variavel:^20}{v["partidas"]:>18}')
    print('--'*33)
while True:                                                                 #escolher um jogador para se printar
    escolha=int(input('Qual jogador deseja ver o desempenho?[999 para sair]'))
    if escolha==999:
        break
    if escolha>len(jogadores):
        print(f'{"DIGITAR VALOR VALIDO!!" :^66}')
    else:
        escolha -= 1
        for c,v in enumerate(jogadores[escolha]['gols_partida']):
                print(f'jogo {c+1}--> {jogadores[escolha]["nome"].upper()} fez {v} gols ')
        print('--' * 33)
print("TERMINO DO PROGRAMA!!!".center(66))
print('-='*33)
'''
