pessoas = {'nome': 'Éric', 'sexo': 'M', 'idade': '19'}
print(pessoas)
print('='*30)
#no caso de dicionários não temos elementos numerados como exemplo pessoas[0], nesse caso usasmos:
print(pessoas['nome'])
print('='*30)
#importante
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('='*30)
#podemos tabém printar o que tem dentro do dicionario
print(pessoas.keys()) #ou seus valores
print(pessoas.values()) #ou podemos mostrar tudo
print(pessoas.items())
print('='*30)
#podemos acessar os dicionarios através de laços
for k in pessoas.keys():
    print(k) #ou values
for v in pessoas.values():
    print(v) #ou os dois
for k, v in pessoas.items():#importante nesse caso de mostrar os dois, usar o items()
    print(f'{k} = {v}')
print('='*30)
#---------------------------------
del pessoas['sexo']# apagando um elemento
pessoas['nome'] = 'Ruan' #trocando um elemento
pessoas['peso'] = 57 #adicionando um elemento
print(pessoas)
print('='*30)

#criando um dicionario dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print('='*30)
#podemos mostrar agora cada elemento da lista
print(brasil[0])
print(brasil[1])
#ou podemos filtrar mais ainda
print(brasil[0]['uf'])
print('='*30)
#---------------------------------------------
#em dicionarios não podemos fazer a cópia de uma lista [:] usamos o comando .copy()
estado = {}
pais = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())
'''for e in pais:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')'''
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print()