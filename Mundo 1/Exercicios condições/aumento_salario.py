'''Escreva um programa que pergunte o salário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 , calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

print('Qual o seu salário? ')
sal = float(input())

if sal > 1250:
    novo_sal = sal + (sal * 10)/100
    print('Seu salário era de R${:.2f}, com aumento de 10% foi para R${:.2f}'.format(sal, novo_sal))
else:
    novo_sal = sal + (sal * 15)/100
    print('Seu salário era de R${:.2f}, com aumento de 15% foi para R${:.2f}'.format(sal, novo_sal))