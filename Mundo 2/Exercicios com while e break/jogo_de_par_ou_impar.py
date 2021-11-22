#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
print('-=-'*20)
print('Vamos jogar par ou ímpar')
print('-=-'*20)
while True:
    pc = randint(1,10)
    usuario = int(input('Diga um valor: '))
    resp = str(input('Você escolhe par ou ímpar? [P/I] ')).upper().strip()
    result = pc + usuario
    cont+=1
    if result % 2 == 0:
        if resp in 'pP':
            print('Você venceu!')
            break
        else:
            print('Você perdeu!')
print(f'Você venceu... O número de vezes que jogou foi {cont}')