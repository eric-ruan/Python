def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar número.\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\33[33m{c}\33[m - \33[34m{i}\33[m')
        c+=1
    print(linha())
    opc = leiaInt('\33[32mSua opção: \33[m')
    return opc