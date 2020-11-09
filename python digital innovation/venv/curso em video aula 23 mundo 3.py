#desafio 1 construir uma função leia int e uma função leita float que permitam digito de um valor errado mostrando um erro.
#desafio 2 crie um programa em python que retorne se o site do pudim está acessivel
#desafio 3 programa que permite cadastrar nome e idade de pessoas em um arquivo de texto simples. O progroma vai ter 3 opões cadastrar uma pessoa nova, listar as pessoas cadastradas e sair



#       RESOLUÇÃO

#1)

def leia_int():
    while True:
        try:
            num=int(input('Digite o valor: '))
        except:
            print('O valor digitad {num} é invalido'.format(num))
        else:
            break
numero=leia_int()
print ('num')
