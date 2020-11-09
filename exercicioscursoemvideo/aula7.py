#+ para soma
#- para subtração
#* para multiplicação
#/ para divisão
#** para potenciação
#// para divisão inteira
#% para o resto  da divisão

#ORDEM DE PROCEDENCIA
'''
1º()-> Os parenteses são executados primeiro
2º**-> As potencias são as segundas na ordem de execução
3º */%//->São os terceiros a ser executados
4º+- -> São os ultimos na ordem das operações
'''
#PRÁTICA DA AULA 7
#nome =input('Qual é seu nome')
#print('prazer em te conhecer {:-^s20}'.format(nome))

n1=int(input('Um valor'))
n2=int(input('Outro valor'))
s=n1+n2
m=n1*n2
d=n1/n2
e=n1**n2

#DESAFIO 1

suce=n1+1
ante=n1-1
print('O sucessor de {} é {} e o antecessor é {}'.format(n1,suce,ante))

#DESAFIO 2
dobro=n1*2
triplo=n1*3
raiz=n1**(1/2)

print('O dobro de {} é {}, o triplo é {} e a sua raiz quadrada é {}'.format(n1, dobro,triplo,raiz))

#DESAFIO 3


n1=int(input('Digite a primeira nota do aluno:'))
n2=int(input('Digite a segunda nota do aluno:'))

media=(n1+n2)/2

print('O aluno tem média igual a {}'.format(media))

#DESAFIO 4

n1=int(input('Digite o valor em metros:'))

cm=100*n1
mm=n1*1000

print('{} metros equivalem a {}cm e a {}mm'.format(n1,cm,mm))

#DESAFIO 5

n1=int(input('Digite o numero que você deseja a tabuada de 0 a 10:'))
#print('TABUADA DE {0} {1}*1={2}'.format(n1,n1*2,n1*3))

print('TABUADA DE {0}\n {0}*0={1}\n {0}*1={2}\n {0}*2={3}\n {0}*3={4}\n {0}*4={5}\n {0}*5={6}\n {0}*6={7}\n {0}*7={8}\n {0}*8={9}\n {0}*9={10}\n {0}*10={11}\n'.format(n1,n1*0,n1*1,n1*2,n1*3,n1*4,n1*5,n1*6,n1*7,n1*8,n1*9,n1*10))

#DESAFIO 6
n1=float(input('Quanto dinheiro você tem na carteira?'))
dolar=n1/4.14

print('Voce pode comprar até {} dolares'.format(dolar))

#DESAFIO 7
n1=float(input('Qual a altura da parede?'))
n2=float(input('Qual a largura da parede?'))

area=n1*n2
tinta=area/2


print('Você precisará de {} litros de tinta para pintar a parede'.format(tinta))

#DESAFIO 8

n1=float(input('Qual o preço do produto?'))
desconto=(n1/100)*95

print('O produto terá um desconto de 5% e ficará por {}'.format(desconto))

#DESAFIO 9

n1=float(input('informe o seu salario:'))

aumento=1.15*n1

print('O seu salario terá novo valor de {}'.format(aumento))


