#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Você quer ver a tabuada de qual número: '))
    if n <= 0:
        break
    print('-=-'*20)
    for cont in range(1, 11):
        print(f'{n} X {cont} = {n*cont}')
    print('-=-'*20)
    