'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa 
mostrar as notas de cada aluno individualmente.'''
from time import sleep
ficha = []
boletim = []
media = 0
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    ficha.append([nome, [nota1, nota2], media])
    if resp in 'nN':
        break

print('='*30)  
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')

while True:
    print('-'*35)
    op = int(input('Deseja que mostre a nota de qual aluno? (999 INTERROMPE): '))
    if op == 999:
        sleep(1)
        print('Finalizando')
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
print('<<<< VOLTE SEMPRE >>>>')
sleep(1)
