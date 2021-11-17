#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print('Digite um número qualquer entre 0 e 9999: ')
numb = int(input())

print('O número digitado foi: {}'.format(numb))
print('A unidade é: {}'.format(numb//1 %10))
print('A dezena é: {}'.format(numb//10 %10))
print('A centena é: {}'.format(numb//100 %10))
print('O milhar é: {}'.format(numb//1000 %10))