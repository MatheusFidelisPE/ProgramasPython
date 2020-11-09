def lista_unidimensional(lista):
    lista_retornada=list()
    for c in lista:
        for x in c:
            lista_retornada.append(x)
    return lista_retornada


'''
lista=[[1,2,5,4,6],[15,5,9,8,78,3,4,0]]
retorno = lista_unidimensional(lista)
print(f'{lista}-->{len(lista[0])+len(lista[1])}\n{retorno}-->{len(retorno)}')
print('MESMOS TERMOS SÓ QUE UM EM MAIS DE UMA LISTA E OUTRO EM APENAS UMA LISTA')
'''
def dicionario_soma(dicionario):
    soma=0
    for values in dicionario.values():
        soma+=values
    return soma

#print(dicionario_soma({'numero1':3, 'numero2':4}))
def inverte_frase(frase):
    separada = frase.split()

    nova_palavra=list()
    frase_invertida=list()
    for x in separada:
        for c in range((len(x)-1),-1,-1):
            nova_palavra.append(x[c])

        palavrainvertida= ''.join(nova_palavra)
        print(palavrainvertida+' ',end='')
        nova_palavra.clear()
        frase_invertida.append(palavrainvertida+' ')

   # y = ' '.join(frase_invertida[0])


    return frase_invertida

'''
frase='MINHA PRIMEIRA TENTATIVA COM A FUNÇÃO INVERTE COISAS'
print(frase, '\n', inverte_frase(frase))
'''
import os
print('casa')
print(os.)