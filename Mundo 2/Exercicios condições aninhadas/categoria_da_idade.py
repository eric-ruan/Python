'''Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: sênior
- acima: master'''

from datetime import date
data = date.today().year
print('Em que ano o atleta nasceu?')
ano_nasc = int(input())

if (data - ano_nasc) > 1 and (data - ano_nasc) <= 9:
    print('Categoria Mirim!!')

elif (data - ano_nasc) > 9 and (data - ano_nasc) <= 14:
    print('Categoria Infantil!!')

elif (data - ano_nasc) > 14 and (data - ano_nasc) <= 19:
    print('Categoria Juior!!')

elif (data - ano_nasc) > 19 and (data - ano_nasc) <= 20:
    print('Categoria Sênior!!')
    
elif (data - ano_nasc) >= 20:
    print('Categoria Master!!')
    
else:
    print('A criança é muito nova!')