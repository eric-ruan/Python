'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra. -
B) quantos produtos custam mais de R$1000. -
C) qual é o nome do produto mais barato. -'''

'''cont = valor = totValor = contMais = contMenor = 0
print('-'*20)
print('Mercearia do Éric')
print('-'*20)
while True:
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    valor = float(input('Digite o valor do produto: R$'))
    print('-=-'*20)
    totValor += valor
    if valor > 1000:
        contMais += 1
    elif cont == 1:
        if valor < contMenor:
            contMenor = valor
            #nomeProd = nome
    
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    print('-=-'*20)
    if resp in 'nN':
        break

print(f'O valor total da compra é de {totValor}')
print(f'O número de produtos que custa menos de R$1000.00 é {contMais}')
print(f'O nome do produto mais barato é {contMenor}')'''