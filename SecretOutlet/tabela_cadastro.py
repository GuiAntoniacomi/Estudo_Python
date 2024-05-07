import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo - substitua por seus dados reais
data = pd.read_excel("C:\\Users\\anton\\OneDrive\\Área de Trabalho\\Cadastro Abril.xlsx")

# Criando DataFrame
df = pd.DataFrame(data)
df['DATA'] = pd.to_datetime(df['DATA'])

# Análises
## Atividade Diária
atividade_diaria = df.groupby(df['DATA']).size()

## Desempenho por Colaborador
total_cadastros_colaborador = df.groupby('Quem Fez').size()
distribuicao_situacao_colaborador = df.pivot_table(index='Quem Fez', columns='SITUAÇÃO', aggfunc='size', fill_value=0)

## Eficiência do Cadastro
situacao_count = df['SITUAÇÃO'].value_counts()

# Criando gráficos
fig, axs = plt.subplots(2, 2, figsize=(14, 12))

# Gráfico de Eficiência do Cadastro
situacao_count.plot(kind='bar', ax=axs[1, 0], color=['green', 'red'])
axs[1, 0].set_title('Eficiência do Cadastro')
axs[1, 0].set_xlabel('Situação')
axs[1, 0].set_ylabel('Quantidade')
axs[1, 0].set_xticklabels(axs[1, 0].get_xticklabels(), rotation=0)

# Gráfico de Desempenho por Colaborador
total_cadastros_colaborador.plot(kind='bar', ax=axs[0, 1], color='skyblue')
axs[0, 1].set_title('Total de Cadastros por Colaborador')
axs[0, 1].set_xlabel('Colaborador')
axs[0, 1].set_ylabel('Total de Cadastros')
axs[0, 1].set_xticklabels(axs[0, 1].get_xticklabels(), rotation=0)

# Gráfico de Atividade Diária
atividade_diaria.plot(kind='line', ax=axs[0, 0], marker='o', color='b')
axs[0, 0].set_title('Atividade Diária de Cadastro')
axs[0, 0].set_xlabel('Data')
axs[0, 0].set_ylabel('Quantidade de Cadastros')

# Gráfico de Distribuição de Situações por Colaborador
distribuicao_situacao_colaborador.plot(kind='bar', stacked=True, ax=axs[1, 1])
axs[1, 1].set_title('Distribuição de Situações por Colaborador')
axs[1, 1].set_xlabel('Colaborador')
axs[1, 1].set_ylabel('Quantidade')
axs[1, 1].set_xticklabels(axs[1, 1].get_xticklabels(), rotation=0)

plt.tight_layout()
plt.savefig('Cadastro_Team_Analysis.pdf', format='pdf')
plt.show()


