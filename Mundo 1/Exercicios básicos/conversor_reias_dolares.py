#crie um programa que leia quanto dinhehiro uma pessao tem na carter e mostre quatos dolares 
#ela pode comprar. valor atualmente R$5,48

print('Quanto dinheiro você tem na carteira? ')
r = float(input())

print('Com esse valor de R${}, você pode comprar US${:.2f}'.format(r, r / 5.48))