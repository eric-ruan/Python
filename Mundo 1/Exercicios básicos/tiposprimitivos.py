#VALIDANDO OS TIPOS
n = input('Digite algo: ')
print('O tio primitivo desse valor é: ', type(n))
print('Só tem espaços: ', n.isspace())
print('É um número: ', n.isnumeric())
print('É alfabetico: ', n.isalpha())
print('É alfanúmerico: ', n.isalnum())
print('Está em maisculas: ', n.isupper())
print('Está em minusculas: ', n.islower())
print('Está capitalizada: ', n.istitle())
