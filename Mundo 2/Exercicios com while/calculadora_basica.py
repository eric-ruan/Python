import time
'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior')
op = int(input('Digite uma operação desejada: '))

while op != 5:
    if op == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1,n2,soma))
    elif op == 2:
        mult = n1 * n2
        print('{} X {} = {}'.format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('O maior entre {} e {} = {}'.format(n1,n2,maior))
        else:
            maior = n2
            print('O maior entre {} e {} = {}'.format(n1,n2,maior))
    elif op == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif op == 5:
        print('Fim do programa...')
    else:
        print('Digite um número válido...')
    print('=-='*10)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] Novos números\n[ 5 ] Saior do programa')
    op = int(input())
tempo = time.sleep(1)
print('SAINDO')
