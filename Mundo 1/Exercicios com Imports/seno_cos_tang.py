#Faça um programa que leia um valor qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
print('Digite um valor qualquer para calcularmos seu seno, cosseno e tangente: ')
n = float(input())
sen = math.radians(n)
cos = math.radians(n)
tan = math.radians(n)

print('O valor digitado foi {:.2f}\nSeu seno é de {:.2f} \nSeu cosseno é de {:.2f} \nE sua tangente é de {:.2f}'.format(n, math.sin(sen), math.cos(cos), math.tan(tan)))