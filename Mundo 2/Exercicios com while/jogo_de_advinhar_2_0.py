'''Melhore o jogo onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print('-=-'*30)
print('Vamos brincar de jogo de advinha, vou pensar em um número, tente advinhar...')
print('-=-'*30)

pc = randint(0, 10)
usuario = int(input('Digite um número entre 0 e 10: '))
cont = 1
while pc != usuario:
    usuario = int(input('Você errou, tente novamente: '))
    cont+=1
    if usuario > 10:
        print('Digite um valor entre 0 e 10...')
    else:
        if usuario < pc:
            print('Digite um número maior...')
        else:
            print('Digite um número menor...')
    
print('Você acertou, foram {} tentativas...'.format(cont))
print('Fim')