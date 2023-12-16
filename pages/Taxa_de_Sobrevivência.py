# Importe as bibliotecas necessárias
import pandas as pd
import streamlit as st
import plotly.express as px

# Configurações de título e ícones
st.set_page_config(page_title="Taxa de Sobrevivência", page_icon="☠️")

# Função para carregar uma amostra dos dados da base de dados
@st.cache_data
def load_data():
    data = pd.read_csv('gladiator_data3.csv')
    return data

# Carregue os dados (utilizando uma amostra de 1000 linhas, por exemplo)
data = load_data()

# Seção para filtros no sidebar
st.sidebar.header("Filtros")
selected_age_survival = st.sidebar.slider("Selecione a Idade:", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))
selected_origin_survival = st.sidebar.selectbox("Selecione a Origem:", ["Todos"] + list(data['Origin'].unique()))

# Aplique os filtros
filtered_data_survival = data[
    (data['Age'] >= selected_age_survival[0]) & (data['Age'] <= selected_age_survival[1]) &
    ((data['Origin'] == selected_origin_survival) | (selected_origin_survival == "Todos"))
]

# Título da página
st.title("Taxa de Sobrevivência dos Gladiadores")

# Gráficos de coluna
fig_category_survival = px.bar(
    filtered_data_survival,
    x="Category",
    color="Survived",
    labels={"Category": "Categoria de Gladiadores", "count": "Número de Gladiadores"},
    title="Categoria x Sobrevivência"
)
st.plotly_chart(fig_category_survival)

fig_weapon_survival = px.bar(
    filtered_data_survival,
    x="Weapon of Choice",
    color="Survived",
    labels={"Weapon of Choice": "Arma de Escolha", "count": "Número de Gladiadores"},
    title="Arma de Escolha x Sobrevivência"
)
st.plotly_chart(fig_weapon_survival)

fig_combat_style_survival = px.bar(
    filtered_data_survival,
    x="Battle Strategy",
    color="Survived",
    labels={"Battle Strategy": "Estratégia de Batalha", "count": "Número de Gladiadores"},
    title="Estratégia de Batalha x Sobrevivência"
)
st.plotly_chart(fig_combat_style_survival)

fig_previous_occupation_survival = px.bar(
    filtered_data_survival,
    x="Previous Occupation",
    color="Survived",
    labels={"Previous Occupation": "Ocupação Anterior", "count": "Número de Gladiadores"},
    title="Ocupação Anterior x Sobrevivência"
)
st.plotly_chart(fig_previous_occupation_survival)
