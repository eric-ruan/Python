'''Faça uma tabuada com o número que o usuario digitar'''
print('Digite um número inteiro qualquer...')
n = int(input())
print('Você quer fazer esse número multiplicado até quanto?')
multi = int(input())

for i in range(1, multi+1):
    print('{} X {} = {}'.format(n, i, n*i))