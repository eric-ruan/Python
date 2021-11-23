'''Crie uma tupla preenchida com os 20 primeiros 
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino', 'Fluminense', 'Internacional', 'Ceará SC', 'América-MG',
          'Cuiabá', 'Santos', 'Athletio-PR', 'São Paulo', 'Atlético-GO', 'Juventude', 'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')
#a)
print('-=-'*30)
print(f'Os cinco primeiros times são: {tabela[:5]}')
print('-=-'*30)
#b)
print(f'Os ultimos 4 colocados são: {tabela[-4:]}')
print('-=-'*30)
#c)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('-=-'*30)
#d)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
print('-=-'*30)

