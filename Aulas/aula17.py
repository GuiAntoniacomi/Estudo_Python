'''
Tuplas:
lanche = ('hamburguer', 'sucon', 'pizza', 'pudim')
print(lanche[2])
tuplas = são imutáveis
'''
# Listas
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche[2])
lanche[2] = "picolé"
print(lanche[2])

# Para adicionar elementos na lista
lanche.append('cookie')
# Para adicionar elementos em alguma posição especifica da lista
lanche.insert(0, 'cachorro quente')

print(lanche)

#Apagar elementos pelo índice
del lanche[3]
lanche.pop(3) #Se nao colocar nenhum número, apaga o últmo item da lista
#Para remover pelo nome
lanche.remove('picolé')

if 'pizza' in lanche:
    lanche.remove('cookie')

#Criar listas através de range
valores = list(range(4, 11))
print(valores)

#Organizando valores
valores = [8,2,5,4,9,3,0]
valores.sort()
valores.sort(reverse=True)

#Quantidade de elementos na lista
valores = [8,2,5,4,9,3,0]
len(valores)
print(len(valores))

# Exemploe aula
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos')

########################################################################
valores = list()


for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# Criar uma cópia
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
a = [2, 3, 4, 7]
b = a[:] #dessa forma é feito uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


