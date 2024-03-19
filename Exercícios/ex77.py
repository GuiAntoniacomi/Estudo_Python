palavras = ('python', 'programação', 'exemplo', 'tupla', 'string', 'aleatório', 'lista', 'função', 'desenvolvimento', 'openai', 'trabalhar')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')