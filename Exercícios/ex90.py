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