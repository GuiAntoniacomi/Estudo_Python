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
