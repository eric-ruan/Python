'''Desenvolva um progrma que leia o nome, idade e sexo de 4 pessoas. no final mostre:
- a média de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos.'''

soma_idade = 0
media_idade = 0
maior_idade = 0
nome_mais_velho = 0
cont_f = 0

for i in range(1,5):
    print('-------{}ª PESSOA -------'.format(i))
    nome = str(input('Digite seu nome: ')).title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo, sendo M/F: ')).lower()
    soma_idade+=idade
    if i == 1 and sexo == 'm':
        maior_idade = idade
        nome_mais_velho = nome
    elif sexo == 'm' and idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome
    elif sexo == 'f' and idade < 20:
        cont_f+=1

media_idade = soma_idade/4
    
print('A média de idade do grupo é de {}'.format(media_idade))
print('A idade do homem mais velho é {} e ele se chama {}'.format(maior_idade, nome_mais_velho))
print('O número de mulheres que tem menos de 20 anos é {}'.format(cont_f))