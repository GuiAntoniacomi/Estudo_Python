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

