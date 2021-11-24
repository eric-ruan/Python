'''Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

galera = []
dado = []
cont = maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    cont+=1
    if len(dado) > 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear
        
        
    r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if r in 'nN':     
        break
print('galera ',galera)
print('maior ',maior)
print('menor ',menor)
#a)
print(f'O número de pessoas adicionadas foi {cont}')
#b)

    