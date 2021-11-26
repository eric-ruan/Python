'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
ano =  date.today().year
pessoa = {}
dados = []
pessoa['nome'] = str(input('Qual o nome da pessoa: ')).strip()
pessoa['idade'] = ano - int(input('Qual o ano de nascimento: '))
pessoa['ctps'] = int(input('Qual o nº da carteira de trabalho (digite 0 se não tiver): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Qual foi o ano de contratação: '))
    pessoa['salario'] = float(input('Qual o salario R$'))
    pessoa['aposentadoria'] = (pessoa['contratacao']+35)-2000

dados.append(pessoa.copy())

print(f'------------------ Dados de CTPS de {dados[0]["nome"]}------------------')
for e in dados:
    for k, v in e.items():
        print(f"{k} = {v}")
    