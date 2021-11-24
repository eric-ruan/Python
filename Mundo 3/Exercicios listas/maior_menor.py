'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

lista = []
maior = 0
menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um número na posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
print('='*30)
print(f'A lista de valores digitados foi: {lista}')
print(f'O maior valor digitado foi: {maior} e está nas posições: ',end = '')
for pos, i in enumerate(lista):
    if i == maior:
        print(f'{pos}...', end = '')
print()
print(f'O menor valor digitado foi: {menor} e está nas posições: ',end = '')   
for posicao, i in enumerate(lista):
    if i == menor:
        print(f'{posicao}...', end = '')
print()
