
import streamlit as st

st.title("🎬 Visualizador de Conversas - Netflix Fake API")
st.write("""
Esta aplicação simula o consumo de uma API que retorna conversas e comentários sobre séries e filmes da Netflix.
""")

# Dados fake em português com mais filmes e séries
data = {
    "conversas": [
        {
            "titulo": "Stranger Things",
            "comentarios": [
                {"usuario": "self", "texto": "A terceira temporada foi incrível!"},
                {"usuario": "Ana", "texto": "A ambientação dos anos 80 é perfeita."},
                {"usuario": "self", "texto": "E aquele final surpreendente!"},
            ]
        },
        {
            "titulo": "The Witcher",
            "comentarios": [
                {"usuario": "self", "texto": "A história do Geralt é muito envolvente."},
                {"usuario": "Carlos", "texto": "Quero ver mais monstros diferentes na próxima temporada."},
                {"usuario": "self", "texto": "A atuação do Henry Cavill é espetacular!"},
            ]
        },
        {
            "titulo": "Black Mirror",
            "comentarios": [
                {"usuario": "self", "texto": "Cada episódio é uma nova história, adoro isso."},
                {"usuario": "Paula", "texto": "Alguns episódios são bem assustadores."},
                {"usuario": "self", "texto": "Mas fazem a gente refletir bastante."},
            ]
        },
        {
            "titulo": "La Casa de Papel",
            "comentarios": [
                {"usuario": "self", "texto": "A estratégia do Professor é genial!"},
                {"usuario": "Lucas", "texto": "Não consigo parar de assistir, muito viciante."},
                {"usuario": "self", "texto": "A quarta temporada teve muitas reviravoltas."},
            ]
        },
        {
            "titulo": "Bridgerton",
            "comentarios": [
                {"usuario": "self", "texto": "O figurino é simplesmente maravilhoso."},
                {"usuario": "Mariana", "texto": "A trama é cheia de romance e mistérios."},
                {"usuario": "self", "texto": "Mal posso esperar pela próxima temporada."},
            ]
        },
        {
            "titulo": "O Gambito da Rainha",
            "comentarios": [
                {"usuario": "self", "texto": "A personagem principal é inspiradora."},
                {"usuario": "Pedro", "texto": "A ambientação e o enredo são incríveis."},
                {"usuario": "self", "texto": "Assistiria várias vezes!"},
            ]
        },
        {
            "titulo": "Round 6",
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

st.subheader(f"💬 Conversa sobre {titulo_escolhido}")

# Exibir os comentários
for comentario in conversa_selecionada["comentarios"]:
    usuario = "Você" if comentario["usuario"] == "self" else comentario["usuario"]
    st.markdown(f"**{usuario}**: {comentario['texto']}")
