cont = ('um, dois, três, quatro, cinco, seis, sete, oito, nove, dez, onze, doze, treze, catorze, quinze, dezesseis, dezessete, dezoito, dezenove, vinte')

while True:
        num= int(input('digite um numero entre 1 e 20:'))
        if 0<= num <=20:
           break
        print('tente novamente.',end=' ')
print(f'voce digitou o numero{cont[num]}')
