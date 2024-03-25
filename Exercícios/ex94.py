cadastro = {}
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
    #lista_idade += idade
    perg = str(input('Deseja continuar? [S/N] ')).upper()
    ficha.append(cadastro.copy())
    #contagem += 1
    if perg == 'N':
        break
#média_idade = lista_idade / contagem
homens = []
mulheres = []
for c in range(len(ficha)):
    if ficha[c]['Sexo'] in 'Mm':
        homens.append(ficha[c]['Nome'])
    else:
        mulheres.append(ficha[c]['Nome'])
print('-=' * 30)
print(f' O grupo tem {len(ficha)} pessoas.')
#print(f'{média_idade:.2f}' )
print(f'{homens} homens e {mulheres} mulheres.')