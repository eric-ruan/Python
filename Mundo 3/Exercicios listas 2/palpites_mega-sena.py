'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos você quer fazer: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1

for i, l in enumerate(jogos):
    print(f'Sorteando o {i+1}º jogo: {l}')
    sleep(1)
