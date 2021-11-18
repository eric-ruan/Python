'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
n6 = int(input('Digite o sexto número: '))

lista = [n1, n2, n3, n4, n5, n6]
cont = 0

for i in lista:
    if i % 2 == 0:
        print(i, end = ' - ')
        cont+=i
print('O resultado é -> {}'.format(cont))
