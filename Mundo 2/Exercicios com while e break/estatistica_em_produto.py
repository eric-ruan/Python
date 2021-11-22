'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra. -
B) quantos produtos custam mais de R$1000. -
C) qual é o nome do produto mais barato. -'''
total = totalMil = menor = cont = 0
print('-'*20)
print('Mercearia do Éric')
print('-'*20)
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    preco = float(input('Digite o valor do produto: R$'))
    cont += 1
    print('-=-'*20)
    total += preco
#-----------------------------------------------
    if preco > 1000:
        totalMil += 1
#-----------------------------------------------
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    print('-=-'*20)
    if resp in 'nN':
        break

print(f'O valor total da compra é de {total:.2f}')
print(f'O número de produtos que custa menos de R$1000.00 é {totalMil}')
print(f'O nome do produto mais barato é {barato}, seu valor é de R${menor:.2f}')