#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

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


# Segunda Resolução
def ficha(jog= <desconhecido>, gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip == '':
    ficha()
else:
    ficha()