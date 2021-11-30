def aumentar(n = 0, acrescimo = 0, formatado = False):
    tot = n + (n*acrescimo)/100
    return tot if formatado is False else moeda(tot)

def diminuir(n = 0, desconto = 0, formatado = False):
    tot = n - (n*desconto)/100
    return tot if formatado is False else moeda(tot)


def dobro(n = 0, formatado = False):
    dobro = n*2
    return dobro if formatado is False else moeda(dobro)


def metade(n = 0, formatado = False):
    metade = n/2
    return metade if formatado is False else moeda(metade)

def moeda(n = 0, moeda = 'R$', formatado = False):
    return f'{moeda}{n:.2f}'.replace('.', ',')