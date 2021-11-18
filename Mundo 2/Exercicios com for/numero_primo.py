'''Faça um programa que leia um número inteiro e diga se ele é ou não número primo'''
n = int(input('Digite um número: '))
total = 0

for i in range(1, n+1):
    if n % i == 0:
        print('\33[33m', end = ' ')
        total+=1
    else:
        print('\33[31m', end = ' ')
    print(i, end = ' ''\033[m')
print('\nO número {} foi divisível {} vezes...'.format(n,total))
if total == 2:
    print('E por isso ele é primo...')
else:
    print('E por isso ele não é primo...')