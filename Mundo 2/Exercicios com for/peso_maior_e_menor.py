'''Crie um programa que leia o peso de cinco pessoas. No final, mostre qual foi 
o maior e o menor peso lido.'''

maior = 0
menor = 0
for i in range(1,6):
    print('------------- {}ª PESSOA -------------'.format(i))
    peso = float(input('Digite seu peso Kg: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('A pessoa com maior peso tem {}Kg'.format(maior))
print('A pessoa com menor peso tem {}Kg'.format(menor))