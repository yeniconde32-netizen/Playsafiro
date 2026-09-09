import streamlit as st
import random
from gtts import gTTS
import os
import tempfile

st.set_page_config(page_title="Emisora Falsa - El Show del Locutor", page_icon="🎙️", layout="centered")

# --- ESTILOS Y CABECERA ---
st.title("🎙️ Radio Falsa: El Show de la Mañana")
st.markdown("### Música propia, locutor con voz real, chistes y llamadas simuladas")

# --- ESTADOS DE LA SESIÓN ---
if "track_index" not in st.session_state:
    st.session_state.track_index = 0
if "locutor_texto" not in st.session_state:
    st.session_state.locutor_texto = "¡Bienvenidos a la mejor emisora de la web! Arrancamos con toda la energía."

# --- CHISTES DEL LOCUTOR ---
chistes_locutor = [
    "¡Jajaja! Oigan, ¿saben por qué los pájaros vuelven al sur en invierno? ¡Porque caminando se demoran mucho!",
    "Un saludo para todos los que nos sintonizan... ¡Recuerden que el que ríe último, piensa más lento!",
    "Ey, ey, ey, seguimos con más música en la emisora. Si su jefe les pregunta por qué están sonriendo tanto, díganle que es culpa de nuestra programación.",
    "Atención en cabina: me pasaron un chiste malo... ¿Qué hace una abeja en el gimnasio? ¡Zumba!"
]

# --- FUNCION PARA GENERAR VOZ REAL (TTS) ---
def hablar_locutor(texto):
    try:
        tts = gTTS(text=texto, lang='es', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        return None

# --- GESTION DE PLAYLIST (Música propia o por defecto) ---
playlist_default = [
    {"title": "Música de Prueba #1", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
    {"title": "Música de Prueba #2", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"}
]

# Pestañas de la App
tab_cabina, tab_bromas, tab_config = st.tabs(["📻 Cabina Principal", "📞 Sección de Llamadas y Bromas", "⚙️ Subir Mis Canciones"])

with tab_config:
    st.subheader("Sube tu propia música")
    st.markdown("Carga tus archivos MP3 desde tu celular para que suenen en la emisora.")
    uploaded_files = st.file_uploader("Sube tus archivos MP3", type=["mp3"], accept_multiple_files=True)
    if uploaded_files:
        st.session_state["custom_playlist"] = uploaded_files
        st.success(f"¡Se han cargado {len(uploaded_files)} canciones nuevas a la emisora!")

# Definir la lista activa (si subió canciones, usa esas; si no, usa las de prueba)
if "custom_playlist" in st.session_state and st.session_state["custom_playlist"]:
    playlist_activa = st.session_state["custom_playlist"]
    is_custom = True
else:
    playlist_activa = playlist_default
    is_custom = False

# Ajustar índice si es necesario
if st.session_state.track_index >= len(playlist_activa):
    st.session_state.track_index = 0

current_track = playlist_activa[st.session_state.track_index]
if is_custom:
    track_title = current_track.name
    track_source = current_track
else:
    track_title = current_track["title"]
    track_source = current_track["url"]

with tab_cabina:
    # Reproductor de voz del Locutor (Hablando en vivo)
    st.info(f"🗣️ **Locutor al aire:** *\"{st.session_state.locutor_texto}\"*")
    audio_locutor_path = hablar_locutor(st.session_state.locutor_texto)
    if audio_locutor_path:
        st.audio(audio_locutor_path, format="audio/mp3", autoplay=True)

    st.markdown("---")
    
    # Reproductor de la canción actual
    st.success(f"🔴 **EN AIRE (Música):** {track_title}")
    st.audio(track_source, format="audio/mp3")
    
    # Controles de la cabina
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⏮️ Anterior"):
            st.session_state.track_index = (st.session_state.track_index - 1) % len(playlist_activa)
            st.session_state.locutor_texto = "Cambiando de rola, ¡subanle el volumen!"
            st.rerun()
    with col2:
        if st.button("🎲 Chiste del Locutor"):
            st.session_state.locutor_texto = random.choice(chistes_locutor)
            st.rerun()
    with col3:
        if st.button("⏭️ Siguiente"):
            st.session_state.track_index = (st.session_state.track_index + 1) % len(playlist_activa)
            st.session_state.locutor_texto = "¡Seguimos con más música exclusiva en la emisora!"
            st.rerun()

with tab_bromas:
    st.subheader("📞 Línea de Bromas Telefónicas")
    st.markdown("Simula llamadas de oyentes o efectos al aire.")
    if st.button("🚨 ¡Entrar Llamada Falsa al Aire!"):
        st.success("¡Llamada entrante conectada en vivo con el oyente!")
        st.balloons()
