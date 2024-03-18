from random import randint
valores = ()
menor_valor = 11
maior_valor = 0
while len(valores) < 5:
    sorteado = randint(1,  10)
    valores += (sorteado,)

    if valores == 0:
        menor_valor = sorteado
        maior_valor = sorteado
    elif sorteado < menor_valor:
        menor_valor = sorteado
    elif sorteado > maior_valor:
        maior_valor = sorteado
    if len(valores) > 5:
        break
print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi: {maior_valor}')
print(f'O menor valor sorteado foi: {menor_valor}')