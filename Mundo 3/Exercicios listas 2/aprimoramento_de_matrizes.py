'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
somaPares = somaTerceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'[linha{l} coluna{c}] '))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
for l in range(0, 3):
    somaTerceira += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print('========Matriz========')
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('========Soma de todos os pares========')
print(f'{somaPares}')
print('========Soma dos valores da 3ª coluna========')
print(f'{somaTerceira}')
print('========O maior valor da segunda linha========')
print(f'{maior}')
