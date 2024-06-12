galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear()
    
    for p in galera:
        if p[1]>=21:
            print(f'{p[0]} e maior de idade.')
            
            print(f'{p[0]} e menor de idade.')
            totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade.')
