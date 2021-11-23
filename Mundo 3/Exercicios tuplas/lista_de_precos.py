'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
print(f'{"="*12}Lista de produtos{"="*12}')
produtos = ('Lapis',0.50,
            'Caneta',1.25,
            'Caderno',9.99,
            'Apontador', 2.30,
            'Mesa de escritório', 249.99)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}',end = '')
    else:
        print(f'R${produtos[posicao]:>7.2f}')
print(f'{"="*12}{"."*15}{"="*12}')