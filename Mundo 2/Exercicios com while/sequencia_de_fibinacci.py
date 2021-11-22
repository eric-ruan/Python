#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
print('-=-'*20)
print('Sequência de Fibonacci')
print('-=-'*20)
n = int(input('Quer fazer uma sequência de quantos termos? '))
n1 = 0
n2 = 1
print('{} -> {}'.format(n1, n2), end = '')
cont = 3

while cont <= n:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end = '')
    n1 = n2
    n2 = n3
    cont += 1
print(' *')
0 - 1 - 1 - 2 - 3 - 5 - 8 - 13