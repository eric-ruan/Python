#Desenvolva um programa que leia duas notas de um aluno e exiba sua média

print('Digite a primeira nota: ')
n1 = float(input())
print('Digite a segunda nota: ')
n2 = float(input())

media = (n1+n2)/2
print('A primeira nota é {}, a segunda {}, a média foi de {}'.format(n1,n2,media))