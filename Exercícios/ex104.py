#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

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

# Resolução Guanabara

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
        if ok:
            break
    return valor    

n = leiaint('Digite um número inteiro.\033[m')	
print(f'Você acabou de digitar o número {n}')