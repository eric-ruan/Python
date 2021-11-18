'''Crie um  programa que leia duas notas de um aluno e calcule sua média,
mostando no final, de acordo com a média atingida:
- média abaixo de 5.0: Reprovado
- média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior: aprovado'''

print('Digite o valor da primeira nota: ')
n1 = float(input())
print('Digite o valor da segunda nota: ')
n2 = float(input())

media = (n1+n2)/2

if media < 5.0:
    print('A média foi de {}, o aluno foi reprovado!!'.format(media))

elif media > 5.0 and media < 6.9:
    print('A média foi de {}, o aluno ficou de reuperação!!'.format(media))
    
else:
    print('A média foi de {}, o aluno foi aprovado!!'.format(media))