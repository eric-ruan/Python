#help(print)#o comando help() como o nome já diz, serve para auxiliar a pessoa, ele te explica o que é e como funciona
#print(input.__doc__) #serve para mesma coisa que o help
'''def contador(i, f, p):
    """
    É dessa forma que declaramos uma docstring
    [A função contador faz a contagem de um número até outro]

    Args:
        i ([inteiro]): [Inicio]
        f ([inteiro]): [fim]
        p ([inteiro]): [passo]
    """
    cont = i
    while cont <= f:
        print(f'{cont}', end=' ')
        cont += p
contador(0, 100, 10)'''

'''#Parametros opcionais, usamos eles quando não sabemos se será passado um número como parametro de uma def
def somar(a=0, b=0, c=0):
    #dessa forma podemos dar valor para cada parametro ou não
    soma = a+b+c
    print(soma)

somar(3, 3, 2)'''

#escopo de variaveis é a definição de variaveis locais e variaveis globais
#podemos utilizar o comando global para definir que a variavel não será somente local

#retornando valores, para isso usamos a palavra return, dessa forma podemos deixar o código menos repetitivo, exemplo:
'''def somar(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar(3, 5, 8)
r2 = somar(2, 3, 1)
r3 = somar(2, 6)
print(f'As somas valem {r1}, {r2} e {r3}')'''

'''def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''
def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input('Número: '))
print(parOuImpar(n))