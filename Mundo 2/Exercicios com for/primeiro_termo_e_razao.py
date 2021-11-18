'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressao.'''
print('-=-'*10)
p = int(input('Digite o primeiro termo da PA: '))
print('-=-'*10)
r = int(input('Digite a razão: '))
print('-=-'*10)
decimo = p + (10-1) * r

for i in range(p, decimo + r, r):
    print(i, end = ' -> ')
print('Fim')