
import streamlit as st
import requests

# Fake endpoint com dados de séries Netflix (vou usar um JSON fake direto para exemplo)
# Se quiser pode apontar para um JSON no GitHub depois.
API_URL = "https://raw.githubusercontent.com/openai-sample/fake-netflix-api/main/conversations.json"

st.title("🎬 Visualizador de Conversas - Netflix Fake API")
st.write("""
Essa aplicação simula o consumo de uma API que retorna conversas e comentários sobre séries da Netflix.
""")

# Como não existe a API real, vamos simular os dados aqui:
# Remova esse bloco e descomente o código de requests se tiver um endpoint real
data = {
    "conversas": [
        {
            "serie": "Stranger Things",
            "comentarios": [
                {"usuario": "self", "texto": "A terceira temporada foi a melhor!"},
                {"usuario": "Ana", "texto": "Concordo, a vibe dos anos 80 é incrível."},
                {"usuario": "self", "texto": "E aquele final, chocante demais!"},
            ]
        },
        {
            "serie": "The Witcher",
            "comentarios": [
                {"usuario": "self", "texto": "A história do Geralt é muito envolvente."},
                {"usuario": "Carlos", "texto": "Quero ver mais monstros diferentes na próxima temporada."},
                {"usuario": "self", "texto": "A atuação do Henry Cavill é top!"},
            ]
        },
        {
            "serie": "Black Mirror",
            "comentarios": [
                {"usuario": "self", "texto": "Cada episódio é uma história nova, adoro isso."},
                {"usuario": "Paula", "texto": "Alguns são meio assustadores demais."},
                {"usuario": "self", "texto": "Mas fazem a gente pensar, né?"},
            ]
        }
    ]
}

# Código para pegar dados via API (descomente para usar)
# try:
#     response = requests.get(API_URL)
#     data = response.json()
# except Exception as e:
#     st.error("Erro ao carregar dados da API.")
#     st.stop()

series = [conversa["serie"] for conversa in data["conversas"]]

serie_escolhida = st.selectbox("Escolha uma série para ver os comentários:", series)

conversa_selecionada = next(c for c in data["conversas"] if c["serie"] == serie_escolhida)

st.subheader(f"💬 Conversa sobre {serie_escolhida}")

for comentario in conversa_selecionada["comentarios"]:
    usuario = "Você" if comentario["usuario"] == "self" else comentario["usuario"]
    st.markdown(f"**{usuario}**: {comentario['texto']}")
