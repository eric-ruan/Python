'''Crie um programa que mostre qual o tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''

print('Digite valores de retas, vamos verificar qual tipo de triângulo forma!')
l1 = float(input('Primeira reta: '))
l2 = float(input('Segunda reta: '))
l3 = float(input('Terceira reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:

    if l1 == l2 and l2 == l3:
        print('Todos os lados iguais, triângulo equilátero.')
        
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Dois lados iguais, triângulo isósceles.')
        
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('Todos os lados diferentes, triângulo escaleno.')
    
else:
    print('Não pode formar um triângulo.')