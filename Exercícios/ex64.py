n = 0
lista = []
while n != 999:
    n = int(input('Digite um número: '))
    lista.append(n)
x = len(lista) - 1
y = sum(lista) - 999
print(f'Foram digitados {x} valores e a soma deles é igual a {y}.')