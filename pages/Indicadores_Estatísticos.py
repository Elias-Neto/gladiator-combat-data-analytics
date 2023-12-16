# Importe as bibliotecas necessárias
import pandas as pd
import streamlit as st

# Configurações de título e ícones
st.set_page_config(page_title="Indicadores Estatísticos", page_icon="📊")

# Função para carregar os dados da base de dados
@st.cache_data
def load_data():
    data = pd.read_csv('gladiator_data3.csv')
    return data

# Carregue os dados
data = load_data()

# Seção para filtros
st.sidebar.header("Filtros")

# Adicione filtros para Age, Origin, Category, Special Skills, Weapon of Choice
selected_age = st.sidebar.slider("Selecione a Idade:", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))
selected_origin = st.sidebar.selectbox("Selecione a Origem:", ["Todos"] + list(data['Origin'].unique()))
selected_category = st.sidebar.selectbox("Selecione a Categoria:", ["Todos"] + list(data['Category'].unique()))
selected_skills = st.sidebar.selectbox("Selecione as Habilidades Especiais:", ["Todos"] + list(data['Special Skills'].unique()))
selected_weapon = st.sidebar.selectbox("Selecione a Arma de Escolha:", ["Todos"] + list(data['Weapon of Choice'].unique()))

# Aplique os filtros
filtered_data = data[
    (data['Age'] >= selected_age[0]) & (data['Age'] <= selected_age[1]) &
    ((data['Origin'] == selected_origin) | (selected_origin == "Todos")) &
    ((data['Category'] == selected_category) | (selected_category == "Todos")) &
    ((data['Special Skills'] == selected_skills) | (selected_skills == "Todos")) &
    ((data['Weapon of Choice'] == selected_weapon) | (selected_weapon == "Todos"))
]

# Título da página
st.title("Indicadores Estatísticos Gerais da Base de Dados")

# Total de combates
total_combats = filtered_data['Wins'].sum() + filtered_data['Losses'].sum()

# Porcentagem de vitória
win_percentage = (filtered_data['Wins'].sum() / total_combats) * 100

# Média de Vitórias por Combate
avg_wins_per_combat = filtered_data['Wins'].mean()

# Média de Idade dos Gladiadores
avg_age = filtered_data['Age'].mean()

# Porcentagem de Gladiadores que Sobreviveram
survival_percentage = (filtered_data['Survived'].sum() / len(filtered_data)) * 100

# Média de Peso dos Gladiadores
avg_weight = filtered_data['Weight'].mean()

# Média de Altura dos Gladiadores
avg_height = filtered_data['Height'].mean()

# Média de Experiência em Combate
avg_battle_experience = filtered_data['Battle Experience'].mean()

# Maior Número de Vitórias
max_wins = filtered_data['Wins'].max()

# Maior Número de Derrotas
max_losses = filtered_data['Losses'].max()

# Média de Popularidade (Public Favor)
avg_public_favor = filtered_data['Public Favor'].mean()

# Média de Resiliência Mental (Mental Resilience)
avg_mental_resilience = filtered_data['Mental Resilience'].mean()

# Categoria mais Vitoriosa
most_victorious_category = filtered_data['Category'].mode().values[0]

# Armas Escolhida mais Vitoriosa
most_victorious_weapon = filtered_data['Weapon of Choice'].mode().values[0]

# Estratégia de Batalha mais Vitoriosa
most_victorious_strategy = filtered_data['Battle Strategy'].mode().values[0]

# Crie a tabela com os indicadores estatísticos
tabela_estatisticas = pd.DataFrame({
    'Indicador Estatístico': [
        "Total de Combates", "Porcentagem de Vitória", "Média de Vitórias por Combate", "Média de Idade dos Gladiadores", "Porcentagem de Gladiadores que Sobreviveram",
        "Média de Peso dos Gladiadores", "Média de Altura dos Gladiadores", "Média de Experiência em Combate", "Maior Número de Vitórias", "Maior Número de Derrotas",
        "Média de Popularidade", "Média de Resiliência Mental", "Categoria mais Vitoriosa", "Armas Escolhida mais Vitoriosa", "Estratégia de Batalha mais Vitoriosa"
    ],
    'Valor': [
        total_combats, f"{win_percentage:.2f}%", f"{avg_wins_per_combat:.2f}", f"{avg_age:.2f} anos", f"{survival_percentage:.2f}%",
        f"{avg_weight:.2f} kg", f"{avg_height:.2f} cm", f"{avg_battle_experience:.2f}", max_wins, max_losses,
        f"{avg_public_favor:.2f}", f"{avg_mental_resilience:.2f}", most_victorious_category, most_victorious_weapon, most_victorious_strategy
    ]
})

# Exiba a tabela
st.table(tabela_estatisticas)
