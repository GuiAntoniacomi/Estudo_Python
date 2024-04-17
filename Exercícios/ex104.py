def leiaint(num):
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro.\033[m')
            continue
        else:
            return n


n = leiaint('Digite um número inteiro.\033[m')
print(f'Você acabou de digitar o número {n}')