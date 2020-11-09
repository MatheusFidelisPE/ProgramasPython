# Utilizando modulos

#importação de bibliotecas
import math
import random
from random import randint
# quando importar a biblioteca da forma import biblioteca usa-se a função dessa forma biblioteca.função(variavel)
# Quando importar a biblioteca na forma from biblioteca import função usa-se a função dessa forma função(variavel)
'''
num=int(input('Digite um numero:'))
raiz=math.sqrt(num)
print('a raiz de {} é {:.3f}'.format(num,raiz))
num=0
num =random.randint(1,20)
print(num)
'''
#Desafio 1 --->retirando os numeros após a vírgula
''' 
num=float(input('Digite um número dom casas após a virgula.'))

num_semdecimal= math.floor(num)
print('O número {} tem esse valor sem os valores após a vírgula {}' .format(num, num_semdecimal))

'''

#Desafio 2 --->Calculando o valor da hipotenusa

'''
cat1=float(input('Digite o valor do cateto oposto: '))
cat2=float(input('Digite o valor do cateto adjacente: '))
hipotenusa=math.hypot(cat1,cat2)

print('Com o cateto oposto medindo {} e o cateto adjacente medindo {} a hipotenusa mede {}'.format(cat1,cat2,hipotenusa))
'''

#Desafio 3 --->escrevendo o valor de seno, cosseno, tangente.

'''

num=int(input('Digite o ângulo:'))
sen=math.sin(num)
cos=math.cos(num)
tan=math.tan(num)

print('\tO ângulo de {}º\n tem valor de seno = {}\n valor de cosseno = {}\n valor de tangente = {}'.format(num, sen, cos, tan))
'''
#Desafio 4 --->escolhendo uma pessoa


nome1=input('Digite o nome do primeiro aluno:')
nome2=input('Digite o nome do segundo aluno:')
nome3=input('Digite o nome do terceiro aluno:')
nome4=input('Digite o nome do quarto aluno:')

escolhido=random.choice([nome1,nome2,nome3,nome4])
print('O escolhido foi {} '.format(escolhido))


#Desafio 5 --->
'''''
nome1=input('Digite o nome do primeiro aluno:')
nome2=input('Digite o nome do segundo aluno:')
nome3=input('Digite o nome do terceiro aluno:')
nome4=input('Digite o nome do quarto aluno:')
nome5=input('Digite o nome do quinto aluno:')
nome6=input('Digite o nome do sexto aluno:')

lista=[nome1,nome2,nome3,nome4,nome5,nome6]
random.shuffle(lista)
print(lista)
'''


#Desafio 6 ---> Reprodução de uma musica
import pygame
import os
#inicializando o pygame
pygame.init()

if os.path.exists('FRONTEIRA.mp3'):
    pygame.mixer.music.load('FRONTEIRA.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock=pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo ORappa_Fronteira.mp3 não está disponível no diretório do script python')
'''''

import playsound

playsound.playsound('aonde_quer_que_eu_va.mp3')



import pygame
pygame.init()
print('Vamos lá para uma musiquinha')
pygame.mixer.music.load('FRONTEIRA.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('Fim da musica!!')

'''