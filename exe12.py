valores = []
while True:
    valores.append(int(input('digite um valor:')))
    resp= str(input('quer continuar? {s/n}'))
    if resp in 'Nn':
        break
print('-' * 30)
print(f'voce digitou {len(valores)} elementos.')
