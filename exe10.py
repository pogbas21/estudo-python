numeros =list ()
while True:
    n = int(input('digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso')
    else:
        print('valor duplicado! não vou adicionar...')
    r = str(input('quer continuar?[s/n]'))
    if r in 'Nn':
            break
print('-' * 30)
print(f'voce digitou os valores {numeros}')
