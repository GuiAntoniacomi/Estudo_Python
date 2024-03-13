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

# 2 Números pares que estão entre 1 e 50
for c in range(2, 51, 2):
    print(c, end='')
#Resolução mais longa
for n in range(1,51):
    if n % 2 == 0:
        print(n, end=" ")
print('Acabou!')    
# 3 Soma entre todos os número impares que são multiplos de 3 entre 1 e 500 - errei
s = 0
for c in range(3, 500, 3):
    s += c
print(f"O somaatório de todos os múltiplos de 3 é {s}") 
# Resolução Guanabara
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {soma} valores solicitados é {cont}')

# 4 Tabuada
num = int(input('Digite um número para ver sua tabuada:'))
for c in range(0,11)
    print(f'{num} x {c} = {num x c}')

# 5 Motrar soma apenas de pares
ns = []
for p in range(6):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        ns.append(n)
soma = sum(ns)
print("A soma dos números pares digitados é", soma)
# Resolução Guanabara
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} número pares e a soma foi {soma}')

# 6 A partir do primeiro termo e razão de uma PA, mostrar os 10 primeiros termos dessa PA.
p = int(input('Digite o primeiro termo:'))
r = int(input('Qual a razão dessa PA?'))
i = p + 10 * r
for c in range(p, i, r):
    print(c)
#Resolução Guanabara
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10-1)*razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=" → ")
print('Acabou')

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
    ano_nasc = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa:'))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maioridade += 1
    else:   
        menoridade += 1
print(f'{maioridade} pessoas já atingiram a maioridade.')
print(f'{menoridade} pessoas ainda não atingiram a maioridade.')

# Peso de 5 pessoas, qual maior e menor?
lista = []
for p in range(5):
    peso = float(input(f'Digite o peso da pessoa {p+1}:'))
    lista.append(peso)
maior = max(lista)
menor = min(lista)
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')

# Desafio leia nome, idade e sexo de 4 pessoas, retorne media de idade do grupo, homem mais velho e quantas mulheres tem menos de 20 anos
lista = []
mulheres_under_20 = []
homem_mais_velho = ['', 0] #[nome, idade]
total_mulheres_under_20 = 0
#loop para coleta dos dados
for d in range(4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').upper()

    if sexo == "M" and idade > homem_mais_velho[1]:
        homem_mais_velho = [nome, idade]
    
    if sexo == "F" and idade < 20:
        total_mulheres_under_20 += 1
    
    lista.append([nome, idade, sexo])

    if sexo == 'F':
        mulheres_under_20.append(idade)

idades_grupo = [pessoa[1] for pessoa in lista]
media_idade = sum(idades_grupo) / len(idades_grupo)

print(f'\nMédia de idade do grupo: {media_idade:.2f} anos')
print(f'Nome do homem mais velho: {homem_mais_velho[0]}')
print(f'Total de mulheres com menos de 20 anos: {total_mulheres_under_20}')
