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