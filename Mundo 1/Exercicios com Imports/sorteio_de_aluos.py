#Um professor quer sortear um de seus quatro alunos para apagar o quadro, faça um programa que ajude ele
#lendo os nomes e escrevendo quem foi o escolhido.
import random
a1 = str(input('Digite o ome do primeiro aluno: '))
a2 = str(input('Digite o ome do segundo aluno: '))
a3 = str(input('Digite o ome do terceiro aluno: '))
a4 = str(input('Digite o ome do quarto aluno: '))

print('O escolhido foi: {}'.format(random.choice([a1, a2, a3, a4])))