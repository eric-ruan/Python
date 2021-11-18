'''Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.'''

print('Digite o valor da casa: ')
valor_casa = float(input())
print('Digite o valor do seu salário: ')
salario = float(input())
print('Você irá pagar em quantos anos?')
anos = int(input())

parcelas = anos*12
prestacao = valor_casa/parcelas

if prestacao <= (salario*30)/100:
    print('empréstimo aprovado!!')

elif prestacao > (salario*30)/100:
    print('Prestação excedeu o 30% do seu salário!')

else:
    print('Emprestimo negado!!')
    