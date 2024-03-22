'''tuplas = ()
listas = []
dicionarios = {}

dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = "M"
del.dados[idade]

filme1 ={
    'título': 'Star Wars', "ano": 1977, 'diretor': 'George Lucas'
}
filme2 = {
    'titulo': 'Avengers', "ano": 2012, 'diretor': 'Joss Whedon'
}
filme3 = {
    'titulo': 'Matrix', "ano": 1999, 'diretor': 'Wachowski'
}
print(filme1.values())
print(filme1.keys())
print(filme1.items())
for k, v in filme1.items():
    print(f'O {k} é {v}')

locadora = [
    filme1,
    filme2,
    filme3
]

print(locadora[1]['titulo'])'''

pessoas = {
    'nome': 'Guilherme',
    'sexo': 'M',
    'idade': 32
}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

Brasil = []
estado = {
    'uf': 'Rio de Janeiro', 'sigla': 'RJ'
}
estado2 = {
    'uf': 'Goiás','sigla': 'GO'
}
Brasil.append(estado)
Brasil.append(estado2)

print(Brasil)

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input('Digite o nome do estado: ')
    estado['sigla'] = input('Digite a sigla do estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O {k} é {v}.', end=" ")
    print()