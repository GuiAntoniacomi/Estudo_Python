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
if nove == 0:
    print('O número nove não foi digitado.')
elif nove == 1:
    print(f'O número nove apareceu {nove} vez.')
else:
    print(f'O número nove apareceu {nove} vezes')
elif n == 3:
    pos_3 = valores.index(3)
    print(f'O número 3 ficou na {pos_3+1}ª posição')
if len(pares) == 0:
    print(f'Nenhum número par foi digitado.')
elif len(pares) == 1:
    print(f'O número par foi {pares}')
else:
    print(f'OS números pares foram {pares}')

#Resolução Guanabara

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitar foram ', end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")