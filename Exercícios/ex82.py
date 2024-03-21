# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

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
    if cont == 'N':
        break
print(f'A lista completa é {lista_completa}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {ímpares}')

# Resolução Guanabara

'''num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print("-="*30)
print(f'A lista completa é {num}.')
print(f" a lista de pares é {pares}.")
print(f'A lista de impares é {impares}.')
print('-='*30)'''