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