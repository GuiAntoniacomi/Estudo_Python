#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

'''cadastro = {}
ficha = []
contagem = 0
lista_idade = 0
while True:
    nome = str(input('Nome: '))
    cadastro['Nome'] = nome
    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Reposta inválida, tente novamente. Sexo [M/F]: ')).upper()
    cadastro['Sexo'] = sexo
    idade = int(input('Idade: '))
    cadastro['Idade'] = idade
    lista_idade += idade
    perg = str(input('Deseja continuar? [S/N] ')).upper()
    ficha.append(cadastro.copy())
    contagem += 1
    if perg == 'N':
        break
média_idade = lista_idade / contagem

# Separando homens e mulheres da lista
homens = []
mulheres = []
for c in range(len(ficha)):
    if ficha[c]['Sexo'] in 'Mm':
        homens.append(ficha[c]['Nome'])
    else:
        mulheres.append(ficha[c]['Nome'])

# Lista com pessoas acima de 18 anos
maioridade = list()
for i in range(len(ficha)):
    if ficha[i]['Idade'] >= 18:
        maioridade.append(ficha[i]['Nome'])

print('-=' * 30)
print(ficha)
print('-=' * 30)
print(f'Foram cadastradas {len(ficha)} pessoas.')
print(f'A média de idade do grupe é de {média_idade:.0f} anos.' )
print(f'As mulheres cadastradas foram: {mulheres}.')
print(f'As pessoas cadastradas que são maior de idade são {maioridade}.')'''

# Resolução Guanabara

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print('EROO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in "SN":
            break
        print('EROO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print(f'As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["Nome"]}', end=' ')
print()
print('Lista de pessoas que estão acima da média', end='')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<<<Encerrado>>>')