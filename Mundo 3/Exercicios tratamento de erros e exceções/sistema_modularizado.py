'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples. O sistema só vai ter duas opções: cadastrar uma nova pessoa
e listar todas as pessoas cadastradas.'''
from lib.interface import*
from lib.arquivo import*
from time import sleep

arq = 'arquivo.txt'
if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema!!')
        break
    else:
        print('\33[31mErro, digite uma opção válida\33[m')
    sleep(1)