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

def resumo(n = 0, taxaaume = 10, taxared = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Com {taxaaume}% de aumento: \t{aumentar(n, taxaaume, True)}')
    print(f'Com {taxared}% de desconto: \t{diminuir(n, taxared, True)}')
    print('-'*30)
    
def leiaDineheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)