#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
print('Digite um número: ')
n = float(input())

dobro = n*2
triplo = n*3
raiz = n**(1/2)
print('O número digitado foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(n, dobro, triplo, raiz))