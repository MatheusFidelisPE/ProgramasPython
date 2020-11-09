import os
import sys
import platform


def ud():

    us = {'Windows': 'USARNAME',
          'Linux': 'USER'}
    u = us.get(platform.system())
    return os.environ.get(u)



print(f'usuario--> {ud()}')
print(f'plataforma: {platform.platform(os.curdir)}')
print(f'diretório corrente: {os.path.abspath(os.curdir)}')
print(f'executavel: {os.path.split(sys.executable)}')