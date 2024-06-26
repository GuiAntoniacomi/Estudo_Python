produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.20)
produto_lista = 0
preço_lista = 1
contagem_strings = sum(isinstance(item, str) for item in produtos)
total_produtos = contagem_strings
while total_produtos > 0: 
    print(f'{produtos[produto_lista]:.<25}R${produtos[preço_lista]:>7.2f}')
    produto_lista += 2
    preço_lista += 2
    total_produtos -= 1
    if total_produtos == 0: 
        break

#Resolução Guanabara

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
             'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
    