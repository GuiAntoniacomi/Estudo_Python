import pandas as pd
import matplotlib.pyplot as plt

# Dados de cadastros por colaborador em cada marketplace
data_marketplaces = {
    'DAFITI': {'Beatriz': 488, 'Gustavo': 165, 'Total': 653},
    'MERCADO LIVRE': {'Beatriz': 581, 'Gustavo': 579, 'Total': 1160},
    'NETSHOES/ZATTINI': {'Beatriz': 301, 'Gustavo': 147, 'Total': 448}
}

# Dados de produtos publicados por canal
produtos_publicados = {'DAFITI': 3504, 'MERCADO LIVRE': 4389, 'NETSHOES/ZATTINI': 3361}

# Total por colaborador
total_por_colaborador = {'Beatriz': 1370, 'Gustavo': 891}

# Convertendo dados para DataFrames
marketplaces = list(data_marketplaces.keys())
beatriz_contrib = [data_marketplaces[m]['Beatriz'] for m in marketplaces]
gustavo_contrib = [data_marketplaces[m]['Gustavo'] for m in marketplaces]

df_marketplaces = pd.DataFrame({
    'Beatriz': beatriz_contrib,
    'Gustavo': gustavo_contrib
}, index=marketplaces)

# Criar figura e eixos para todos os seis gráficos
fig, axs = plt.subplots(3, 2, figsize=(16, 18))

# Gráfico 1: Total de Cadastros por Marketplace com valores nas barras
marketplace_totals = df_marketplaces.sum(axis=1)
bars_marketplace = axs[0, 0].bar(marketplace_totals.index, marketplace_totals.values, color='lightblue')
axs[0, 0].set_title('Total de Cadastros por Marketplace')
axs[0, 0].set_ylabel('Total de Cadastros')
axs[0, 0].set_xlabel('Marketplace')
for bar in bars_marketplace:
    axs[0, 0].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom')

# Gráfico 2: Total de Cadastros por Colaborador com valores nas barras
bars_colaborador = axs[0, 1].bar(total_por_colaborador.keys(), total_por_colaborador.values(), color=['pink', 'lightgreen'])
axs[0, 1].set_title('Total de Cadastros por Colaborador')
axs[0, 1].set_ylabel('Total de Cadastros')
axs[0, 1].set_xlabel('Colaborador')
for bar in bars_colaborador:
    axs[0, 1].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom')

# Repetir gráficos 3-5: Contribuição por Colaborador em cada Marketplace
for i, marketplace in enumerate(marketplaces):
    axs[(i+2)//2, (i+2)%2].bar(['Beatriz', 'Gustavo'], [df_marketplaces.loc[marketplace, 'Beatriz'], df_marketplaces.loc[marketplace, 'Gustavo']], color=['pink', 'lightgreen'])
    axs[(i+2)//2, (i+2)%2].set_title(f'Contribuição por Colaborador - {marketplace}')
    axs[(i+2)//2, (i+2)%2].set_ylabel('Total de Cadastros')
    axs[(i+2)//2, (i+2)%2].set_xlabel('Colaborador')
    for bar in axs[(i+2)//2, (i+2)%2].patches:
        axs[(i+2)//2, (i+2)%2].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom')

# Gráfico 6: Produtos Publicados por Canal
axs[2, 1].bar(produtos_publicados.keys(), produtos_publicados.values(), color='purple')
axs[2, 1].set_title('Produtos Publicados por Canal')
axs[2, 1].set_ylabel('Quantidade de Produtos')
axs[2, 1].set_xlabel('Canal')
for bar in axs[2, 1].patches:
    axs[2, 1].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom')

# Ajustar layout e salvar os gráficos em PDF
plt.tight_layout()
plt.savefig('All_Graphs.pdf', format='pdf')
plt.show()
