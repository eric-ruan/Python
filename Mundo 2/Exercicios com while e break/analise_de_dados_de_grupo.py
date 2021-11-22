'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos. - 
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
dezoito = masc = vinteFem = 0
while True:
    print('-=-'*20)
    print('Cadastro de pessoas')
    print('-=-'*20)
    idade = int(input('Qual a idade da pessoa: '))
    sexo = str(input('Qual o sexo da pessoa [M/F]: ')).upper().strip()[0]
    print('-=-'*10)
    if idade > 18:
        dezoito += 1
    if sexo in 'mM':
        masc += 1
    elif sexo in 'fF' and idade < 20:
        vinteFem += 1    
    
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if resp in 'nN':
        break
print(f'O número de pessoas com mais de 18 anos é {dezoito}.\nO número de homens cadastrados foram {masc}.\nO número de mulheres cadastradas com menos de 20 anos é {vinteFem}')