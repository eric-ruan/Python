'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler 
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
from time import sleep
dados = {}
gols = []
soma = 0
dados['nome'] = str(input('Qual o nome do jogador: ')).strip()
dados['partidas'] = int(input('Quantas partidas ele jogou: '))
tot = 1
while tot <= dados['partidas']:
    gols.append(int(input(f'Quantos gols ele fez no {tot}º jogo: ')))
    tot+=1
dados['gols'] = gols
for v in dados['gols']:
    soma += v
dados['totaldegols'] = soma

print(f'---------- Dados do jogador {dados["nome"]}----------')
print(f'Nome: {dados["nome"]}')
sleep(1)
print(f'Ele jogou um total de {dados["partidas"]} partidas.')
for p, g in enumerate(gols):
    print(f'No {p+1}º jogo ele fez: {g} gols')
    sleep(0.5)
print(f'Total de gols no campeonato: {dados["totaldegols"]}')
sleep(1)
print('---------- Fim da ficha ---------')