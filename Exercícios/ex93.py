# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''analise = {}

Nome = str(input('Nome do jogador: '))
analise['Nome'] = Nome
partidas = int(input('Partidas disputadas: '))
analise['partidas'] = partidas

gols_partida = {}

for partida in range(partidas):
    gols = int(input(f'Quantos gols fez na partida {partida + 1}? '))
    gols_partida[partida + 1] = gols

analise['gols por partida'] = gols_partida
soma_gols = sum(analise['gols por partida'].values())

print(30*'=-')
print(f'O nome do jogador é {analise['Nome']}.')
print(f'O total de gols marcado pelo jogador foi {soma_gols}.')
print(30*'=-')

print(f'O jogador {analise["Nome"]} jogou {analise["partidas"]} partidas.')
for jogos in range(partidas):
    print(f'    => Na partida {jogos + 1}, fez {analise["gols por partida"][jogos + 1]} gols.')
   
print(f'Foi um total de {soma_gols} gols em {partidas} partidas, com uma média de {soma_gols/partidas:.2f} gols por partida')'''

# Resolução Guanabara

jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(30*'=-')
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'O total de gols marcados pelo jogador foi {jogador["total"]} gols.')
print(30*'=-')
