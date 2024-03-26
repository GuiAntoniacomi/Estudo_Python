'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar}) número ímpares.')'''

# Prática de break

'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')

    