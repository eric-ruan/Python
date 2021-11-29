#podemos utlizar as def para facilitar os códigos que escrevemos varias vezes
#IMPORTANE, EM ALGUMAS IDES UMA DEF PRECISA DE DUAS LINHAS VAZIAS APOS SER CRIADA
'''Exemplo do
print("-=-"*30), nesse caso utilizamos
'''
def linha():
    print('-=-'*30)
    
    
linha()
print('Olá')
linha()

#Podemos também utilizar uma def com parametros para algo que queremos manipular dentro dela, exemplo: 
def p(msg):
    print('-=-'*30)
    print(msg)
    print('-=-'*30)
    
    
p('Hello Word')

def s(a, b):
    print(f'O A vale {a} e o B vale {b}')
    soma = a + b
    print(f'A soma entre A+B = {soma}')


s(4,5)
s(b = 4, a = 5)
s(2, 4)

#podemos usar um contador para número mesmo quando não sabemos quantos números iremos receber

'''def contador(* num):
    print(num)
    
contador(3, 4, 2, 6, 8, 7)
contador(3, 4, 2, 5, 6)'''

def contador(* num):
    for i in num:
       print(i, end = ' ')
    print('Fim')
    tam = len(num)
    print(f'Recebi os valores e o tamanho é {tam}')
    

contador(3, 4, 2, 6, 8, 7)
contador(3, 4, 2, 5, 6)
print('-=-'*30)

def dobra(lst):
    pos = 0
    while pos < len(valores):
        lst[pos] *= 2
        pos += 1


valores = [4, 5, 3, 6, 2, 1]
dobra(valores)
print(valores)

print('-=-'*25)
def soma(* valores):
    cont = 0
    for i in valores:
        cont += i
    print(f'somando os valores {valores} temos {cont}')

soma(3, 2, 2)
soma(2, 2, 2)
