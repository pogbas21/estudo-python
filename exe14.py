num = [[], []]
valor = 0
for c in range(1,8):
    valor= int(input('digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-' * 30)
print( f'os valores pares digitados foram: {num[0]}')
print(f'os valores impares digitados foram: {num[1]}')
