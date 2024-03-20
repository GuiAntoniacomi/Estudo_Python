#
'''Alternativa 1'''
cadastro = list()
qtdd_pessoas = mais_pes = menos_pes = 0

while True:
    nome = cadastro.append(str(input('Digite o nome: ')))
    peso = cadastro.append(float(input('Digite o peso: ')))
    qtdd_pessoas += 1
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    while cont not in 'SN':
        print("Resposta inválida, tente novamente.")
    if cont == "N":
        break
print(cadastro)

'''Alternativa 2'''
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

print(cadastro)
print(f'Ao todo você cadastrou {qtdd_pessoas} pessoas.')
print(f'O maior peso cadastrado foi {maior_peso:.2f}kg.')
print(f'O menor peso cadastrado foi {menor_peso:.2f}kg.')
