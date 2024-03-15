p = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão dessa PA? '))
contador = 0
lista = []
while contador < 10:  # 10 representa o número de termos que você quer imprimir
    print(p, end=' ')
    p += r  # Adiciona a razão para obter o próximo termo
    contador += 1
    lista.append(p)
    ultimo_valor = lista[-1] 
    
print()  # Imprime uma linha em branco
print('Deseja ver mais valores? Se sim, digite quantos a mais gostaria de ver; se não, digite 0: ')
cont = int(input('Qual opção escolhe? '))
if cont == 0:
    print("Programada encerrado.")
else:
    while contador < 10+cont:
        print(ultimo_valor, end=' ')
        ultimo_valor += r
        contador += 1

# Resolução Guanabara
print('Gerador de PA')
print('=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end=" ")
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')