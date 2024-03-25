analise = {}

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
   
print(f'Foi um total de {soma_gols} gols em {partidas} partidas, com uma média de {soma_gols/partidas:.2f} gols por partida')