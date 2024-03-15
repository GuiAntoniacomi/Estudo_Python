from time import sleep
n = int(input('Digite um número: '))
lista = []
while True:
    n = int(input('Digite um número: '))
    lista = []
    lista.append(n)
    print('Quer continuar adicionando números?\n[1] Sim\n[2] Não')
    x = int(input('Digite a opção escolhida:'))
    if x == 1:
        n = int(input('Digite o próximo número: '))
        lista.append(n)
    elif x == 2:
        print('Calculando...')
        sleep(2)
        break
    else:
        print('Escolha uma opção valida.')
media = sum(lista) / len(lista)
maior = max(lista)
menor = min(lista)
print(f'O maior número digitado foi {maior:.0f} e o menor foi {menor:.0f} e a média dos números digitados é {media:.0f}.')

# Resolução Guanabara
'''resp = "S"
s = q = m = 0
while resp in "Ss":
    n = int(input('Digite um número: '))
    s += n
    q += 1
    if q == 1: # Pois o primeiro numero digitado é tanto o maior quanto o menor
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
m = s/q
print(f'Você digitou {q} números e a média foi {m}.')     
print(f'O maior valor foi {maior} e o menor foi {menor}.')'''