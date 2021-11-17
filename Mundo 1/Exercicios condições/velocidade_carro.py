'''Escreva um programa que leia a velocidade de um carro. Se ele utrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

print('Você está a quantos Km/h??')
km = float(input())

if km > 80:
    vel = km - 80
    print('VOCÊ ESTÁ EM UMA VELOCIDADE ACIMA DO PERMITIDO')
    print('FOI MULTADO(A), O VALOR A SER PAGO É DE R${:.2f}'.format(vel*7))
else:
    print('Você está na velocidade permitida!!')