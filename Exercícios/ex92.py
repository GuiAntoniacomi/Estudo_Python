from datetime import datetime

ano_atual = datetime.today().year

funcionarios = {}

# Coletando os dados
while True:
    nome = str(input('Nome: ')).strip()
    funcionarios['Nome'] = nome
    data_nascimento = int(input('Ano de nascimento: '))
    idade = ano_atual - data_nascimento
    funcionarios['idade'] = idade
    carteira_trabalho = int(input('Carteira de Trabalho (0 caso não tenha): '))
    funcionarios['ctps'] = carteira_trabalho
    if carteira_trabalho == 0:
        print('-='*30)
        print(f'O nome do colaborador é {funcionarios['Nome']}')
        print(f'A idade do colaborador é de {funcionarios["idade"]}')
        print(f'Ctps tem valor {funcionarios["ctps"]}, ou seja, não possui carteira de trabalho')
        break
    else:
        ano_cont = int(input('Ano de contratação: '))
        funcionarios['contratação'] = ano_cont
        salario = float(input('Salário: R$ '))
        funcionarios['salário'] = salario
        aposentadoria = idade + 35
        funcionarios['aposentadoria'] = aposentadoria
        # Imprimindo os dados
        print('-=' * 30)
        print(f'O nome do colaborador é {funcionarios['Nome']}.')
        print(f'A idade do colaborador é de {funcionarios["idade"]}.')
        print(f'Número da ctps é {funcionarios["ctps"]}.')
        print(f'O ano de contratação é de {funcionarios["contratação"]}.')
        print(f'O salário do colaborador é de R${funcionarios["salário"]}.')
        print(f'Colaborador se aposentará com {funcionarios["aposentadoria"]} anos.')
        break