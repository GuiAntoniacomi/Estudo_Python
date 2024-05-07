import pandas as pd


#Criando um Dataframe de livros
info_livros = {
    'Título': ['Duna', 'Neuromancer', 'O Guia do Mochileiros das Gláxias', 'Admirável Mundo Novo', 'O Homem Duplicado'],
    'Autor': ['Frank Herbert', 'William Gibson', 'Douglas Adams', 'Aldous Huxley', 'José Saramago'],
    'Páginas': [688, 304, 256, 256, 336],
    'Preço': [49.90, 34.90, 39.90, 29.90, 44.90] 
}
df = pd.DataFrame(info_livros)

#Selecionar livros com mais de 300 páginas
livros_mais_300_pgs = df[df['Páginas'] > 300]
print(livros_mais_300_pgs)

# Adicinar coluna "Preço por Página"
df['Preço por Página'] = df['Preço'] / df['Páginas']   

resumo = df.describe()
'''
count: Número de observações não-nulas.
mean: Média dos valores.
std: Desvio padrão dos valores.
min: Menor valor.
25%: Primeiro quartil (mediana dos valores inferiores).
50%: Segundo quartil, ou mediana.
75%: Terceiro quartil (mediana dos valores superiores).
max: Maior valor.
'''
resumo_texto = df.describe(include='object')
resumo_arredondado = resumo.round(2)

print(resumo_arredondado)
print(resumo_texto)