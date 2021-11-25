'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa 
mostrar as notas de cada aluno individualmente.'''

lista = []
boletim = []
media = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    lista.append(n1)
    lista.append(n2)
    lista.append(media)
    
    boletim.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp in 'nN':
        break
for i, l in enumerate(boletim):
    print(f'O aluno {l[0]} tirou {l[1]}, e {l[2]}, media {l[3]}')
    print('='*30)