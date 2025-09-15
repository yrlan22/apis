
import streamlit as st
import requests

# Fake endpoint de exemplo
API_URL = "https://raw.githubusercontent.com/openai-sample/fake-whatsapp-api/main/conversations.json"

st.title("💬 Visualizador de Conversas - WhatsApp Fake API")
st.write("""
Essa aplicação simula o consumo de uma API do WhatsApp, exibindo conversas recentes com contatos fictícios.
""")

# Fazendo a requisição para a API fake
try:
    response = requests.get(API_URL)
    data = response.json()
except Exception as e:
    st.error("Erro ao carregar dados da API.")
    st.stop()

# Pegar nomes dos contatos disponíveis
contatos = [conversa["contato"] for conversa in data["conversas"]]

# Selectbox para escolher contato
contato_escolhido = st.selectbox("Escolha um contato para ver a conversa:", contatos)

# Mostrar conversa do contato escolhido
conversa_selecionada = next(c for c in data["conversas"] if c["contato"] == contato_escolhido)

st.subheader(f"📱 Conversa com {contato_escolhido}")

# Exibir as mensagens como uma "tabela"
for msg in conversa_selecionada["mensagens"]:
    remetente = "Você" if msg["remetente"] == "self" else contato_escolhido
    st.markdown(f"**{remetente}**: {msg['texto']}")

