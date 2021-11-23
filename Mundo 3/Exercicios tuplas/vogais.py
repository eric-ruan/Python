'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
tupla = ('limao', 'cenoura', 'uva', 'banana', 'abacate', 'alface')
for i in range(0, len(tupla)):
    print(f'Palavra: {tupla[i].upper()}\nVogais: ')
    for vogais in tupla[i]:
        if vogais in 'aeiou':
            print(f'{vogais}',end='')
    print('\n')