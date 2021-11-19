'''Melhore o Exercicio de PA, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

resp = 'S'
while resp == 'S':
    print('-=-'*10)
    p = int(input('Digite o primeiro termo da PA: '))
    print('-=-'*10)
    r = int(input('Digite a razão: '))
    print('-=-'*10)
    q = int(input('Você quer quantos termos: '))
    termo = p
    cont = 1

    while cont <= q:
        print('{}'.format(termo), end = '')
        print(' -> ' if cont < q else ' * ',end = '')
        termo+=r
        cont+=1
    resp = str(input('\nVocê quer mostrar novamente [ S/N ]: ').upper())
print('FIM')