#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    cont = maior = 0
    print('=-'*30)
    print('\nAnalisando os valores passados...')
    print('Foram informados {} valores ao todo.'.format(len(num)))
    print('Os valores informados foram: ', end='')
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)