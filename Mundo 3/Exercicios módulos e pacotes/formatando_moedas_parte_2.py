'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from formatando_moeda import *
num = float(input('Digite um valor: R$'))
desc = float(input('Digite o desconto: '))
acresc = float(input('Digite o acrescimo: '))

print(f'O valor digitado foi {moeda(num)}')
print(f'Com aumento de {acresc} fica em {aumentar(num, acresc, True)}')
print(f'Com o desconto de {desc} fica em {diminuir(num, desc, True)}')
print(f'O dobro é {dobro(num, True)}')
print(f'A metade é {metade(num, True)}')