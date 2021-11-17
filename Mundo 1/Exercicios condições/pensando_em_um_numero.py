''' Crie um prrgrama que faça o computador "pensar" em um número entre 0 e 5 e peça 
para o usuário tentar descobrir qual foi o númro escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''
from random import randint

n = randint(0, 5)
print('-=-'*20)
print('Estou pensando em um número de 0 a 5, tente advinhar qual é...')
print('-=-'*20)
numero = int(input())

if numero == n:
    print('Parabens, você acertou o número!!')
elif numero > 5:
    print('Digite apenas um número entre 0 e 5...')
else:
    print('Você errou, tente novamente')
print('Fim do programa, obrigado por brincar!!')