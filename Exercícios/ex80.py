# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
for x in range(5):
    num = int(input('Digite um número: '))
    if not valores:
        valores.append(num)
    else:
        index = 0
        while index < len(valores) and num > valores[index]:
            index += 1
        valores.insert(index, num)
print('=-'*20)
print(f'Os números digitados em ordem foram: {valores}')

# Resolução Guanabara

lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Foi adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Foi adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*30)
print(f'Os valor digitados em ordem foram {lista}.')