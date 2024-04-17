def ficha(nome, gols):
    if nome == "":
        nome = '<Desconhecido>'
    try:
        gols = int(gols)
    except ValueError:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = input('Número de gols: ')
ficha(n, g)
