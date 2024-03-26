# Curo em Python - TUPLA
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[2])
print(lanche[0:2]) #python sempre ignoar o ultimo elemento
print(lanche[1:])
print(lanche[-1]) #hamburguer é o lanche 0 ou o -4

print(len(lanche))

for c in lanche:
    print(c)

# AS TUPLAS SÃO IMUTÁVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche)) #coloca a tupla em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))

pessoa = ('Guilherme', 32, 'M', 83.50)
