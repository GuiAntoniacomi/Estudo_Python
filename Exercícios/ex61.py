p = int(input('Digite o primeiro termo:'))
r = int(input('Qual a razão dessa PA?'))
i = p + 10 * r
for c in range(p, i, r):
    print(c)

#Usando while
p = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão dessa PA? '))
contador = 0

while contador < 10:  # 10 representa o número de termos que você quer imprimir
    print(p, end=' ')
    p += r  # Adiciona a razão para obter o próximo termo
    contador += 1

# Resolução Guanabara
print('Gerador de PA')
print('=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} → ', end=" ")
    termo += r
    cont += 1
print('FIM')