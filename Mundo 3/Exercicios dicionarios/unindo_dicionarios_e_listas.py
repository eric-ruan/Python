'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = {}
lista = []
cont = soma = 0
while True:
    dados["nome"] = str(input('Nome: '))
    while True:
        dados["sexo"] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'mMfF':
            break
        print('Digite [M/F]...')
    dados["idade"] = int(input('Idade: '))
    cont += 1
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if resp not in 'nNsS':
            print('Resposta inválida, digite apenas [S/N]')
        else:
            break
    if resp in 'nN':
        break
#A) Quantas pessoas foram cadastradas
print('='*25)
print(f'O número de pessoas cadastradas é: {cont}')
#B) A média de idade
print('='*25)
print(f'A média de idade das pessoas cadastradas é: {soma/cont:.2f}')       
#C) Uma lista com as mulheres
print('='*25)
print('O nome das mulheres cadastradas é: ')
for s in lista:
    if s['sexo'] == 'F':
        print(f'{s["nome"]}', end=' ')    
#D) Uma lista de pessoas com idade acima da média
print()
print('='*25)
print('O nome das pessoas que tem idade acima da média é: ')
for i in lista:
    if i["idade"] > (soma/cont):
        print(f'{i["nome"]}',end=' ')
