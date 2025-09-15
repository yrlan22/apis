import streamlit as st
from PIL import Image

st.title("🎬 Visualizador de Conversas - Netflix Fake API")
st.write("""
Esta aplicação simula o consumo de uma API que retorna conversas e comentários sobre séries e filmes da Netflix.
""")

# Caminho da imagem carregada
imagem_path = "/mnt/data/9de0834d-6ca0-490d-8d78-9b3c84de3f65.png"

# Exibir a imagem carregada
img = Image.open(imagem_path)
st.image(img, caption="Imagem carregada", use_column_width=True)

# Dados fake em português com mais filmes e séries
data = {
    "conversas": [
        {
            "titulo": "Stranger Things",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Stranger_Things_logo.svg",
            "comentarios": [
                {"usuario": "self", "texto": "A terceira temporada foi incrível!"},
                {"usuario": "Ana", "texto": "A ambientação dos anos 80 é perfeita."},
                {"usuario": "self", "texto": "E aquele final surpreendente!"},
            ]
        },
        {
            "titulo": "The Witcher",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/The_Witcher_logo.svg/1280px-The_Witcher_logo.svg.png",
            "comentarios": [
                {"usuario": "self", "texto": "A história do Geralt é muito envolvente."},
                {"usuario": "Carlos", "texto": "Quero ver mais monstros diferentes na próxima temporada."},
                {"usuario": "self", "texto": "A atuação do Henry Cavill é espetacular!"},
            ]
        },
        {
            "titulo": "Black Mirror",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Black_Mirror_logo.svg",
            "comentarios": [
                {"usuario": "self", "texto": "Cada episódio é uma nova história, adoro isso."},
                {"usuario": "Paula", "texto": "Alguns episódios são bem assustadores."},
                {"usuario": "self", "texto": "Mas fazem a gente refletir bastante."},
            ]
        },
        {
            "titulo": "La Casa de Papel",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/e/e1/La_Casa_de_Papel_logo.svg",
            "comentarios": [
                {"usuario": "self", "texto": "A estratégia do Professor é genial!"},
                {"usuario": "Lucas", "texto": "Não consigo parar de assistir, muito viciante."},
                {"usuario": "self", "texto": "A quarta temporada teve muitas reviravoltas."},
            ]
        },
        {
            "titulo": "Bridgerton",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Bridgerton_logo.svg",
            "comentarios": [
                {"usuario": "self", "texto": "O figurino é simplesmente maravilhoso."},
                {"usuario": "Mariana", "texto": "A trama é cheia de romance e mistérios."},
                {"usuario": "self", "texto": "Mal posso esperar pela próxima temporada."},
            ]
        },
        {
            "titulo": "O Gambito da Rainha",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/4/43/The_Queen%27s_Gambit_logo.svg",
            "comentarios": [
                {"usuario": "self", "texto": "A personagem principal é inspiradora."},
                {"usuario": "Pedro", "texto": "A ambientação e o enredo são incríveis."},
                {"usuario": "self", "texto": "Assistiria várias vezes!"},
            ]
        },
        {
            "titulo": "Round 6",
            "imagem": "https://upload.wikimedia.org/wikipedia/commons/4/42/Squid_Game_logo.svg",
            "comentarios": [
                {"usuario": "self", "texto": "A série coreana que conquistou o mundo."},
                {"usuario": "Fernanda", "texto": "Muito intensa e cheia de suspense."},
                {"usuario": "self", "texto": "Impossível parar de assistir!"},
            ]
        }
    ]
}

# Lista dos títulos
titulos = [conversa["titulo"] for conversa in data["conversas"]]

# Selectbox para escolher o título
titulo_escolhido = st.selectbox("Escolha uma série ou filme para ver os comentários:", titulos)

# Selecionar a conversa referente ao título escolhido
conversa_selecionada = next(c for c in data["conversas"] if c["titulo"] == titulo_escolhido)

# Exibir a imagem do filme/série
st.image(conversa_selecionada["imagem"], width=400)

st.subheader(f"💬 Conversa sobre {titulo_escolhido}")

# Exibir os comentários
for comentario in conversa_selecionada["comentarios"]:
    usuario = "Você" if comentario["usuario"] == "self" else comentario["usuario"]
    st.markdown(f"**{usuario}**: {comentario['texto']}")
