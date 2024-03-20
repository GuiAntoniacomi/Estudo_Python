lista = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 != 0:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')