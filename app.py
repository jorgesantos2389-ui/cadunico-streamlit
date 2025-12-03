import streamlit as st
import pandas as pd

# Título do painel
st.title("Cadastro Único - Situação de Rua")

# Carregar o arquivo Excel
df = pd.read_excel("VIS DATA 3 beta.xlsx")

# Selecionar apenas as colunas relevantes
df = df[[
    "Código",
    "Unidade Territorial",
    "UF",
    "Referência",
    "Total de famílias em situação de rua inscritas no Cadastro Único"
]]

# Exibir os dados
st.dataframe(df)

# Filtro por estado (UF)
estado = st.selectbox("Selecione o estado (UF):", df["UF"].unique())
df_filtrado = df[df["UF"] == estado]

# Exibir dados filtrados
st.subheader(f"Dados para o estado: {estado}")
st.dataframe(df_filtrado)