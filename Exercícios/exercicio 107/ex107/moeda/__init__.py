def metade(n, sit=False):
    if sit:
        return moeda(n / 2)
    else:
        return n / 2

def dobro(n, sit=False):
    if sit:
        return moeda(n * 2)
    else:
        return n * 2

def aumentar(n, a=10, sit=False):
    if sit:
        return moeda(n + (n * a / 100))
    else:
        return n + (n * a / 100)

def diminuir(n, r=13, sit=False): 
    if sit:
        return moeda(n - (n * r / 100))
    else:
        return n - (n * r / 100)

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxab=5):
    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)
    print(f'Preço analisad: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxab}% de redução: \t{diminuir(preço, taxab, True)}')
    print('-' * 30)
 