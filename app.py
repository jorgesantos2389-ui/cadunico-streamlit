import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Exibir os dados completos
st.dataframe(df)

# Filtro por estado (UF)
estado = st.selectbox("Selecione o estado (UF):", df["UF"].unique())
df_estado = df[df["UF"] == estado]

# Filtro por municípios (Unidade Territorial) dentro do estado selecionado
municipios = st.multiselect(
    "Selecione os municípios:",
    options=df_estado["Unidade Territorial"].unique(),
    default=df_estado["Unidade Territorial"].unique()
)

# Aplicar filtro de municípios
df_filtrado = df_estado[df_estado["Unidade Territorial"].isin(municipios)]

# Exibir dados filtrados
st.subheader(f"Dados para o estado: {estado} e municípios selecionados")
st.dataframe(df_filtrado)

# Escolha do tipo de gráfico
tipo_grafico = st.radio(
    "Escolha o tipo de gráfico:",
    ("Barras", "Pizza")
)

# Gerar gráfico conforme escolha
if not df_filtrado.empty:
    if tipo_grafico == "Barras":
        fig, ax = plt.subplots()
        ax.bar(df_filtrado["Unidade Territorial"],
               df_filtrado["Total de famílias em situação de rua inscritas no Cadastro Único"],
               color="skyblue")
        ax.set_ylabel("Total de famílias")
        ax.set_xlabel("Unidade Territorial")
        ax.set_title(f"Gráfico de Barras - {estado}")
        st.pyplot(fig)

    elif tipo_grafico == "Pizza":
        fig, ax = plt.subplots()
        ax.pie(df_filtrado["Total de famílias em situação de rua inscritas no Cadastro Único"],
               labels=df_filtrado["Unidade Territorial"],
               autopct="%1.1f%%",
               startangle=90)
        ax.set_title(f"Gráfico de Pizza - {estado}")
        st.pyplot(fig)
else:
    st.warning("Nenhum dado disponível para os municípios selecionados.")