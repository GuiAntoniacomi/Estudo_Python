#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = {}
nome = str(input('Nome: '))
alunos['Nome'] = nome
média = float(input(f'Média de {alunos["Nome"]} : '))
alunos['Média'] = média
print(f'O nome do aluno é {alunos["Nome"]}.')
print(f'A média foi {alunos["Média"]}.')
if média < 7:
    print(f'Infelizmente {alunos["Nome"]} foi reprovado.')
else:
    print(f'Parabéns! {alunos["Nome"]} foi aprovado(a).')

# Resolção Guanabara
    
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'   - {k} é igual {v}.')