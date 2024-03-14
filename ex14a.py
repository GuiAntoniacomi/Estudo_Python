s = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while s not in ["M", "F"]:
    print('Por favor, verifique sua reposta e tente novamente.')
    s = str(input('Digite seu sexo: [M/F]')).strip().upper()
if s == 'M':
    print('O sexo informado foi masculino')
else:
    print('O sexo informado foi feminino')