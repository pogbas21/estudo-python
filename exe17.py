from random import randint
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')