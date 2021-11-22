'''Melhore o Exercicio de PA, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('-=-'*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
print('-=-'*10)
razao = int(input('Digite a razão: '))
print('-=-'*10)
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('*')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))