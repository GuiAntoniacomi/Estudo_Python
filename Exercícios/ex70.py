qtdd_produto = valor_total = over_th = 0
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

# Resoluçao Guanabara
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    resp = str(input(' Quer continuar? [S/N] '))strip().upper()[0]
    while resp not in 'SN':
        resp = str(input(' Quer continuar? [S/N] '))strip().upper()[0]
    if resp == "N":
        break
print({'FIM DO PROGRAMA':-^40})
print(f' O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')