from random import randint
lista = list()
print('-' * 30)
print('       JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('quantos jogos voce quer q eu sortei'))
while True:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
print(f'os numeros sorteados foram {lista}')
