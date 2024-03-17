h = 0
m = 0
mulheres_maioridade = 0
homens_maioridade = 0
mulheres_menoridade = 0
homens_menoridade = 0
mulheres_under_20 = 0

print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)

while True:
    idade = int(input('Digite sua idade: '))
    Sexo = str(input('Digite seu sexo: [M/F] ')).upper()
    while Sexo not in ['M', 'F']:  # Verifica se o sexo é válido
        Sexo = str(input('Digite seu sexo: [M/F] ')).upper()
    if Sexo == 'M':
        h += 1
        if idade >= 18:
            homens_maioridade += 1
        else:
            mulheres_menoridade += 1
    elif Sexo == 'F':
        m += 1
        if idade >= 18:
            mulheres_maioridade += 1
            if idade < 20:
                mulheres_under_20 += 1
        else:
            homens_menoridade += 1
    perg = str(input("Deseja continuar? [S/N] ")).upper()
    while perg not in ['S', 'N']:  
        perg = str(input("Deseja continuar? [S/N] ")).upper()
    if perg == 'S':
        print('-'*20)
        print('CADASTRE UMA PESSOA')
        print('-'*20)
    else:
        total_pessoas = h + m
        pessoas_maioridade = homens_maioridade + mulheres_maioridade
        pessoas_menoridade = homens_menoridade + mulheres_menoridade
        print(f'Total de pessoas com mais de 18 anos: {pessoas_maioridade}')
        print(f'Ao todo temos {h} homens cadastraods')
        print(f'E temos {mulheres_under_20} mulheres com menos de 20 anos')
        break
                
