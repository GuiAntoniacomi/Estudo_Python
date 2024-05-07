try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[31mERRO! Digite um número inteiro.\033[m')
    r = 0
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except Exception as erro:
    print(f'Foi encontrar um erro {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre, obrigado!')