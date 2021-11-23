'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista = []
resp = 'S'
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Não vou adicionar, já foi adicionado')
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print(f'A lista lista ficou: {lista}')
print('='*20)
lista.sort()
print(f'Em ordem crescente fica: {lista}')