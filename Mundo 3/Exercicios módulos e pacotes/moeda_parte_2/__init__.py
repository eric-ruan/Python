def aumentar(n = 0, acrescimo = 0):
    tot = n + (n*acrescimo)/100
    return tot

def diminuir(n = 0, desconto = 0):
    tot = n - (n*desconto)/100
    return tot


def dobro(n = 0):
    dobro = n*2
    return dobro


def metade(n = 0):
    metade = n/2
    return metade

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')