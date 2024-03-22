# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

# Sorteando dados:
'''jogos = {}
resultados = []
for c in range(1,5):
    jogos['jogador'] = c
    jogos['resultado'] = randint(1,6)
    resultados.append(jogos.copy())
    print(f'O {jogos["jogador"]}º jogador tirou {jogos["resultado"]}.')
    sleep(1)
'''

jogos = {
    'Jogador A': randint(1,6),
    'Jogador B': randint(1,6),
    'Jogador C': randint(1,6),
    'Jogador D': randint(1,6)
}
ranking = list()
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('O raning dos recultados ficou: ')
for i, v in enumerate(ranking):
    print(f'O {i+1}º lugar> {v[0]} com {v[1]}.')
    sleep(1)