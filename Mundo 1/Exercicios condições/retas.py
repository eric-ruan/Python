'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.''' 
print('Digite o valor de 3 retas, vamos conferir se pode formar um triângulo!!')
r1 = float(input())
r2 = float(input())
r3 = float(input())

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Com essas 3 retas podemos formar um triângulo!')
else:
    print('Infelizmente não podemos formar um triângulo!')