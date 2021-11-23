lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])#mostra o suco
print(lanche[-2])#mostra a pizza, pois o pudim é o 3 ou -1
print(lanche[1:3])#suco e pizza, o elemento 3 é desconsiderado
print(lanche[2:])#pizza e pudim
print(lanche[:2])#mostra hamburguer e suco, ignora a pizza
print(lanche[-2])#mostra a pizza
print(lanche[-2:])#pizza, pudim

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}') #me diz os elementos da lista
print('='*30)
for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}') #me diz os elementos e suas posições
print('Comi bastante')    

print('='*30)
print(sorted(lanche)) #coloca a tupla em ordem
print('='*30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
print(c)#junta as duas tuplas
print('='*30)
pessoa = ('Éric', 19, 'M')
del(pessoa)#esse comando apaga uma variavel

print(f'O hamburguer está na {lanche.index("Hamburguer")}º posição')
'''TUPLAS SÃO IMUTAVEIS'''