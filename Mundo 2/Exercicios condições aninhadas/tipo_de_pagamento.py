'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

det = '-=-'*20
print('Qual o valor do produto?')
preco = float(input('R$'))
print(det)
print('Qual a forma de pagamento?')
print(det)
print('[1] Dinheiro/cheque\n',det,'\n[2] À vista no cartão\n',det,'\n[3] Em até 2x no cartão\n',det,'\n[4] 3x ou mais no cartão\n',det)
forma_pagamento = int(input())

if forma_pagamento == 1:
    desc = preco - (preco*10)/100
    print('O produto custava R${:.2f}, com o desconto ficou em R${:.2f}!!'.format(preco, desc))

elif forma_pagamento == 2:
    desc = preco - (preco*5)/100
    print('O produto custava R${:.2f} com o desconto passou a custar R${:.2f}!!'.format(preco, desc))
    
elif forma_pagamento == 3:
    parcelas = preco/2
    print('O valor do produto fica em R${:.2f} em duas vezes de R${:.2f}'.format(preco, parcelas))
    
elif forma_pagamento == 4:
    numb = int(input('Em quantas parcelas: '))
    novo_preco = preco + (preco*20)/100
    parcelas = novo_preco / numb
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(numb, parcelas))
    
else:
    print('Você precisa escolher uma das opções de pagamento.')