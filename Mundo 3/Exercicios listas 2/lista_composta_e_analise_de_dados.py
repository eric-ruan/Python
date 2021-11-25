'''Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

galera = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado [1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()  
    r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if r in 'nN':     
        break
print(f'Ao todo o número de pessoas cadastradas foi de: {len(galera)}')
print(f'O maior peso é de {maior}Kg. São os pesos de: ',end='')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso é de {menor}Kg. São os pesos de: ',end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}, ', end='')


    