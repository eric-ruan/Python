'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(nasc):
    from datetime import date
    data = date.today().year
    resp = data - nasc
    if resp < 16 or resp > 65:
        return f'Você tem {resp} anos, não vota.'
    elif resp >=16 and resp < 18:
        return f'Você tem {resp} anos, voto opicional.'
    else:
        return f'Você tem {resp} anos, voto obrigatório.'
    

anoNasc = int(input('Qual o ano do seu nascimento: '))
print(voto(anoNasc))

