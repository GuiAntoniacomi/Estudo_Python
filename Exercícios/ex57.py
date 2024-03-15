s = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while s not in ["M", "F"]:
    print('Por favor, verifique sua reposta e tente novamente.')
    s = str(input('Digite seu sexo: [M/F]')).strip().upper()
if s == 'M':
    print('O sexo informado foi masculino')
else:
    print('O sexo informado foi feminino')

#Resolução Guanabara
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in "MmDf":
    sexo = str(input('Dados inválisdo. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')