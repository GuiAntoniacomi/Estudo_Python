time = list()
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(30*'=-')    
for k, v in enumerate(time):
    print(f' {k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(30*'=-')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for k, v in enumerate(time[busca]['gols']):
            print(f'    No jogo {k+1} fez {v} gols.')
        print(f'Foi um total de {time[busca]["total"]} gols.')