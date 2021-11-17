'''Faça um programa que leia uma frase pelo teclado e mostre:
-quantas vezes aparece a letra "A".
-Em que posição ela aparece a primeira vez 
-E em que posição ela aparece a última vez.'''

print('Digite uma frase qualquer: ')
frase = str(input()).upper().strip()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))