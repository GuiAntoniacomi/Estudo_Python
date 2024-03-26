def maior(*num):
    print('=-'*30)
    print('Foram informados {} valores ao todo.'.format(len(num)))
    print('Os valores informados foram: ', end='')
    for valor in num:
        print(valor, end=' ')
    print()


numeros = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    p = str(input('Deseja adicionar mais números? [S/N] ')).upper()[0]
    if p == 'N':
        break

maior(*numeros)
