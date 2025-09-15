import streamlit as st

st.set_page_config(page_title="🎬 Quiz Netflix", layout="centered")

st.title("🎬 Quiz Netflix Original")
st.write("Teste seus conhecimentos sobre as séries e filmes mais populares da Netflix!")

# Perguntas do quiz
perguntas = [
    {
        "pergunta": "Qual personagem é conhecido como 'O Professor'?",
        "alternativas": ["Berlin", "Professor Xavier", "Sérgio Marquina", "Denver"],
        "resposta_certa": "Sérgio Marquina"
    },
    {
        "pergunta": "Qual dessas séries se passa no mundo invertido?",
        "alternativas": ["The Umbrella Academy", "Dark", "Stranger Things", "Black Mirror"],
        "resposta_certa": "Stranger Things"
    },
    {
        "pergunta": "Qual série mostra um jogo mortal com desafios infantis?",
        "alternativas": ["Round 6", "Breaking Bad", "You", "Lucifer"],
        "resposta_certa": "Round 6"
    },
    {
        "pergunta": "Em qual série uma jovem prodígio joga xadrez?",
        "alternativas": ["The Crown", "O Gambito da Rainha", "Bridgerton", "Sex Education"],
        "resposta_certa": "O Gambito da Rainha"
    },
    {
        "pergunta": "Quem é Geralt de Rívia?",
        "alternativas": ["Um mago", "Um vampiro", "Um bruxo caçador de monstros", "Um rei"],
        "resposta_certa": "Um bruxo caçador de monstros"
    }
]

# Sessão para armazenar estado
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
    st.session_state.pontuacao = 0
    st.session_state.mostrando_resposta = False

# Etapa atual
etapa = st.session_state.etapa
pontuacao = st.session_state.pontuacao
mostrando_resposta = st.session_state.mostrando_resposta

# Quando terminar todas as perguntas
if etapa >= len(perguntas):
    st.success(f"🏁 Fim do Quiz! Sua pontuação final: {pontuacao} de {len(perguntas)}")
    if st.button("🔁 Recomeçar"):
        st.session_state.etapa = 0
        st.session_state.pontuacao = 0
        st.session_state.mostrando_resposta = False
    st.stop()

# Mostrar pergunta atual
pergunta_atual = perguntas[etapa]
st.subheader(f"Pergunta {etapa + 1} de {len(perguntas)}")
st.write(pergunta_atual["pergunta"])

# Mostrar opções
resposta_escolhida = st.radio("Escolha uma opção:", pergunta_atual["alternativas"], key=f"pergunta_{etapa}")

# Verificar resposta
if st.button("Confirmar resposta"):
    st.session_state.mostrando_resposta = True
    if resposta_escolhida == pergunta_atual["resposta_certa"]:
        st.success("✅ Resposta correta!")
        st.session_state.pontuacao += 1
    else:
        st.error(f"❌ Resposta errada! A resposta correta era: **{pergunta_atual['resposta_certa']}**")

# Botão para próxima pergunta
if mostrando_resposta:
    if st.button("Próxima"):
        st.session_state.etapa += 1
        st.session_state.mostrando_resposta = False
        st.experimental_rerun()

