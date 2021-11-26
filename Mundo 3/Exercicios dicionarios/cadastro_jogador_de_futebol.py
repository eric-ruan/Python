'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler 
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
from time import sleep
dados = {}
dados['nome'] = str(input('Qual o nome do jogador: ')).strip()
dados['partidas'] = int(input('Quantas partidas ele jogou: '))
dados['golspartida'] = int(input('Quantos gols ele fez em cada partida: '))
dados['totaldegols'] = dados['golspartida']*dados['partidas']

'''for d, k in dados.items():
    print(f'{d} = {k}')'''
print(f'---------- Dados do jogador {dados["nome"]}----------')
print(f'Nome: {dados["nome"]}')
sleep(1)
print(f'Total de partidas: {dados["partidas"]}')
sleep(1)
print(f'Total de gols por partida: {dados["golspartida"]}')
sleep(1)
print(f'Total de gols no campeonato: {dados["totaldegols"]}')
sleep(1)
print('---------- Fim da ficha ---------')