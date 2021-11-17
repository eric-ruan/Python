'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

print('Digita um número: ')
n1 = float(input())
n2 = float(input())
n3 = float(input())

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print('O primeiro número foi {}, o segundo {} e o terceiro {}.'.format(n1, n2, n3))
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
