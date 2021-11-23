'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = (int(input('Digite o primeiro número: ')), 
int(input('Digite o segundo número: ')), 
int(input('Digite o terceiro número: ')), 
int(input('Digite o quarto número: ')))
print(tupla)

#a)
print(f'O número 9 aparece {tupla.count(9)} vezes')
#b)
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado...')
print('Os valores pares digitados foram: ', end = '')
for i in tupla:
    if i % 2 == 0:
        print(i, end = ' ')