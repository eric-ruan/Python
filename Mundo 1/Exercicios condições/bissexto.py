'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
print('Digite um ano: ')
ano = int(input())

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É ano bissexto!')
else:
    print('Não é ano bissexto!')