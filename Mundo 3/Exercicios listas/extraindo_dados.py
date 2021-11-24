'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
cont = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont+=1
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp in 'nN':
        break
print('='*30)
print(f'A quantidade de números digitados foram: {cont}')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {lista}')
#for i in lista:
if 5 in lista:
    print('O número 5 ESTÁ na lista')
else:
    print('O número 5 NÃO ESTÁ na lista')
    