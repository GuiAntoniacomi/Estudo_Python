'''from math import floor
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
print('Volte sempre e tenha um ótimo dia!')'''

print('='*40)
print('BANCO GUIZEIRA')
print('='*40)
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
saque = int(input("Qual o valor do saque?"))
while True:
    no