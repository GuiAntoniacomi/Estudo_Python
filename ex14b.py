import random
tentativas = 0
jogador = int(input('Estou pensando num número de 0 a 10, qual você acha que é? '))
computador = random.randint(0, 10)
if 0 < jogador > 10:
    print('Esse número não entra em nosso jogo.')
    jogador = int(input('Digite outro número, mas lembre-se, tem que ser entre 1 e 10! '))
while jogador != computador:
    tentativa += 1
    print('Não foi dessa vez!')
    jogador = int(input('Mas não desanime, tente outro número: '))
    computador = random.randint(0, 10)
print(f'Boa! Dessa vez você acertou! Foram necessárias {tentativas} tentativas para conseguir vencer.')
