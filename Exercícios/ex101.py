from datetime import date 

def voto(n):
    atual = date.today().year
    idade = atual - n
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


n = int(input('Digite o seu ano de nascimento: '))
voto(n)