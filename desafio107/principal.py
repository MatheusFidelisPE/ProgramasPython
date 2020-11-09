#-->desafio 1 criar um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar, diminuir, dobrar e metade, faça também um programa que importe essas funções
#-->desafio 2 adapte o código criando uma função adicional chamada de moeda que
# consiga mostrar todos os valores como um valor monetário formatado
#-->desafio 3 modifique as funções craiadas no desafio 1 para que elas aceitem um parametro a mais,
# informando se o valor vai ser formatado pela função moedadesenvolvida no exercicio 2
#-->desafio 4 adicione ao modulo moeda.py uma função chamada resumo, que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui



from UtilidadesCeV import moeda
from UtilidadesCeV import dados
from time import sleep

quantia=dados.leitura_float()

print(f'Dado um aumento de 25% à quantia {moeda.formata(quantia)}, chegamos a uma valor de {moeda.aumentar(quantia,25)}.')
sleep(1)
print(f'Dado um desconto de 15% à quantia {moeda.formata(quantia)}, chegamos a um valor de {moeda.diminuir(quantia,15)}.')
sleep(1)
print(f'O dobro de {moeda.formata(quantia)} é {moeda.dobrar(quantia,True)}')
sleep(1)
moeda.resumo(quantia,25,15,True)
