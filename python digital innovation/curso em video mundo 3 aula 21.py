#desafio 1 programa que tenha uma função chamada voto()que recebe o ano de nascimento de uma pessoa e retorne valor  literal informando se a pessoa tem voto negado, opcional ou obrigatório
#desafio 2 programa que tenha uma função fatorial que receba dois parametros o primeiro o numero a calcular o fatorial o outro chamado show que será valor lógico que escolhe se a pessoa deseja mostrar o processo do cálculo
#desafio 3 programa que tenha uma função chamada ficha() que receba dois parametros opcionais nome e gols de um jogador o programa devera informar a ficha mesmo que algum dado não tenha sido informado
#desafio 4 programa que tenha uma função leiaint() que vai ser semelhante a função input só que fazendo validação para só aceitar valor numerico
#desafio 5 programa que tenha uma função chamada notas() e retorna um dicionario com as seguintes informações, quantidade de notas, a maior nota, menor nota, a media da turma, a situação e adicionar docstrings
#desafio 6 programa faça um interactivHelp do python. o usuario vai digitar o comando e o manual vai aparecer quando o usuario digitar 'fim' o programa se encerra


#               RESOLUÇÃO

#1)
'''
import datetime

def voto(ano):
        """
        parameter ano: ano de nascimento da pessoa
        return: a situção perante o estado
        """
        data=datetime.date.today()
        ano_atual=data.year
        if ano_atual-ano<16:
            return 'NEGADO'
        elif 18<=ano_atual-ano<65:
            return 'OBRIGATÓRIO'
        else:
            return 'OPCIONAL'


ano=int(input('Ano de nascimento: '))
print(f'SUA RELAÇÃO COM O VOTO É {voto(ano)}')
help(voto)
'''
#2)
'''
def fatorial(numero, exib=False):
    fat=1
    if exib==True:
        for c in range(numero, 0, -1):
            print(f'{c}', end='')
            if c>1:
                print('*',end='')
            fat*=c
        print(f'={fat}')
    else:
        for c in range(numero, 0, -1):
            fat*=c
        print(f'FATORIAL={fat}')

num=int(input('INFORME O VALOR: '))
exibir=bool(input('DESEJA EXIBIR O CONTEUDO?'))
fatorial(num,exibir)
'''

#3)
'''
def ficha(nome,gols):
    if len(nome)==0:
        nome='<Desconhecido>'

    if len(gols)==0:
        gols=0


    print(f'O jogador {nome} fez {gols} gols no campeonato')

nome_jogador=str(input('Nome do jogador: '))
gols=(input('Quantidade de gols marcados: '))
ficha(nome_jogador,gols)
'''
#4)
'''
def leiaint():
    numero1=cont=0
    numero=''

    while True:

        numero=str(input('Número: '))

        for c in numero:
            if c in'1234567890':
                cont+=1
        if len(numero)==cont:
            numero1 = int(numero)
            print('-='*9)
            print(type(int(numero1)))
            print(f'NÚMERO VÁLIDO-->{int(numero)}\n{int(numero)}+5={int(numero) + 5}')
            print(type(numero1))
            break
        else:
            print('VALOR INVALIDO')

    return numero1

valor=0
valor=leiaint()
print(type(valor))
'''
#5)
'''
def notas(*notas,sit=False):
    """
    :parameter: A função recebe uma variável empacotada, que tem todas as notas.
    :return: Print da quantidade de notas, maior nota, menor nota, a média e a situação
    """
    fich=dict()
    fich['quantidade']=len(notas)
    fich['maxima nota']=max(notas)
    fich['minima nota']=min(notas)
    fich['somatorio']=sum(notas)
    if sit:
        if fich['somatorio']/fich['quantidade']>=7:
            fich['situação']='APROVADO'
        elif fich['somatorio']/fich['quantidade']<4:
            fich['situação']='REPROVADO'
        else:
            fich['situação']='RECUPERAÇÃO'
    return fich


    print(f'Foram informadas {len(notas)}\nA maior nota foi {max(notas)}\nA menor nota foi {min(notas)}\nA média da turma foi {sum(notas)/len(notas)}')

    if sum(notas)/len(notas)>=7:
        print(f'O ESTUDANTE ESTÁ APROVADO')
    elif sum(notas)/len(notas)<4:
        print(f'O ESTUDANTE ESTÁ REPROVADO')
    else:
        print('O ESTUDANTE ESTÁ EM RECUPERAÇÃO.')



print(notas(4,5,8.6,6,2.2))

'''
#6)
'''
def helpi(instrução):
    help(instrução)


função=''
while True:
    função=str(input('Qual função deseja o help? '))
    if função=='fim':
        print('OBRIGADO POR USAR O NOSSO PROGRAMA. \n\t\tATÉ A PRÓXIMA')
        break
    helpi(função)
'''


