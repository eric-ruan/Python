'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longe.'''

print('Quantos Km terá a viagem?')
km = float(input())

if km <= 200:
    valor = km * 0.50
    print('O valor a ser gasto será de R${:.2f}'.format(valor))
else:
    valor = km * 0.45
    print('O valor a ser gasto será de R${:.2f}'.format(valor))
