from datetime import datetime
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
idade = datetime.now().year - nasc
dados ['ctps'] = int(input('cateira de trabalho(0 não tem):'))

print(dados)
print(nasc)