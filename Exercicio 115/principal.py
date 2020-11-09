import cores as c


'''
mensagem=str(input('Qual a mensagem? ')).upper()

c.cores_letra(opções=True)
cor_letra= str(input('cor da letra? ')).lower()

c.cores_fundo(opções=True)
cor_fundo=str(input('Cor do fundo? ')).lower()

c.estilo_letra(opções=True)
estilo_letra=str(input('Estilo da letra? ')).lower()

print(menu.print_menu(), '\n')
print(c.pintura(letra=c.estilo_letra(estilo_letra),fundo=c.cores_fundo(cor_fundo),cortexto=c.cores_letra(cor_letra),msg=mensagem))
'''
arquivo = open('lista.txt','r')
conteudo=arquivo.readlines()
pessoa=dict()
while True:
    print('-=' * 10)
    print(f'{"MENU":^20}')
    print('-=' * 10)
    print('1-LISTAR PESSOAS\n2-ADICIONAR PESSOAS\n3-SAIR')
    escolha=int(input('ESCOLHA- '))
    if escolha==1:
        print(conteudo)
    if escolha==2:
        nome=str(input('INFORME O NOME: '))
        conteudo.append(nome[:])
        idade=int(input('INFORME A IDADE: '))
        conteudo.append(idade)
        pessoa.clear
    if escolha == 3:
        arquivo = open('lista.txt', 'w')
        arquivo.writelines(conteudo)

arquivo.close()






