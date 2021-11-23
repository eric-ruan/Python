'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    
for pos, i in enumerate(lista):
    print(f'Na posição {pos}, encontrei: {i}')


print(f'A lista de valores digitados foi: {lista}')
print(f'O maior valor digitado foi: {max(lista)}')
print(f'O menor valor digitado foi: {min(lista)}')