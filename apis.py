import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="🎬 Quiz Netflix com Imagens", layout="centered")

st.title("🎬 Quiz Netflix com Imagens")
st.write("Teste seus conhecimentos sobre séries e filmes da Netflix! Olhe a imagem e responda.")

# Perguntas do quiz com imagens
perguntas = [
    {
        "pergunta": "Qual série da Netflix é essa imagem?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Stranger_Things_logo.svg",
        "alternativas": ["Dark", "Stranger Things", "Black Mirror", "The OA"],
        "resposta_certa": "Stranger Things"
    },
    {
        "pergunta": "Qual série é mostrada nesta imagem?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/The_Witcher_logo.svg",
        "alternativas": ["Vikings", "The Witcher", "Game of Thrones", "Castlevania"],
        "resposta_certa": "The Witcher"
    },
    {
        "pergunta": "Qual é essa série?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Black_Mirror_logo.svg",
        "alternativas": ["Love, Death & Robots", "Black Mirror", "Westworld", "Black Summer"],
        "resposta_certa": "Black Mirror"
    },
    {
        "pergunta": "Que série é essa?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/La_Casa_de_Papel_logo.svg",
        "alternativas": ["Elite", "Money Heist (La Casa de Papel)", "Narcos", "Sky Rojo"],
        "resposta_certa": "Money Heist (La Casa de Papel)"
    },
    {
        "pergunta": "E esta, qual é?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Squid_Game_logo.svg",
        "alternativas": ["Alice in Borderland", "Squid Game", "Lupin", "1899"],
        "resposta_certa": "Squid Game"
    },
    {
        "pergunta": "Essa imagem representa qual série?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/4/43/The_Queen%27s_Gambit_logo.svg",
        "alternativas": ["House of Cards", "The Queen's Gambit", "Designated Survivor", "Ozark"],
        "resposta_certa": "The Queen's Gambit"
    },
    {
        "pergunta": "Que série é esta?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Bridgerton_logo.svg",
        "alternativas": ["Outlander", "Bridgerton", "The Crown", "Downton Abbey"],
        "resposta_certa": "Bridgerton"
    },
    {
        "pergunta": "Qual é essa série/mídia?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/The_Witcher_series_logo.svg/1280px-The_Witcher_series_logo.svg.png",
        "alternativas": ["The Witcher", "The Mandalorian", "Lord of the Rings", "Cursed"],
        "resposta_certa": "The Witcher"
    },
    {
        "pergunta": "Essa imagem é de qual título?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Stranger_Things_Season_3_2019.jpg",
        "alternativas": ["Lost in Space", "Stranger Things", "Dark", "Locke & Key"],
        "resposta_certa": "Stranger Things"
    },
    {
        "pergunta": "Última – essa imagem representa qual série/filme?",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/7/79/La_Casa_de_Papel_season_5_poster.jpg",
        "alternativas": ["La Casa de Papel", "Elite", "Money Heist", "Sky Rojo"],
        "resposta_certa": "La Casa de Papel"
    },
]

# Estado para o quiz
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
    st.session_state.pontuacao = 0
    st.session_state.mostrando_resposta = False

etapa = st.session_state.etapa
pontuacao = st.session_state.pontuacao
mostrando_resposta = st.session_state.mostrando_resposta

# Se acabar todas perguntas
if etapa >= len(perguntas):
    st.success(f"🏁 Fim do Quiz! Sua pontuação final: {pontuacao} de {len(perguntas)}")
    if st.button("🔁 Recomeçar"):
        st.session_state.etapa = 0
        st.session_state.pontuacao = 0
        st.session_state.mostrando_resposta = False
    st.stop()

# Pergunta atual
pergunta_atual = perguntas[etapa]
st.subheader(f"Pergunta {etapa + 1} de {len(perguntas)}")
st.write(pergunta_atual["pergunta"])

# Mostrar imagem da pergunta
response = requests.get(pergunta_atual["imagem_url"])
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="", use_container_width=True)

# Alternativas
resposta_escolhida = st.radio("Escolha uma opção:", pergunta_atual["alternativas"], key=f"pergunta_{etapa}")

# Botão de confirmar
if st.button("Confirmar resposta"):
    st.session_state.mostrando_resposta = True
    if resposta_escolhida == pergunta_atual["resposta_certa"]:
        st.success("✅ Resposta correta!")
        st.session_state.pontuacao += 1
    else:
        st.error(f"❌ Resposta errada! A resposta correta era: **{pergunta_atual['resposta_certa']}**")

# Próxima pergunta
if mostrando_resposta:
    if st.button("Próxima"):
        st.session_state.etapa += 1
        st.session_state.mostrando_resposta = False
        st.experimental_rerun()
