# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final: A) Quantas pessoas foram. | B) Uma listagem com as pessoas mais pesadas. | C) Uma listagem com as pessoas mais leves.
cadastro = []
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    cadastro.append((nome, peso))
    cont = input('Deseja continuar? [S/N] ').upper()
    while cont not in 'SN':
        print("Resposta inválida, tente novamente.")
        cont = input('Deseja continuar? [S/N] ').upper()
    if cont == "N":
        break
maior_peso = menor_peso = 0
for _, peso in cadastro:  # Change here to iterate over (nome, peso) tuples
    if maior_peso == menor_peso == 0:
        maior_peso = menor_peso = peso
    elif peso >= maior_peso:
        maior_peso = peso
    elif peso <= menor_peso:
        menor_peso = peso
qtdd_pessoas = len(cadastro)
print(f'Ao todo você cadastrou {qtdd_pessoas} pessoas.')
print(f'O maior peso cadastrado foi {maior_peso:.2f}kg.', end=" ")
for p in cadastro:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=" ")
print()
print(f'O menor peso cadastrado foi {menor_peso:.2f}kg.', end=" ")
for p in cadastro:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=" ")
print()


# Resolução Guanabara

'''temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=" ")
print(f'O menor peso foi de {menor:.2f}Kg')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=" ")'''
