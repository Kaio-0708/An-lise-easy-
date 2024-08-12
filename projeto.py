import pandas as pd
import plotly.express as px

# Carregar os dados do arquivo Excel
dados = pd.read_excel("vendas.xlsx")

# Análise inicial dos dados
dados.head()
dados.tail()
dados.shape
dados.info()
dados.describe()

# Análise específica de colunas
dados["loja"].value_counts()
dados["loja"].unique()
dados["forma_pagamento"].value_counts()

# Agrupamento de dados por loja e soma dos preços
dados.groupby("loja")["preco"].sum().to_frame()

# Agrupamento de dados por estado, cidade e loja
dados_agrupados = dados.groupby(["estado", "cidade", "loja"])["preco"].sum().to_frame()

# Exportar os dados agrupados para um arquivo Excel
dados_agrupados.to_excel("Faturamento.xlsx")

# Criação de um gráfico de histogramas
grafico = px.histogram(
    dados, 
    x="loja", 
    y="preco", 
    text_auto=True,
    title="Faturamento",
    color="forma_pagamento"
)

# Exibir o gráfico e salvar em um arquivo HTML
grafico.show()
grafico.write_html("Faturamento.html")

# Lista de colunas para gerar gráficos de histogramas
lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

# Loop para criar e salvar gráficos para cada coluna na lista
for coluna in lista_colunas: 
    grafico = px.histogram(
        dados, 
        x=coluna, 
        y="preco", 
        text_auto=True,
        title="Faturamento",
        color="forma_pagamento"
    )

    grafico.show()
    grafico.write_html(f"Faturamento-{coluna}.html")