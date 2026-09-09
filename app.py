import streamlit as st
import random
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Emisora Falsa - El Show del Sabor Cubano", page_icon="🇨🇺", layout="centered")

# --- CABECERA DE LA EMISORA ---
st.title("🎙️ Radio El Solar: ¡Sabor y Broma en Vivo!")
st.markdown("### Transmitiendo con el tumbao' y las mejores ocurrencias")

# --- ESTADOS DE LA SESIÓN ---
if "track_index" not in st.session_state:
    st.session_state.track_index = 0
if "locutor_texto" not in st.session_state:
    st.session_state.locutor_texto = "¡Asere, qué bolá! Bienvenidos a la emisora más pegá' de todo el dial. ¡Súbele el volumen a esa bocina!"

# --- FRASES Y CHISTES CON ACENTO / MODISMO CARIBEÑO ---
chistes_locutor = [
    "¡Oye mi hermano! ¿Saben por qué los peces no hablan en el agua? ¡Porque con tanta humedad se les ahoga la voz, asere!",
    "Atención mi gente linda... Me dice el operador que el que se duerma hoy, ronca de último en la cola del pan.",
    "¡Ño! Qué calor hace en la cabina hoy... ¡Estoy más sofocado que una olla presión sin válvula!",
    "¡Sueltate ese pasito, mi amor! Recuerda que la vida es corta, pero las penas de amor duran dos discos LP."
]

# --- ANUNCIOS COMERCIALES FALSOS ---
anuncios_falsos = [
    "📢 *[ANUNCIO]* ¿Se te rompió el alma y los zapatos? ¡Llega **Pegamento 'El Milagro'**! Tan fuerte que si se lo pegas a tu ex, no se va nunca más de tu casa. ¡Búscalo ya!",
    "📢 *[ANUNCIO]* ¿Cansado de que el bus te deje botado? Cómprate ya los nuevos **Championes Voladores 'San Lázaro'**... ¡Llega tarde al trabajo, pero llega con estilo!",
    "📢 *[ANUNCIO]* ¿Hambre a las tres de la mañana? Visita **'El Rincón del Tocino Feliz'**, donde la grasa es gratis y los colesterol vienen con diploma de honor."
]

# --- LLAMADAS FALSAS DE OYENTES ---
llamadas_oyentes = [
    {"oyente": "Comemierda de Alamar", "dialogo": "¡Alo, radio! Mire, llamo para saludar a mi abuela y pa' decirles que el agua por mi cuadra no llega ni milagrosamente."},
    {"oyente": "La tina de Cienfuegos", "dialogo": "¡Oigan, qué programazo tienen! Pero por favor pongan salsa brava y dejen de hablar tanto que me duele la cabeza."},
    {"oyente": "El Pana de Lawton", "dialogo": "¡Asere, saludos a toda la clica de Lawton! Y al jefe mío que está viendo esto, ¡renuncio, caballero, renuncio!"}
]

# --- FUNCION DE VOZ DEL LOCUTOR ---
def hablar_locutor(texto):
    try:
        # Usamos acento en español (es) con textos de jerga para simular el personaje
        tts = gTTS(text=texto, lang='es', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        return None

# --- PLAYLIST DE MÚSICA ---
playlist_default = [
    {"title": "Salsa / Ritmo Callejero #1", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
    {"title": "Reparto / Dembow Urbano #2", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
    {"title": "Bolero / Vacilón #3", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"}
]

# --- PESTAÑAS PRINCIPALES ---
tab_cabina, tab_anuncios, tab_llamadas, tab_config = st.tabs(["📻 Cabina", "📢 Comerciales", "📞 Llamadas", "⚙️ Mi Música"])

with tab_config:
    st.subheader("Carga tu música propia")
    st.markdown("Sube tus archivos MP3 desde el celular para que suenen al aire en la emisora.")
    uploaded_files = st.file_uploader("Sube tus rolas", type=["mp3"], accept_multiple_files=True)
    if uploaded_files:
        st.session_state["custom_playlist"] = uploaded_files
        st.success(f"¡Se han cargado {len(uploaded_files)} canciones tuyas al sistema!")

# Seleccionar lista de reproducción activa
if "custom_playlist" in st.session_state and st.session_state["custom_playlist"]:
    playlist_activa = st.session_state["custom_playlist"]
    is_custom = True
else:
    playlist_activa = playlist_default
    is_custom = False

if st.session_state.track_index >= len(playlist_activa):
    st.session_state.track_index = 0

current_track = playlist_activa[st.session_state.track_index]
track_title = current_track.name if is_custom else current_track["title"]
track_source = current_track if is_custom else current_track["url"]

with tab_cabina:
    # Locutor hablando en vivo
    st.info(f"🗣️ **Locutor Cubano:** *\"{st.session_state.locutor_texto}\"*")
    audio_path = hablar_locutor(st.session_state.locutor_texto)
    if audio_path:
        st.audio(audio_path, format="audio/mp3", autoplay=True)

    st.markdown("---")
    
    # Canción al aire
    st.success(f"🔴 **EN AIRE (Música):** {track_title}")
    st.audio(track_source, format="audio/mp3")
    
    # Botones de control de cabina
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⏮️ Anterior"):
            st.session_state.track_index = (st.session_state.track_index - 1) % len(playlist_activa)
            st.session_state.locutor_texto = "¡Vámonos con otro tema pesao', mi gente!"
            st.rerun()
    with col2:
        if st.button("🎲 Chiste / Ocurrencia"):
            st.session_state.locutor_texto = random.choice(chistes_locutor)
            st.rerun()
    with col3:
        if st.button("⏭️ Siguiente"):
            st.session_state.track_index = (st.session_state.track_index + 1) % len(playlist_activa)
            st.session_state.locutor_texto = "¡Esto no para, caballero! Seguimos sonando duro."
            st.rerun()

with tab_anuncios:
    st.subheader("📢 Pausa Comercial Falsa")
    st.markdown("Activa un patrocinio falso en vivo para vacilar a la audiencia.")
    if st.button("📻 Lanzar Anuncio Comercial al Aire"):
        anuncio_elegido = random.choice(anuncios_falsos)
        st.session_state.locutor_texto = anuncio_elegido
        st.rerun()

with tab_llamadas:
    st.subheader("📞 Línea Caliente de Oyentes")
    st.markdown("Conecta llamadas falsas de la calle con personajes cómicos.")
    for l in llamadas_oyentes:
        if st.button(f"📞 Entrar llamada de: {l['oyente']}"):
            st.session_state.locutor_texto = f"¡Tenemos llamada en directo! Adelante {l['oyente']}: {l['dialogo']}"
            st.rerun()
