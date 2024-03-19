valores = []
while True:
    num = int(input('Digite um valor para adicionar a lista: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Valor ja está na lista, não será adicionado. ')
    per = str(input('Deseja continuar? [S/N] ')).upper()
    if per == 'N':
        break
valores.sort()
print('=-'*25)
print(f'Os números digitados foram {valores}')