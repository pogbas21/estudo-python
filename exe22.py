from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} ate {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
            print('fim')
    else: 
        cont = i
        while cont >= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont -= p
            print('fim')

contador(0,100,10)
contador(10,0,2)