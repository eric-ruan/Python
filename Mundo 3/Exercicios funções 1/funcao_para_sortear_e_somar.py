'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a 
soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep



def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end = '')
    for i in range(1, 6):
        num = randint(0, 10)
        lista.append(num)
        print(num, end= ' ', flush=True)
        sleep(0.3)
    print('Pronto!!')
    


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista} temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)        