qtdd_produto = 0
valor_total = 0
over_th = 0
cheaper = float('inf')

while True:
    nome_produto = str(input('Digite o nome do produto: '))
    qtdd_produto += 1
    preço_produto = float(input('Preço do produto:\nR$ '))
    valor_total += preço_produto
    if preço_produto >= 1000:
        over_th += 1
    if preço_produto < cheaper:
        cheaper = preço_produto
        nome_cheaper = nome_produto
    adicionar = str(input('Deseja continuar? {S/N} ')).upper()
    while adicionar not in ['S', 'N']:
        adicionar = str(input('Deseja continuar? {S/N} ')).upper()
    if adicionar == 'N':
        print('--------FIM DO PROGRAMA--------')
        print(f'O total gasto nas compras foi R${valor_total:.2f}.')
        print(f'Você comprou {over_th} produtos acima de R$1000,00.')
        print(f'O produto mais barato que você comprou foi {nome_cheaper} que custa R${cheaper:.2f}.')
        break