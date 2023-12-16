# Importe as bibliotecas necessárias
import pandas as pd
import streamlit as st
import plotly.express as px

# Configurações de título e ícones
st.set_page_config(page_title="Taxa de Vitórias", page_icon="🏆")

# Função para carregar uma amostra dos dados da base de dados
@st.cache_data
def load_data():
    data = pd.read_csv('gladiator_data3.csv')
    return data.sample(sample_size)

# Carregue os dados (utilizando uma amostra de 1000 linhas, por exemplo)
data = load_data()

# Seção para filtros no sidebar
st.sidebar.header("Filtros")
selected_age_victory = st.sidebar.slider("Selecione a Idade:", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))
selected_origin_victory = st.sidebar.selectbox("Selecione a Origem:", ["Todos"] + list(data['Origin'].unique()))

# Aplique os filtros
filtered_data_victory = data[
    (data['Age'] >= selected_age_victory[0]) & (data['Age'] <= selected_age_victory[1]) &
    ((data['Origin'] == selected_origin_victory) | (selected_origin_victory == "Todos"))
]

# Título da página
st.title("Taxa de Vitórias dos Gladiadores")

# Gráficos de coluna
fig_category_victory = px.bar(
    filtered_data_victory,
    x="Category",
    y=["Wins", "Losses"],
    labels={"Category": "Categoria de Gladiadores", "value": "Número de Gladiadores", "variable": "Resultado"},
    title="Categoria x Vitórias/Derrotas"
)
st.plotly_chart(fig_category_victory)

fig_weapon_victory = px.bar(
    filtered_data_victory,
    x="Weapon of Choice",
    y=["Wins", "Losses"],
    labels={"Weapon of Choice": "Arma de Escolha", "value": "Número de Gladiadores", "variable": "Resultado"},
    title="Arma de Escolha x Vitórias/Derrotas"
)
st.plotly_chart(fig_weapon_victory)

fig_combat_style_victory = px.bar(
    filtered_data_victory,
    x="Battle Strategy",
    y=["Wins", "Losses"],
    labels={"Battle Strategy": "Estratégia de Batalha", "value": "Número de Gladiadores", "variable": "Resultado"},
    title="Estratégia de Batalha x Vitórias/Derrotas"
)
st.plotly_chart(fig_combat_style_victory)

fig_previous_occupation_victory = px.bar(
    filtered_data_victory,
    x="Previous Occupation",
    y=["Wins", "Losses"],
    labels={"Previous Occupation": "Ocupação Anterior", "value": "Número de Gladiadores", "variable": "Resultado"},
    title="Ocupação Anterior x Vitórias/Derrotas"
)
st.plotly_chart(fig_previous_occupation_victory)
