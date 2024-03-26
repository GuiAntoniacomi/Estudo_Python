#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
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

# Resolução Guanabara
from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
id dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    aposentadoria = dados['Idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'  - {k} tem o valor: {v}')