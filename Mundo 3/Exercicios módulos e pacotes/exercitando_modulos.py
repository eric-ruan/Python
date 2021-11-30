'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from moeda import *

num = float(input('Digite um valor: R$'))
desc = float(input('Digite o desconto: '))
acresc = float(input('Digite o acrescimo: '))

print(f'O valor digitado foi R${num:.2f}')
print(f'Com aumento de {acresc} fica em R${aumentar(num, acresc):.2f}')
print(f'Com o desconto de {desc} fica em R${diminuir(num, desc):.2f}')
print(f'O dobro é R${dobro(num):.2f}')
print(f'A metade é {metade(num):.2f}')