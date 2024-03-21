# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('=-'*30)
print(f'{"JOGOS PARA MEGA SENA":^60}')
print('=-'*30)
jogos =[]
j = 0
qtdd = int(input('Quantos jogos gostaria de gerar? '))
print("-="*3, f'SORTEANDO {qtdd} JOGOS', "-="*3)
while len(jogos) <= qtdd - 1:
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogos.append(jogo)
for j in range(qtdd):
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
print('=-'*30)
print(f'{"Jogos gerados! Boa sorte!":^60}')
print('=-'*30)