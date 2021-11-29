'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(num):
    menor = maior = cont = 0
    for i in num:
        if cont == 0:
            maior = menor = i
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        cont += 1
        print(f'{i}', end = ' ')
    print(f'O maior é {maior} e o menor foi {menor}')

num = []
while True:
    num.append(int(input('Digite um número: ')))
    if len(num) >= 2:
        while True:
            resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
            if resp not in 'sSnN':
                print('Resposta inválida, digite apenas [S/N]')
            else:
                break
        if resp == 'N':
            break
maior(num)