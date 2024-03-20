valores = []
for x in range(5):
    num = int(input('Digite um número: '))
    if not valores:
        valores.append(num)
    else:
        index = 0
        while index < len(valores) and num > valores[index]:
            index += 1
        valores.insert(index, num)
print('=-'*20)
print(f'Os números digitados em ordem foram: {valores}')