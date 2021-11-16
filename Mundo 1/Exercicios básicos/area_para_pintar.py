#Faça um programa que leia a altura e a largura de uma parede, calcule sua área
#e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta,
#pinta uma área de 2m².

print('Digite a altura de um parede: ')
altura = float(input())
print('Digite a largura da parede: ')
largura = float(input())

area = altura*largura
tinta = area/2
print('Sua parede tem uma dimensão de {}X{} e a área dela é de {}m²'.format(altura, largura, area))
print('Para pintar sua parede irá precisar de {}L de tinta'.format(tinta))