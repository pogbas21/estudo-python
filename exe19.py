jogador = dict()
partidas = list()
jogador['nome']= str(input('nome do jogador:'))
tot = int(input (f'quantas partidas {jogador["nome"]} jogou?'))
for c in range(tot):
    partidas.append(int(input(f'quantos gols na partida{c+1}?')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)