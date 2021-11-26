'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
from time import sleep
boletim = {}
lista = []
while True:
    boletim['nome'] = str(input('Qual o nome do aluno: ')).strip()
    boletim['media'] = float(input('Qual a média do aluno: '))
    lista.append(boletim.copy())
    r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if r in 'nN':
        break

for b in lista:
    for k, v in b.items():
        print(f'{k} = {v}')
        
       
print('FINALIZANDO')
print('='*30)

