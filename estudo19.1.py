estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla']= str(input('sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for e in e.values():
        print(v, end=' ')
    print()
    