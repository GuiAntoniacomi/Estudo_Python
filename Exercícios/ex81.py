# Crie um programa que vai ler vários números e colocar em uma lista.

lista =[]
while True:
    numeros =  int(input('Digite o valor desejado: '))
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    lista.append(numeros)
    if cont == 'N':
        break

lista.sort(reverse=True)
print('=-'*25)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista em ordem descescente fica: {lista}')
if 5 not in lista:
    print('O valor 5 não foi digitado.')
else:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)} da lista.')
print('=-'*25)

# Resolução Guanabara

lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continua? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*25)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem descescente fica: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)} da lista.')
else:
    print('O valor 5 não foi digitado.')
print('=-'*25)