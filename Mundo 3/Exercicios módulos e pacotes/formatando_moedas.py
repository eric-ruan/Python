'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.'''
from moeda_parte_2 import *
num = float(input('Digite um valor: R$'))
desc = float(input('Digite o desconto: '))
acresc = float(input('Digite o acrescimo: '))

print(f'O valor digitado foi {moeda(num)}')
print(f'Com aumento de {acresc} fica em {moeda(aumentar(num, acresc))}')
print(f'Com o desconto de {desc} fica em {moeda(diminuir(num, desc))}')
print(f'O dobro é {moeda(dobro(num))}')
print(f'A metade é {moeda(metade(num))}')