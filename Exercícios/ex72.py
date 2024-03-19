números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezessei', 'Dezesseter', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20:'))
while n < 0 or n > 20:
    print(f'Você deve digitar um número entre 0 e 20.')
    n = int(input('Digite um número entre 0 e 20:'))
print(f'Você digitou o número {números[n]}.')

#Resolução Guanabara

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
           'Quinze', 'Dezessei', 'Dezesseter', 'Dezoito',
           'Dezenove', 'Vinte')
while true:
    num = int(input('Digite um número entre 0 e 20:'))
    if num < 0 or num > 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {cont[num]}.')
