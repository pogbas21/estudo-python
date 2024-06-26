def area(larg, comp):
    a = larg * comp
    print(f'a area de um terreno {larg}x{comp} e de {a}')


print('controle de terrenos')
print('-' * 20)
l = float(input('largura (m):'))
c = float(input('comprimento (m):'))
area(l, c)
