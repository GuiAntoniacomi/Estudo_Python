from time import sleep
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

while True:
    soma = n1 + n2
    mult = n1 * n2
    print("O que deseja fazer agora?\n\033[93m[1]\033[0m Somar\n\033[93m[2]\033[0m Multiplicar\n\033[93m[3]\033[0m Maior\n\033[93m[4]\033[0m Digitar novos números\n\033[93m[5]\033[0m Sair do programa")

    escolha = int(input("Digite a opção desejada: "))
    if escolha == 1:
        print(f'A soma de {n1} com {n2} é igual a {soma}.')
        sleep(1)
    elif escolha == 2:
        print(f'A multiplicação de {n1} e {n2} é igual a {mult}.')
        sleep(1)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número é {maior}.')
        sleep(1)
    elif escolha == 4:
        n1 = float(input("Perfeito! Qual seu novo primeiro valor? "))
        n2 = float(input("E qual o segundo? "))
    elif escolha == 5:
        print('Encerrando o programa....')
        sleep(1)
        break
    else:
        print('Opção inválida. Tente novamente.')
        sleep(1)