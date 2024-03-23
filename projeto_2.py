import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="chart_with_upwards_trend",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

caminho = r'C:\Users\Cristina\Desktop\modulo_16\demo011.csv'

renda = pd.read_csv(caminho)

# plots
st.write('## Gráficos por Idade')

fig, ax = plt.subplots(7, 1, figsize=(10, 50), gridspec_kw={'hspace': 1})  # Adicionando espaço vertical entre os subplots

sns.barplot(x='posse_de_imovel', y='idade', data=renda, ax=ax[0]).set_title('Posse de Imóvel', fontsize=14)
ax[0].tick_params(axis='both', which='major', labelsize=10)  # Reduzindo o tamanho da fonte do eixo x e y
ax[0].tick_params(axis='both', which='minor', labelsize=8)

sns.barplot(x='posse_de_veiculo', y='idade', data=renda, ax=ax[1]).set_title('Posse de Veículo', fontsize=14)
ax[1].tick_params(axis='both', which='major', labelsize=10)
ax[1].tick_params(axis='both', which='minor', labelsize=8)

sns.barplot(x='qtd_filhos', y='idade', data=renda, ax=ax[2]).set_title('Quantidade de Filhos', fontsize=14)
ax[2].tick_params(axis='both', which='major', labelsize=10)
ax[2].tick_params(axis='both', which='minor', labelsize=8)

sns.barplot(x='tipo_renda', y='idade', data=renda, ax=ax[3]).set_title('Tipo de Renda', fontsize=14)
ax[3].tick_params(axis='both', which='major', labelsize=10)
ax[3].tick_params(axis='both', which='minor', labelsize=8)

sns.barplot(x='educacao', y='idade', data=renda, ax=ax[4]).set_title('Educação', fontsize=14)
ax[4].tick_params(axis='both', which='major', labelsize=10)
ax[4].tick_params(axis='both', which='minor', labelsize=8)

sns.barplot(x='estado_civil', y='idade', data=renda, ax=ax[5]).set_title('Estado Civil', fontsize=14)
ax[5].tick_params(axis='both', which='major', labelsize=10)
ax[5].tick_params(axis='both', which='minor', labelsize=8)

sns.barplot(x='tipo_residencia', y='idade', data=renda, ax=ax[6]).set_title('Tipo de Residência', fontsize=14)
ax[6].tick_params(axis='both', which='major', labelsize=10)
ax[6].tick_params(axis='both', which='minor', labelsize=8)

for axis in ax:
    axis.set_xticklabels(axis.get_xticklabels(), rotation=45)

sns.despine()
st.pyplot(fig)


