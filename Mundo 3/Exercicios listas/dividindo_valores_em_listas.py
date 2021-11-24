'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista.append(n)
        pares.append(n)
    else:
        lista.append(n)
        impares.append(n)
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp in 'nN':
        break
print('='*30)
print(f'A lista completa ficou: {lista}')
print('='*30)
print(f'A lista somente com os valores pares fica: {pares}')
print('='*30)
print(f'A lista só com valores ímpares fica: {impares}')