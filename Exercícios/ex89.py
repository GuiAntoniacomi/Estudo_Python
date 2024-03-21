boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    cont = str(input('Adicionar mais alunos? [S/N] ')).upper()

    media = (nota1 + nota2) / 2
    boletim.append((nome, nota1, nota2))
    while cont not in 'SN':
        print('Resposta inválida, tente novamente.')
        cont = str(input('Adicionar mais alunos? [S/N] ')).upper()
    if cont == 'N':
        break
print(boletim[0])