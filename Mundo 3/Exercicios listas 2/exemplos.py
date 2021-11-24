'''lista = list()
lista.append('Éric')
lista.append(19)
galera = []
galera.append(lista)
lista[0] = 'João'
lista[1] = 22
galera.append(lista)
print(galera)'''
#dessa forma os dados vão ficar iguais, pois o que aconteceu foi uma ligação entre as duas estruturas
'''print('='*30)
lista = list()
lista.append('Éric')
lista.append(19)
galera = []
galera.append(lista[:])
lista[0] = 'João'
lista[1] = 22
galera.append(lista[:])
print(galera)'''
#assim, criamos uma cópia, aí os dados serão exibidos diferentes
'''print('='*30)
galera = [['João', 19], ['Éric', 19], ['Maria', 19], ['Fernana', 18]]
print(galera[0])#mostra somente os dados do João
print(galera[0][0])#mostra somente o nome do Jõao
print(galera[2][1])#mostra a idade da Maria'''
#Podemos também correr uma lista
'''galera = [['João', 19], ['Éric', 19], ['Maria', 19], ['Fernana', 18]]
for p in galera:
    print(p)'''
#assim mostramos os dados de todas as pessoas que tem na lista
#podemos também mstrar somente o nome ou a idade das pessoas, da seguinte maneira
'''#nome
galera = [['João', 19], ['Éric', 19], ['Maria', 19], ['Fernana', 18]]
for p in galera:
    print(p[0])
#idade
for p in galera:
    print(p[1])'''
#pedindo nome e idade
'''galera = []
dado = []
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)'''
#dessa forma você cria um dado e copia esses dados para dentro de uma outra lista.
#-------------------------------------
#se quisermos mostrar somente as pessoas que tenham mais de 21 anos.
'''galera = []
dado = []
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')'''
#ou
'''galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen+=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''
