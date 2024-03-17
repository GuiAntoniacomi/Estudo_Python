while True:
    n = int(input('Quer ver a tabuada de qual valor? Digite um número negativo para finalizar.'))
    if n < 0:
        break
    t = 1
    while t <= 10:
        print(f'{n} x {t} = {n*t}')
        t += 1
