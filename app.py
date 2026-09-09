import streamlit as st
import random
import time

st.set_page_config(page_title="Emisora Falsa - El Show del Locutor", page_icon="🎙️", layout="centered")

# --- ESTILOS Y CABECERA ---
st.title("🎙️ Radio Falsa: El Show de la Mañana")
st.markdown("### Música, locutor automático, chistes y llamadas en vivo (Todo simulado)")

# --- ESTADOS DE LA SESIÓN ---
if "track_index" not in st.session_state:
    st.session_state.track_index = 0
if "locutor_mensaje" not in st.session_state:
    st.session_state.locutor_mensaje = "¡Bienvenidos a la mejor emisora! Arrancamos con toda la energía."

# --- DATOS DE LA EMISORA ---
# Aquí puedes poner los enlaces de tus canciones (puedes subirlas a GitHub, un bucket o usar archivos locales)
playlist = [
    {"title": "Mi Canción Propia #1", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
    {"title": "Mi Canción Propia #2", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
    {"title": "Rolita Exclusiva", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"}
]

# Chistes y frases del locutor falso
chistes_locutor = [
    "¡Jajaja! Oigan, ¿saben por qué los pájaros vuelven al sur en invierno? ¡Porque caminando se demoran mucho!",
    "Un saludo para todos los que nos sintonizan... ¡Recuerden que el que ríe último, piensa más lento!",
    "Ey, ey, ey, seguimos con más música en la emisora. Si su jefe les pregunta por qué están sonriendo tanto, díganle que es culpa de nuestra programación.",
    "Atención en cabina: me pasaron un chiste malo... ¿Qué hace una abeja en el gimnasio? ¡Zumba!"
]

# Bromas telefónicas simuladas (audios falsos o efectos)
bromas_telefonicas = [
    {"nombre": "Broma del plomero confundido", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "desc": "Llamando a un vecino por una fuga de agua inexistente."},
    {"nombre": "Broma de la pizza gigante que nunca pidió", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "desc": "Le caen 50 pizzas a una casa de la nada."}
]

# --- PESTAÑAS DE LA EMISORA ---
tab_cabina, tab_bromas, tab_config = st.tabs(["📻 Cabina Principal", "📞 Sección de Llamadas y Bromas", "⚙️ Subir Mis Canciones"])

with tab_cabina:
    current_track = playlist[st.session_state.track_index]
    
    # Panel de locución (El locutor falso hablando)
    st.info(f"🗣️ **Locutor (En Cabina):** *\"{st.session_state.locutor_mensaje}\"*")
    
    # Reproductor de la canción actual
    st.success(f"🔴 **EN AIRE:** {current_track['title']}")
    st.audio(current_track["url"], format="audio/mp3", autoplay=True)
    
    # Controles del DJ
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⏮️ Anterior"):
            st.session_state.track_index = (st.session_state.track_index - 1) % len(playlist)
            st.session_state.locutor_mensaje = random.choice(chistes_locutor)
            st.rerun()
    with col2:
        if st.button("🎲 Chiste / Comentario del Locutor"):
            st.session_state.locutor_mensaje = random.choice(chistes_locutor)
            st.rerun()
    with col3:
        if st.button("⏭️ Siguiente"):
            st.session_state.track_index = (st.session_state.track_index + 1) % len(playlist)
            st.session_state.locutor_mensaje = "¡Venimos con más éxitos! No se muevan de sintonía."
            st.rerun()

with tab_bromas:
    st.subheader("📞 Línea Caliente de Bromas Telefónicas")
    st.markdown("Simula llamadas de oyentes o reproduce secciones de bromas grabadas en la emisora.")
    
    broma_seleccionada = st.selectbox("Elige la broma para transmitir:", bromas_telefonicas, format_func=lambda x: x["nombre"])
    st.write(f"*{broma_seleccionada['desc']}*")
    
    # Reproductor para la broma
    st.audio(broma_seleccionada["url"], format="audio/mp3")
    
    if st.button("🚨 ¡Entrar Llamada Falsa al Aire!"):
        st.success("¡Llamada entrante conectada en vivo! El locutor está hablando con el oyente ficticio...")
        st.balloons()

with tab_config:
    st.subheader("Subir tu propia música")
    st.markdown("Puedes cargar los archivos de audio de tu celular o PC para que suenen directamente en la emisora.")
    
    uploaded_files = st.file_uploader("Sube tus archivos MP3", type=["mp3"], accept_multiple_files=True)
    if uploaded_files:
        st.success(f"¡Se han cargado {len(uploaded_files)} canciones nuevas a la memoria de la emisora!")
        for file in uploaded_files:
            st.text(f"🎵 {file.name}")
