# Mini-Projeto Avaliativo - Análise de Dados com Python SCtec/Senai

## Aluno

Vanderson Luiz C. Martins

## Turma

T2

---

## Objetivo

Realizar uma Análise Exploratória de Dados (AED) utilizando a base de Varejo disponibilizada para a disciplina.

O projeto contempla:

- Importação dos dados;
- Identificação de problemas na base;
- Limpeza de dados;
- Tratamento de nulos e duplicatas;
- Conversão de tipos;
- Estatística descritiva;
- Agrupamentos utilizando Pandas;
- Exportação da base limpa.

---

## Estrutura do Projeto

```text
Miniprojeto_Vanderson_Luiz_Turma2/
│
├── raw/
│   └── Base_Varejo.csv
│
├── output/
│   └── df_limpo.csv
│
├── Miniprojeto_SCtec.py
│
├── LICENSE
│
└── README.md
```

## Tecnologias Utilizadas

- Python 
- Pandas
- VS Code

## Como Executar

### Instalar Pandas

```bash
pip install pandas
```

### Executar o projeto

```bash
python Miniprojeto_SCtec.py
```

---

## Limpeza Realizada

- Remoção de colunas totalmente vazias;
- Conversão da coluna DATA para datetime;
- Remoção de registros duplicados;
- Tratamento da coluna CL_FHL;
- Verificação de categorias vazias.

---

## Estatística Descritiva

Foi realizada análise da coluna:

**CL_FHL (Número de Filhos)**

Métricas calculadas:

- Média
- Mediana
- Moda
- Desvio padrão
- Mínimo
- Máximo
- Quartis
- Contagem

---

## Conclusões

Após a análise exploratória foi possível identificar:

- Existência de colunas completamente vazias.
- Presença de registros duplicados.
- Necessidade de conversão da coluna DATA.
- Diferenças na distribuição de compras por gênero.
- Concentração de vendas em determinadas categorias.
- Importância do tratamento dos dados antes de análises futuras.

---

##

## Arquivos Gerados

- df_limpo.csv