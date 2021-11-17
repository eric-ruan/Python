'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas. 
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

print('Digite seu nome: ')
nome = str(input()).strip()

print('SEU NOME EM LETRAS MAIUSCULAS, {}'.format(nome.upper()))
print('seu nome em letras minusculas, {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))