# Importe as bibliotecas necessárias
import streamlit as st

st.set_page_config(page_title="Gladiator Data Analysis", page_icon="🏹")

st.title("Bem-vindo à Análise de Dados de Gladiadores 🛡️")

st.write(
    "Esta aplicação web oferece uma análise detalhada de gladiadores, combinando elementos históricos com potencial de análise de dados moderna."
)

image_url = "https://qph.cf2.quoracdn.net/main-qimg-cb7257da1ebcc3b14a6a6f4f85b6a257-lq"
st.image(image_url, caption="Gladiator Image", use_column_width=True)
