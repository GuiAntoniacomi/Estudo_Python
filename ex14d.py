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
