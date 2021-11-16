#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Quantos km você andou com o carro?')
km = float(input())

print('Quantos dias você ficou com o carro?')
dias = int(input())

preco = (dias*60) + (km*0.15)

print('Você andou {:.2f}km com o carro e ficou com ele por {} dias. \n O valor total do aluguel é de R${:.2f}'.format(km, dias, preco))