def aumentar(valor,percent, formatação=False):
    if formatação:
        valor = valor * (1 + percent / 100)
        return formata(valor)

    return valor *(1+percent/100)


def diminuir(valor, percent,formatação=False):
    if formatação:
        valor = valor * (1 - percent / 100)
        return formata(valor)

    return valor * (1-percent/100)


def dobrar(valor, formatação=False):
    if formatação:
        valor = valor *2
        return formata(valor)

    return valor*2


def metade(valor, formatação=False):
    if formatação:
        valor = valor /2
        return formata(valor)

    return valor/2


def formata(valor):
    return f'R${valor:.2f}'

def lin():
    linhas='-='*16
    print(f'{linhas:^40}',end='')
    print()


def resumo(valor, percent_mais, percent_menos, formatação=False):
    lin()
    print(f'{"RESUMO DE DADOS":^40}')
    lin()
    print(f'{" OPERAÇÃO                            FINAL":^40}')
    print('1.AUMENTO',f'{aumentar(valor,percent_mais,formatação):>33}')
    print(f'2.DESCONTO',f'{diminuir(valor,percent_mais,formatação):>32}')
    print(f'3.DOBRO',f'{dobrar(valor,formatação):>35}')
    print(f'4.METADE',f'{metade(valor,formatação):>34}')
