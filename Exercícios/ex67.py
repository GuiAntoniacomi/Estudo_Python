while True:
    n = int(input('Quer ver a tabuada de qual valor? Digite um número negativo para finalizar.'))
    if n < 0:
        print('Programa finalizado.')
        break
    t = 1
    while t <= 10:
        print(f'{n} x {t} = {n*t}')
        t += 1

#Resolução Guanabara
while True:
    n = int(input('Quer ver a tabuada de qual valor? Digite um número negativo para finalizar.'))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)

print('Programa finalizado.')

