# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
jogos =[]
qtdd = int(input('Quantos jogos gostaria de gerar?'))
print("-="*3, f'SORTEANDO {qtdd} JOGOS', "-="*3)
while len(jogos) <= qtdd - 1:
    jogo = []
    while len(jogo) < 6:
        jogo.append(randint(1, 60))
    jogos.append(jogo)
print(jogos)