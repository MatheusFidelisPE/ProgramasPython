# apresentar caracteristicas da leitura de uma variável

leitura =input('Digite algo:')

print(type(leitura))
#print(leitura.isalpha(), leitura.isnumeric(), leitura.isnumeric())
senumero = leitura.isnumeric()
sealpha=leitura.isalpha()
str='Minha casa amarela é AZUL'
if sealpha > 0:
    sealpha='ela tem mais que alpha numéricos'
print(sealpha)
numero=leitura.isalnum()
decimal=leitura.isdecimal()
digito=leitura.isdigit()
identificador=leitura.isidentifier()
veloci=leitura.islower()
espaco =leitura.isspace()
forma=str.casefold()
print(forma)