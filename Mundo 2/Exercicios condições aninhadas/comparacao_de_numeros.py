'''Escreva um programa que leia dois números inteiros e compare-os, mostrando
na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais'''

print('Digite o primeiro número, vamos comparar: ')
n1 = int(input())
print('Digite o segundo número: ')
n2 = int(input())

if n1 > n2:
    print('O primeiro valor é maior!!!')
elif n1 < n2:
    print('O segundo valor é maior!!!')
else:
    print('Não existe valor maior, os dois são iguais!!!')