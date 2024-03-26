#relembrando funcionamento das listas
'''
dados = list()
dados.append('Pedro')
dados.append('25')

Cada item adicionado na lista cria um espaço com a informação e um index para essa informação, começando em 0.
Baseado no exemplo acima:
dados:
v = |Pedro|  25  |
i =    0     1

print(dados[0])
vai retornar o valor "Pedro"
print(dados[1])
vai retornar o valor "25"
'''
# Parte teórica
dados = list()
dados.append('Pedro')
dados.append('25')
pessoas = list()
pessoas.append(dados[:])

'''
No caso acima, estamos confinando a lista dados inteira dentro da lista pessoas, ficando mais ou menos assim:
pessoas:
v = ||'Pedro'|  25  |||'Maria'|  19  |||'João'|  32  ||
    |   0        1   |    0      1    |   0       1   |
i =          0                1               2
'''

pessoas = [
    ['Pedro', 25],
    ['Maria', 19],
    ['João', 32]
]
print(pessoas[0][0])
print(pessoas[1][1])