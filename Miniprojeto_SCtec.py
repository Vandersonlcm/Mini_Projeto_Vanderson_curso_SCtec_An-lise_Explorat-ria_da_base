import pandas as pd

# SPRINT 1 - IMPORTAÇÃO DOS DADOS

arquivo = "raw/Base_Varejo.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8"
)

print("\n1. INFORMAÇÕES GERAIS")

print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\nColunas da base:")
for coluna in df.columns:
    print(f"- {coluna}")

print("\nTipos de dados:")
print(df.dtypes)


# SPRINT 2 - IDENTIFICAÇÃO DE PROBLEMAS

print("\n2. VERIFICAÇÃO DE QUALIDADE DOS DADOS")

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