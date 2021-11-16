#Faça um algoritmo que leia o salário de um funcionário  mostre seu novo salário com 15% de aumento.
print('Digite seu salário atual: ')
salario = float(input())
novosalario = salario + (salario*15)/100

print('Seu saalrio anterior era de R${:.2f}, com o aumento de 15% ficou em R${:.2f}'.format(salario, novosalario))