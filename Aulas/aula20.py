def mensagem(msg):
    print('-='*30)
    print(msg)
    print('-='*30)


# Programa Principa
mensagem('SISTEMA DE ALUNOS')


def soma(a, b):
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}.')


# Programa Principal    
soma(4, 5)
soma(8, 9)
soma(2, 1)

def contador(*num):
   tam = len(num)
   print(f'Foram informados {tam} valores ao todo.')

contador(2, 1, 7)
contador(7,0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)