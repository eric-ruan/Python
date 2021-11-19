'''Crie um programa que leia uma frase e diga se ela é ou não
Palindromos são frases que lidas de trás para frente fica mesma coisa
ex: apos a sopa, a sacada da casa, etc'''

print('--------------- VAMOS VERIFICAR SE ALGUMA FRASE É UM PALINDROMO ---------------')
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso+=junto[i]
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é m palíndromo!')
