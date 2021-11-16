#Escreva um programa que exiba valores convertidos de metros para centimetros e milimetros
print('Quantos metros você quer converter? ')
metros = float(input())

print('{}m, convertido para centimetros fica {}cm, convertido para milimetros fica {}mm'.format(metros, metros*100, metros*1000))