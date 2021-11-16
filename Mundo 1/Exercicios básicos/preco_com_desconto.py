#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto.

print('Qual o valor do produto? ')
preco = float(input())
novo = preco - (preco*5)/100

print('O valor do produto era de R${:.2f}, acrescentando o desconto fica em R${:.2f}'.format(preco, novo))