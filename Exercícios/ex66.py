cont = 0
s = 0
while True:
    n = int(input('Digite um número (999 para pausar o programa): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} número e a soma deles resulta em {s}.')
