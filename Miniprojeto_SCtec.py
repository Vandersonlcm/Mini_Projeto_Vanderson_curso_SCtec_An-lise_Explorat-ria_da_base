import pandas as pd

# SPRINT 1 - IMPORTAÇÃO DOS DADOS

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


# SPRINT 2 - IDENTIFICAÇÃO DE PROBLEMAS

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

# SPRINT 3 - LIMPEZA DOS DADOS

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

# SPRINT 4 - ESTATÍSTICA DESCRITIVA

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

print("\nProjeto concluído com sucesso.")

