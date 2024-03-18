from math import floor
print('='*40)
print('BANCO GUIZEIRA')
print('='*40)
saque = int(input("Qual o valor do saque?"))
qtdd50 = floor(saque / 50)
resto_50 = saque % 50
qtdd20 = floor(resto_50 / 20)
resto_20 = resto_50 % 20
qtdd10 = floor(resto_20 / 10)
resto_10 = resto_20 % 10
qtdd_1 = floor(resto_10 / 1)
print(f'Total de {qtdd50} cédulas de R$50,00')
print(f'Total de {qtdd20} cédulas de R$20,00')
print(f'Total de {qtdd10} cédulas de R$10,00')
print(f'Total de {qtdd_1} cédulas de R$1,00')   
print('='*40)
print('Volte sempre e tenha um ótimo dia!')

# Resolução Guanabara
print('='*30)
print(f'{'BANCO GUIZEIRA':^30}')
print('='*30)
valor = int(input("Qual o valor do saque?"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre e tenha um ótimo dia!')
