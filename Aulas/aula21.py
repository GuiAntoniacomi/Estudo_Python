print(input.__doc__)
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma entre {a}, {b} e {c} é igual a {s}.')


somar(3, 2)
somar(a=5, c=11)

#variavel global e  local

def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s 


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
f1 = fatorial(n)
print(f'O fatorial de {n} é {f1}.')
