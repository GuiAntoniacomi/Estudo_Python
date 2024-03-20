# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
# Valores da matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
maior_valor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[1][0] > 0:
            maior_valor = matriz[1][0]
            if matriz[1][1] > maior_valor:
                maior_valor = matriz[1][1]
                if matriz[1][2] > maior_valor:
                    maior_valor = matriz[1][2]
soma_coluna_3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
# Imprimindo resultado final da matriz
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da coluna 3 é {soma_coluna_3}.')
print(f'O maior valor foi {maior_valor}.')