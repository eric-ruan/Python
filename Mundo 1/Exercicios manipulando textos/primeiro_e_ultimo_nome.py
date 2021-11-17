'''Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente'''

print('Digite seu nome completo: ')
nome = str(input()).strip().split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
