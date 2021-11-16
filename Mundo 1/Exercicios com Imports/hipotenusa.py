#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa

import math

print('Digite o valor do Cateto oposto: ')
co = float(input())
print('Digite o valordo Cateto adjacente: ')
ca = float(input())

print('O valor do Cateto Oposto {} com o valor do Cateto Adjacente {}, da o valor da hipotenusa de {:.2f}'.format(co, ca, math.hypot(co, ca)))