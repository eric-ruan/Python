'''Crie um programa que faça o computador jogar Jokenpô com você'''
import random
from time import sleep
print('Vamos jogar pedra papel tesoura?')
usuario = str(input('O que você escolhe?... ')).lower()
print('-=-'*10,'JO','-=-'*10)
sleep(1)
print('-=-'*10,'KEN','-=-'*10)
sleep(1)
print('-=-'*10,'PÔ!!','-=-'*10)
pc = random.choice(['pedra', 'papel', 'tesoura'])
print('-=-'*20)

print('Você escolheu {}'.format(usuario))
print('Eu escolhi {}'.format(pc))
print('-=-'*20)

if (usuario == 'pedra' and pc == 'tesoura') or (usuario == 'tesoura' and pc == 'papel') or (usuario == 'papel' and pc == 'pedra'):
    print('Você ganhou, eu perdi :(')
    
elif (pc == 'pedra' and usuario == 'tesoura') or (pc == 'tesoura' and usuario == 'papel') or (pc == 'papel' and usuario == 'pedra'):
    print('Você perdeu, eu GANHEEIII')
    
elif (usuario == 'pedra' and pc == 'pedra') or (usuario == 'papel' and pc == 'papel') or (usuario == 'tesoura' and pc == 'tesoura'):
    print('Deu empate, vamos de novo?')
    
else:
    print('Digite valores válidos...')
