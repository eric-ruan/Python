#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math 
print('Digite um número Real qualquer: ')
n = float(input())

print('A parte inteira desse número é: {}'.format(math.trunc(n)))
print('A parte inteira desse número arredondada para cima é: {}'.format(math.ceil(n)))
print('A parte inteira desse número arredondada para baixo é: {}'.format(math.floor(n)))