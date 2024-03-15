from random import randint
tentativas = 0
jogador = int(input('Estou pensando num número de 0 a 10, qual você acha que é? '))
computador = randint(0, 10)
if 0 < jogador > 10:
    print('Esse número não entra em nosso jogo.')
    jogador = int(input('Digite outro número, mas lembre-se, tem que ser entre 0 e 10! '))
while jogador != computador:
    tentativa += 1
    print('Não foi dessa vez!')
    jogador = int(input('Mas não desanime, tente outro número: '))
    computador = randint(0, 10)
print(f'Boa! Dessa vez você acertou! Foram necessárias {tentativas} tentativas para conseguir vencer.')

# Resolução Guanabara
from random import randint
computador = randint(0,10)
print('Sou seu computador....')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    j = int(input('Qual é o seu palpite?'))
    palpites +- 1
    if j == computador:
        acertou = True
    else:
        if j < computador:
            print('Mais... Tente novamente')
        else:
            print('Menos... Tente novamente')
print(f'Acertou com {palpites}. Parabéns!')
