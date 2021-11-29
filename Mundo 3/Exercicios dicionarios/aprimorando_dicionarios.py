'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogadores = {}
partidas = []
time = []
while True:
    jogadores.clear()
    jogadores["nome"] = str(input('Qual o nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogadores["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª: ')))
    jogadores["gols"] = partidas[:]
    jogadores["totgols"] = sum(partidas)
    time.append(jogadores.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp in 'nN':
        break
print('-=-'*30)
print(f'Cod ',end='')
for i in jogadores.keys():
    print(f'{i:<15}',end='')
print()
print('-=-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<14} ', end='')
    print()   
print('-=-'*40)
while True:
    busca = int(input('Você quer mostrar os dados de qual jogador (Digite 999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, não existe jogadore com o códio {busca}')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=-'*40)
print('VOLTE SEMPRE')
