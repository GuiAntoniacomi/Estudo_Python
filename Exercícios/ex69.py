m = 0
f = 0
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
        m += 1
        if idade >= 18:
            homens_maioridade += 1
        else:
            homens_menoridade += 1
    elif Sexo == 'F':
        f += 1
        if idade < 20:
            mulheres_under_20 += 1
            if idade >= 18:
                mulheres_maioridade += 1
        else:
            homens_menoridade += 1
    perg = str(input("Deseja continuar? [S/N] ")).upper()
    while perg not in ['S', 'N']:  
        perg = str(input("Deseja continuar? [S/N] ")).upper()
    if perg == 'N':
        total_pessoas = m + f
        pessoas_maioridade = homens_maioridade + mulheres_maioridade
        pessoas_menoridade = homens_menoridade + mulheres_menoridade
        print('====== FIM DO PROGRAMA ======')
        print(f'Total de pessoas com mais de 18 anos: {pessoas_maioridade}')
        print(f'Ao todo temos {m} homens cadastraods')
        print(f'E temos {mulheres_under_20} mulheres com menos de 20 anos')
        break
    else:
        print('-'*20)
        print('CADASTRE UMA PESSOA')
        print('-'*20)

# Resolução Guanabara
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF'ç
        sexo = str(input('Sexo: '))
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] '))
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastraods')
print(f'E temos {totM20} mulheres com menos de 20 anos')