#Um professor quer sortear um de seus quatro alunos para apresentar um trabalho
#ajude ele fazendo esse sorteio e depois mostre a ordem de quem vai primeiro.
import random
a1 = str(input('Digite o ome do primeiro aluno: '))
a2 = str(input('Digite o ome do segundo aluno: '))
a3 = str(input('Digite o ome do terceiro aluno: '))
a4 = str(input('Digite o ome do quarto aluno: '))

nomes = [a1, a2, a3, a4]
random.shuffle(nomes)
print('A ordem de apresentação será: ')
print(nomes)