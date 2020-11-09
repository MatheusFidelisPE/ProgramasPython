#            Cadeias de caracteres
#cadeia de caracteres é um conjuto de caracteres
#mas ela também é chamada de string de caracteres

# frase='curso em video python'---> 21 caracteres cada caractere é guradado em um índice
#[x:x] o primeiro valor representa o primeiro indice do intervalo e o segundo valor significa ultimo indice do intervalo
#[:x] ouc[x:] o primeiro expressa que será pego so primeiro indice até x e o segundo de x até o ultimo caractere
#[x:x:x] o primeiro siginifica o inicio do intervalo o segundo o termino e o terceiro o número de casas que serão puladas até o proximo índice
#a função len() retorna o tamanho da string
#a função .count(x) conta quantas quantas letras x há na string
#.count('o',X,X) faz o fateamento da string e retorna e conta o número de o
#.find('vid') procura quantos 'vid' tem na string
#quando .find()recebe uma string que não tem na string maior ele retorna o valor -1
#.replace('casa','carro') essa função substitui casa por carro
#.upper() coloca as letras da string em maiusculas
#.lower() coloca todas as letras em minusculo
#.captalize() coloca todos os caracteres para minusculo e só a primeira letra fica em maiusculo
#.title()coloca todas as primeiras letras das palavras em maiusculo
#.strip() remove os espaços no começo da string e no final também
#.rsrtip()remove os espaços do fim da string
#.lstrip()remove os espaços do inicio da string
#.split()divide a string nos espaços formando novas strings e recolocandoas em uma lista
#.join(frase)
#
#
#
'''
frase='curso em video python'

print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('vid'))
print(frase.find('ANDROID'))
print('curso' in frase)
print(frase.replace('python','android')
)

frase='   Aprenda Python  '
print(frase)
print(len(frase))
print(len(frase.strip()))


frase='Curso em Video Python'
print(frase.join(frase))
print(frase.split())
print(' '.join(frase))
'''
#Desafio 1 ---> Manipulando uma string

'''''''''''
nome=input('Digite seu nome: ')
print(nome.upper())
print(nome.lower())
nome= nome.strip()
espaços=nome.count(' ')
print(espaços)
numerodenomes=len(nome)-espaços
print('Seu nome tem ',numerodenomes,'letras sem espaço')
primeironome=nome.split()
print('O primeiro nome tem ',len(primeironome[0]),'letras')
'''''''''''
#Desafio 2---> separar o numero em unidades, dezenas, centenas e milhar

'''''''''
num=input('Digite um numero de 0 a 9999')
dividir=num.split()
print(dividir)
print('Unidade:{}\nDezana:{}\nCentena:{}\nMilhar:{}\n'.format(num[3],num[2],num[1],num[0]))
'''''''''''
#Desafio 3---> mostando se a cidade da pessoa tem santo no nome

'''''''''''
cidade=input('Informe o nome da sua cidade: ')
cidade = cidade.lower().strip()
print(cidade[:6].lower()== 'santo ')
'''''''''''
#Desafio 4 ---> mostrando se tem silva no nome

'''''''''''
nome=input('Diga seu nome: ')
nome=nome.lower()
silva=nome.find('silva')
if silva!=-1:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem silva')
'''''''''''
#Desafio 5---> contador de A

'''''''''
frase=input('Digite uma frase: ')
frase=frase.lower()
qt=frase.count('a')
primeiravez=frase.find('a')
ultimavez=frase.rfind('a')
print(len(frase))
print('A frase tem {}, a primeira vez que aparece a letra A é na posição {} e a ultima vez que ela aparece é {}'.format(qt,primeiravez,ultimavez))
'''''''''''
