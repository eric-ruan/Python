'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar
- se é a hora de se alistar
- se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
data = date.today().year

print('Em que ano você nasceu?')
ano_nasc = int(input())

if (data-ano_nasc) < 18:
    print('Você ainda vai se alistar, quando completar 18 anos.')
    tempo_rest = 18 - (data-ano_nasc)
    print('Falta {} anos'.format(tempo_rest))

elif (data-ano_nasc) == 18:
    print('Está na hora de se alistar.')

else:
    print('Você já passou do prazo de alistamento')
    tempo_passado = (data-ano_nasc) - 18
    print('Já se passaram {} anos do prazo!!'.format(tempo_passado))