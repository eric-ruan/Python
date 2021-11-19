'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atigiram a maioridade e quantos já são maiores.'''
from datetime import date
ano = date.today().year
cont_maior = 0
cont_menor = 0

for i in range(1,8):
    print('Digite seu ano de nascimento da {}ª PESSOA: '.format(i))
    pessoa = int(input())
    idade = ano - pessoa
    if idade >= 21:
        cont_maior+=1
    else:
        cont_menor+=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_maior))
print('-=-'*20)
print('Ao todo tivemos {} pessoas menores de idade'.format(cont_menor))