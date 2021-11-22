'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 'S'
cont = soma = media = menor = menor = 0

while resposta in 'sS':
    n = int(input('Digite o primeiro número: '))
    cont += 1
    soma += n
    media = soma/cont
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    
    resposta = str(input('Deseja continuar? [S/N] ' )).upper().strip()[0]
print('----------Fim----------')
print('-=-'*20)
print('A quantidade de números digitados foi {}\n A soma entre eles foi {}\n A média é {}\n O menor número é {}\n O menor é {}'.format(cont, soma, media, menor, maior))