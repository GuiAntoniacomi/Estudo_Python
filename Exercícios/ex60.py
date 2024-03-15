n = int(input('Digite um número: '))
fat = 1
for c in range(n, 0, -1):
    fat *= c
print(f'O fatorial de {n} é {fat}')

# utilizando while

n = int(input('Digite um número: '))
fat = 1
while n > 1:
    fat *= n
    n -= 1
print(f'O fatorial de {n} é {fat}')

# Resolção Guanabara
n = int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando {n}!...')
while c > 0:
    print(f'{c}', end=" ")
    print(' x ' if c > 1 else ' = ', end="")
    f *= c
    c -= 1
print(f'{f}')