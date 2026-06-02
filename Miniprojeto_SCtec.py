import pandas as pd
import matplotlib.pyplot as plt

# IMPORTAÇÃO DOS DADOS

arquivo = "raw/Base_Varejo.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8"
)

print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\nColunas da base:")
for coluna in df.columns:
    print(f"- {coluna}")

print("\nTipos de dados:")
print(df.dtypes)

# IDENTIFICAÇÃO DE PROBLEMAS

print("\nValores nulos por coluna:")
print(df.isnull().sum())

duplicados = df.duplicated().sum()

print(f"\nRegistros duplicados encontrados: {duplicados}")

colunas_vazias = [
    coluna
    for coluna in df.columns
    if df[coluna].isnull().all()
]

print("\nColunas totalmente vazias:")
print(colunas_vazias)

# LIMPEZA DOS DADOS

# Remoção de colunas totalmente vazias

df = df.drop(columns=colunas_vazias)

# Conversão da coluna DATA

df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)

datas_invalidas = df["DATA"].isnull().sum()

print(f"\nDatas inválidas encontradas: {datas_invalidas}")

# Remoção de linhas com datas inválidas

df = df.dropna(subset=["DATA"])

# Remoção de duplicatas

antes = len(df)

df = df.drop_duplicates()

depois = len(df)

print(f"\nDuplicatas removidas: {antes - depois}")

# Tratamento da coluna Número de Filhos

df["CL_FHL"] = pd.to_numeric(
    df["CL_FHL"],
    errors="coerce"
)

# Substituição de valores nulos pela mediana

mediana_filhos = df["CL_FHL"].median()

df["CL_FHL"] = df["CL_FHL"].fillna(
    mediana_filhos
)

# Categorias vazias

categorias_vazias = (
    df["PR_CAT"]
    .astype(str)
    .str.strip()
    .eq("")
    .sum()
)

print(f"\nCategorias vazias: {categorias_vazias}")

#  ESTATÍSTICA DESCRITIVA

print("\nColuna analisada: CL_FHL (Número de Filhos)")

print(f"Média: {df['CL_FHL'].mean():.2f}")
print(f"Mediana: {df['CL_FHL'].median():.2f}")
print(f"Desvio padrão: {df['CL_FHL'].std():.2f}")
print(f"Moda: {df['CL_FHL'].mode()[0]}")
print(f"Valor máximo: {df['CL_FHL'].max()}")
print(f"Valor mínimo: {df['CL_FHL'].min()}")

print("\nResumo estatístico completo:")
print(df["CL_FHL"].describe())

agrupamento_genero = (
    df.groupby("CL_GENERO")
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_genero)

agrupamento_categoria = (
    df.groupby("PR_CAT")
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_categoria.head(10))

agrupamento_segmento = (
    df.groupby("CL_SEG")
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_segmento)

# EXPORTAÇÃO DA BASE LIMPA

df.to_csv(
    "output/df_limpo.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo df_limpo.csv gerado com sucesso.")

print(f"Registros finais: {len(df)}")
print(f"Colunas finais: {len(df.columns)}")

# GRÁFICO - DISTRIBUIÇÃO DAS COMPRAS POR CATEGORIA

top_categorias = (
    df.groupby("PR_CAT")
      .size()
      .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

top_categorias.plot(kind="bar")

plt.title("Distribuição das Compras por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de Compras")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "grafico_categorias.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# GRÁFICO  - COMPRAS POR GÊNERO

compras_genero = (
    df.groupby("CL_GENERO")
      .size()
)

plt.figure(figsize=(8, 8))

plt.pie(
    compras_genero,
    labels=compras_genero.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribuição das Compras por Gênero")

plt.savefig(
    "grafico_genero.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# GRÁFICO - CLIENTES POR SEGMENTO

clientes_segmento = (
    df.groupby("CL_SEG")
      .size()
      .sort_values()
)

plt.figure(figsize=(10, 5))

ax = clientes_segmento.plot(
    kind="barh"
)

plt.title("Quantidade de Clientes por Segmento")
plt.xlabel("Quantidade de Clientes")
plt.ylabel("Segmento")

# Exibir valores ao lado das barras

for i, valor in enumerate(clientes_segmento):
    plt.text(
        valor,
        i,
        f" {valor:,}".replace(",", "."),
        va="center"
    )

plt.tight_layout()

plt.savefig(
    "grafico_segmento.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()




