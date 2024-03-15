from time import sleep
n = int(input('Digite um número: '))
lista = []
lista.append(n)
while True:
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

        
