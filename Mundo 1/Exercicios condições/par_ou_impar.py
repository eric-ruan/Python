'''Crie um programa que leia um número inteiro e mostre na tela
se ele é par ou impar.'''

print('Digite um número qualquer, vamos verificar se é par ou ímpar...')
numb = int(input())

if numb % 2 == 0:
    print('O número digitado é par!')
else:
    print('O número digitado é ímpar!')