'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.2f} X {comprimento:.2f} é de {area:.2f}m².')

print('Controle de Terrenos')
print('-'*25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)