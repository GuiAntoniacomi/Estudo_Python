# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

abertos = []
pa = "("
pf = ")"
expressao = input('Digite a expressão: ')
for caractere in expressao:
    if caractere == pa:
        abertos.append(caractere)
    elif caractere == pf:
        if abertos:
            abertos.pop()  # Remove o último parêntese aberto da lista
        else:
            print('Sua expressão é inválida!')
            break
if not abertos:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')

# Resolução Guanabara
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')

