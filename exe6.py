num = (int(input('digite um numero: '))),(int(input('digite um numero: '))),(int(input('digite um numero: '))),(int(input('digite um numero: '))),
print(f'voce digitou os valores {num}')
print(f'o valor 9 aparceu {num.count(9)} vezes')
print(f'o numero 3 apareceu na {num.index(3)}ª')
print(f'os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')