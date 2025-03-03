import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios
dados_vendas = pd.DataFrame({
    "dias": ["Seg", "Ter", "Qua", "Qui", "Sex"],
    "vendas": [100, 200, 150, 300, 250],
    "clientes": [50, 80, 60, 120, 100],
    "lucro": [30, 50, 40, 70, 60]
})

# Criar DataFrame com apenas colunas numéricas para correlação
df_corr = dados_vendas.select_dtypes(include='number')  # Seleciona apenas colunas numéricas

# Gerar Heatmap
sns.heatmap(df_corr.corr(), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlação Entre Variáveis de Vendas")
plt.show()


# Gráfico de Dispersão - Clientes x Vendas
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Clientes", y="Total Vendas", data=df_vendas, hue="Dia", palette="Set1")
plt.title("Clientes vs. Total de Vendas")
plt.xlabel("Número de Clientes")
plt.ylabel("Total de Vendas")
plt.legend(title="Dia")
plt.show()

# Heatmap - Correlação entre Variáveis
plt.figure(figsize=(8, 5))
sns.heatmap(df_vendas.corr(), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlação entre Variáveis")
plt.show()
