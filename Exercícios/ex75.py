valores = ()
nove = 0
pares = ()
while len(valores) < 4:
    n = int(input('Digite um valor: '))
    valores += (n,)
    if n == 9:
        nove += 1
    elif n % 2 == 0:
        pares += (n,)
    elif n == 3:
        pos_3 = valores.index(3)

if nove == 0:
    print('O número nove não foi digitado.')
elif nove == 1:
    print(f'O número nove apareceu {nove} vez.')
else:
    print(f'O número nove apareceu {nove} vezes')

print(f'O número 3 ficou na {pos_3+1}ª posição')
if len(pares) == 0:
    print(f'Nenhum número par foi digitado.')
elif len(pares) == 1:
    print(f'O número par foi {pares}')
else:
    print(f'OS números pares foram {pares}')
