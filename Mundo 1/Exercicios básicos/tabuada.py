print('Digite um número para fazer sua tabuada: ')
n = int(input())

for i in range(1,11):
    print('{} X {} = {}'.format(n,i,n*i))