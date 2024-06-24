aluno = dict()
aluno['nome'] = str(input(str('nome: ')))
aluno['media'] = float(input(f' media de {aluno['nome']}:'))
if aluno ['media'] >= 7:
    aluno ['situação'] = 'aprovado'
elif 5<= aluno ['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno ['situação'] = 'reprovado'

print(aluno)
for k, v in aluno.items():
    print(f'{k} e igual a {v}')
