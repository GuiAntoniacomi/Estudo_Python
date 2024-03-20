'''valores = [int(input('Digite um valor para a Posição 0:')), 
           int(input('Digite um valor para a Posição 1:')), 
           int(input('Digite um valor para a Posição 2:')), 
           int(input('Digite um valor para a Posição 3:')), 
           int(input('Digite um valor para a Posição 4:'))]

print('=-'*30)
print(f'Você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

pos_maiores = [i for i, v in enumerate(valores) if v == maior]
pos_menores = [i for i, v in enumerate(valores) if v == menor]

print(f'O maior valor digitado foi {maior} nas posições {pos_maiores}.')
print(f'O menor valor digitado foi {menor} nas posições {pos_menores}.')
'''

valores = [
    int(input('Digite um valor para a Posição 0:')),
    int(input('Digite um valor para a Posição 0:')),
    int(input('Digite um valor para a Posição 0:')),
    int(input('Digite um valor para a Posição 0:')),
    int(input('Digite um valor para a Posição 0:'))
]

print('=-'*30)
print(f'Você digitou os valores {valores}')
maior_valor = max(valores)
menor_valor = min(valores)
pos_maior = []
pos_menor = []
for m in enumerate(valores):
    if m[1] == maior_valor:
        pos_maior.append(m[0])
    if m[1] == menor_valor:
        pos_menor.append(m[0])

if len(pos_maior) == 1:
    print(f'O maior valor digitado foi {maior_valor} na posição {pos_maior[0]}')
elif len(pos_maior) == 2:
    print(f'O maior valor digitado foi {maior_valor} nas posições {pos_maior[0]} e {pos_maior[1]}')
elif len(pos_maior) == 3:
    print(f'O maior valor digitado foi {maior_valor} nas posições {pos_maior[0]}, {pos_maior[1]} e {pos_maior[2]}')
elif len(pos_maior) == 4:
    print(f'O maior valor digitado foi {maior_valor} nas posições {pos_maior[0]}, {pos_maior[1]}, {pos_maior[2]} e {pos_maior[3]}')
else:
    print(f'Foi digitado apenas o valor {maior_valor}, ele aparece em todas as posições, é o maior e o menor da lista.')
    
if len(pos_menor) == 1:
    print(f'O menor valor digitado foi {menor_valor} na posição {pos_menor[0]}')
elif len(pos_menor) == 2:
    print(f'O menor valor digitado foi {menor_valor} na posição {pos_menor[0]} e {pos_menor[1]}')
elif len(pos_menor) == 3:
    print(f'O menor valor digitado foi {menor_valor} nas posições {pos_menor[0]}, {pos_menor[1]} e {pos_menor[2]}')
elif len(pos_menor) == 4:
    print(f'O menor valor digitado foi {menor_valor} nas posições {pos_menor[0]}, {pos_menor[1]}, {pos_menor[2]} e {pos_menor[3]}')


# Resolução Guanabara
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c ==0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end=" ")
for i, v in enumerate(listanum): # i = indice e v = valor
    if v == maior:
        print(f'{i}...', end=" ")
print()
print(f'O menor valor digitado foi {menor} nas posições ', end=" ")
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end="")
print()