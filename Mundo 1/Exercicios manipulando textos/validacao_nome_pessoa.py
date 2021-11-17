#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('Digite seu nome: ')
nome = str(input()).upper()

print('Seu nome tem Silva? ', 'SILVA' in nome)