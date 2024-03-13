s = 0
for c in range(0,4):
    n = int(input('Digite um valor:'))
    s += n
print(f"O somaatório de todos os valores foi {s}")  

# Contagem regressiva
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)

# Números pares que estão entre 1 e 50
for c in range(2, 51, 2):
    print(c)

# Soma entre todos os número impares que são multiplos de 3 entre 1 e 500
s = 0
for c in range(3, 500, 3):
    s += c
print(f"O somaatório de todos os múltiplos de 3 é {s}") 

# Tabuada
num = int(input('Digite um número para ver sua tabuada:'))
for c in range(0,11)
    print(f'{num} x {c} = {num x c}')

# Motrar soma apenas de pares
ns = []
for p in range(6):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        ns.append(n)
soma = sum(ns)
print("A soma dos números pares digitados é", soma)

# A partir do primeiro termo e razão de uma PA, mostrar os 10 primeiros termos dessa PA.
p = int(input('Digite o primeiro termo:'))
r = int(input('Qual a razão dessa PA?'))
i = p + 10 * r
for c in range(p, i, r):
    print(c)

# Se é numero primo - com if
n = int(input('Digite um número:'))
    if n % 1 == 0 and n % n == 0:
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')

# Agora utilizando For
n = int(input('Digite um número:'))
primo = True
for i in range(2,n):
    if n % i == 0:
        primo = False
        break
if primo and n > 1:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')

# Descobrir se as pessoas da lista atingiram a maioridade:
from datetime import datetime
ano_atual = datetime.today().year
maioridade = 0
menoridade = 0

for i in range(7):
    ano_nasc = int(input(f'Digite o ano de nascimento da {i+1}ª pessoas:'))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maioridade += 1
    else:   
        menoridade += 1
print(f'{maioridade} pessoas já atingiram a maioridade.')
print(f'{menoridade} pessoas ainda não atingiram a maioridade.')
