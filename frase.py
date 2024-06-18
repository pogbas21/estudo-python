from random import randint
numeros =(randint(1, 100) ,randint(1, 100) ,randint(1, 100) ,randint(1, 100) ,randint(1, 100))
print(f'os valores soerteados foram: ',end='')
for n in numeros:
    print(f'{n}', end='')
print(f'o maior valor sorteado foi: {max(numeros)}')
print(f'o menor valor sorteado foi: {min(numeros)}')