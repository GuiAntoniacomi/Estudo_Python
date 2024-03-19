palavras = ('python', 'programação', 'exemplo', 'tupla', 'string', 'aleatório', 'lista', 'função', 'desenvolvimento', 'openai')

for palavra in palavras:
    vogais = [letra for letra in palavra if letra.lower() in 'aeiou']
    print(f'Na palavra {palavra.upper()}, temos as vogais {" ".join(vogais)}')