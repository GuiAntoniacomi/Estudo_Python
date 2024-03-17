from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
v = 0
while True:
    n = int(input('Diga seu número:'))
    c = randint(1,100)
    total = n + c
    escolha = str(input('Par ou ímpar? [P/I]')).upper()
    
    # Verificador de par ou ímpar
    if total % 2 == 0:
        resultado = "PAR"
    elif total % 2 != 0:
        resultado = "ÍMPAR"
    print('-' * 20)
    print(f'Você jogou {n} e o computador jogou {c}, total de {total}. Deu {resultado}!')
    print('-' * 20)

    # Analisando quem venceu
    if escolha == 'P' and resultado == "PAR":
        v += 1
        print('Você ganhou!')
        print('Vamos jogar novamente...') 
        print('=-' * 20)    
    elif escolha == 'I' and resultado == "ÍMPAR":
        v += 1
        print('Você ganhou!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    else:
        print('Você perdeu!')
        print('=-' * 20)
        if v == 1:
            print(f'Game over!! Você venceu {v} vez. ')
        else:
            print(f'Game over!! Você venceu {v} vezes. ')
        break
    