from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print(f'os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'o maior valor sorteado foi: {max(numeros)}')
print(f'o menor valor sorteado foi: {min(numeros)}')