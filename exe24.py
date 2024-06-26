from random import randint
from time import sleep


def sorteio(list):
    print('sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
         n = randint(1, 10)
         list.append(n)
         print(f'{n}', end='', flush=True)
         sleep(0.3)
         print('pronto!')


def somaPar(list):
     soma = 0
     for valor in list:
          if valor % 2 == 0:
               soma+= valor
     print(f'somando os valores pares de {list}, temos {soma}')

numeros = list()
sorteio(numeros)
somaPar(numeros)