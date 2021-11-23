num = [2, 5, 9, 1]
num[2] = 3 #troca elementos
num.append(7) #add elementos
num.sort(reverse=True) #inverte a ordem de maior para menor
num.insert(2, 0)#add o valor 0 na posição 2
num.pop() #remove o ultimo elemento da lista
num.pop(2) #remove o elemento 2 da lista
num.append(7)
num.remove(7)#dessa forma remove o primeiro elemento 7 que aparecer
print(num)
print(f'Essa lista tem {len(num)} elementos.')#mostra quantos elementos tem na lista

print('-=-'*25)
lista = [2, 5, 9, 1, 4]
if 5 in lista:
    lista.remove(5)
    print('Removido')
else:
    print('Não encontrei o número 5')
    
for c, v in enumerate(lista):#dessa forma mostra a posição e os valores da lista
    print(f'Na posição {c} encontrei o valor {v}!')

print('='*20, 'Colocando valores na lista', '='*20)

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite o valor: ')))