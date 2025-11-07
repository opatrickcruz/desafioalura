import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
loja_1 = pd.read_csv('dados/loja_1.csv')
loja_2 = pd.read_csv('dados/loja_2.csv')
loja_3 = pd.read_csv('dados/loja_3.csv')
loja_4 = pd.read_csv('dados/loja_4.csv')

# Análise 1: Faturamento total de cada loja
faturamento_loja_1 = loja_1['Preço'].sum()
faturamento_loja_2 = loja_2['Preço'].sum()
faturamento_loja_3 = loja_3['Preço'].sum()
faturamento_loja_4 = loja_4['Preço'].sum()

faturamento_lojas = {
    'Loja 1': faturamento_loja_1,
    'Loja 2': faturamento_loja_2,
    'Loja 3': faturamento_loja_3,
    'Loja 4': faturamento_loja_4
}

# Análise 2: Quantidade de produtos vendidos por categoria
quantidade_por_categoria_loja_1 = loja_1.groupby('Categoria do Produto')['Produto'].count()
quantidade_por_categoria_loja_2 = loja_2.groupby('Categoria do Produto')['Produto'].count()
quantidade_por_categoria_loja_3 = loja_3.groupby('Categoria do Produto')['Produto'].count()
quantidade_por_categoria_loja_4 = loja_4.groupby('Categoria do Produto')['Produto'].count()

# Análise 3: Média das avaliações dos clientes
avaliacao_media_loja_1 = loja_1['Avaliação da compra'].mean()
avaliacao_media_loja_2 = loja_2['Avaliação da compra'].mean()
avaliacao_media_loja_3 = loja_3['Avaliação da compra'].mean()
avaliacao_media_loja_4 = loja_4['Avaliação da compra'].mean()

# Análise 4: Produtos mais e menos vendidos
produtos_mais_vendidos_loja_1 = loja_1.groupby('Produto')['Quantidade de parcelas'].sum().sort_values(ascending=False).head(1)
produtos_menos_vendidos_loja_1 = loja_1.groupby('Produto')['Quantidade de parcelas'].sum().sort_values().head(1)

# Análise 5: Custo médio de frete
frete_medio_loja_1 = loja_1['Frete'].mean()
frete_medio_loja_2 = loja_2['Frete'].mean()
frete_medio_loja_3 = loja_3['Frete'].mean()
frete_medio_loja_4 = loja_4['Frete'].mean()

# Visualizações
# Gráfico 1: Faturamento Total de Cada Loja
plt.figure(figsize=(8,6))
lojas = list(faturamento_lojas.keys())
faturamento = list(faturamento_lojas.values())
plt.bar(lojas, faturamento, color=['blue', 'green', 'orange', 'red'])
plt.title('Faturamento Total por Loja')
plt.xlabel('Lojas')
plt.ylabel('Faturamento (R$)')
plt.tight_layout()
plt.show()

# Gráfico 2: Quantidade de Produtos Vendidos por Categoria
plt.figure(figsize=(10, 6))
quantidade_por_categoria_loja_1.plot(kind='bar', color='blue', label='Loja 1')
quantidade_por_categoria_loja_2.plot(kind='bar', color='green', label='Loja 2')
quantidade_por_categoria_loja_3.plot(kind='bar', color='orange', label='Loja 3')
quantidade_por_categoria_loja_4.plot(kind='bar', color='red', label='Loja 4')
plt.title('Quantidade de Produtos Vendidos por Categoria')
plt.xlabel('Categorias')
plt.ylabel('Quantidade')
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico 3: Média de Avaliações
plt.figure(figsize=(8,6))
avaliacoes = [avaliacao_media_loja_1, avaliacao_media_loja_2, avaliacao_media_loja_3, avaliacao_media_loja_4]
plt.bar(lojas, avaliacoes, color=['blue', 'green', 'orange', 'red'])
plt.title('Média de Avaliações por Loja')
plt.xlabel('Lojas')
plt.ylabel('Média de Avaliação')
plt.tight_layout()
plt.show()
