números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezessei', 'Dezesseter', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20:'))
while n < 0 or n > 20:
    print(f'Você deve digitar um número entre 0 e 20.')
    n = int(input('Digite um número entre 0 e 20:'))
print(f'Você digitou o número {números[n]}.')