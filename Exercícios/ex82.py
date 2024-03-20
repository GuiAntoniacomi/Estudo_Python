lista_completa = []
pares = []
ímpares = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
    lista_completa.append(n)
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    while cont not in 'SN':
        n = int(input('Digite um número: '))
    if cont == 'N':
        break
print(f'A lista completa é {lista_completa}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {ímpares}')