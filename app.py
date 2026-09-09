import streamlit as st
import random
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="ZafiroX - Recompensas y Juegos",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS profesionales idénticos a apps de recompensas móviles
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.2rem;
        width: 100%;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }
    .stButton>button:hover {
        opacity: 0.9;
    }
    .card-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 18px;
        border-radius: 16px;
        margin-bottom: 16px;
        backdrop-filter: blur(10px);
    }
    .metric-title { font-size: 14px; color: #94a3b8; }
    .metric-value { font-size: 24px; font-weight: bold; color: #f8fafc; }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Inicializar Estado de Sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = "Frite"
if "coins" not in st.session_state:
    st.session_state.coins = 11626
if "usd_balance" not in st.session_state:
    st.session_state.usd_balance = 5.00
if "gems" not in st.session_state:
    st.session_state.gems = 0
if "tokens" not in st.session_state:
    st.session_state.tokens = 3
if "history" not in st.session_state:
    st.session_state.history = []

# Estados para los minijuegos reales
if "word_secret" not in st.session_state:
    st.session_state.word_secret = random.choice(["ZAFIRO", "PYTHON", "STREAMLIT", "NEQUI", "GANAR"])
if "merge_grid" not in st.session_state:
    st.session_state.merge_grid = [2, 2, 4, 8]
if "water_tubes" not in st.session_state:
    st.session_state.water_tubes = {"Tubo 1": ["Azul", "Rojo"], "Tubo 2": ["Rojo", "Azul"]}

# Autenticación Simulada si no ha iniciado sesión
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>💎 ZafiroX</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>¡Juega, gana y retira al instante a Nequi y Daviplata!</p>", unsafe_allow_html=True)
    
    tab_log1, tab_log2 = st.tabs(["Iniciar Sesión", "Registrarse"])
    
    with tab_log1:
        u_input = st.text_input("Usuario o Correo", key="login_u")
        p_input = st.text_input("Contraseña", type="password", key="login_p")
        if st.button("Entrar a ZafiroX"):
            if u_input:
                st.session_state.username = u_input
            st.session_state.logged_in = True
            st.rerun()
            
    with tab_log2:
        reg_u = st.text_input("Crea tu Usuario", key="reg_u")
        reg_p = st.text_input("Contraseña", type="password", key="reg_p")
        if st.button("Registrarse y Ganar $5 USD"):
            st.session_state.username = reg_u if reg_u else "JugadorZafiro"
            st.session_state.usd_balance = 5.00
            st.session_state.logged_in = True
            st.success("¡Cuenta creada con éxito! Bono de $5.00 USD acreditado.")
            st.rerun()
            
    st.stop()

# Barra Superior de Usuario Estilo App
col_u1, col_u2 = st.columns([2, 1])
with col_u1:
    st.markdown(f"### 👋 Hola, **{st.session_state.username}**")
with col_u2:
    st.markdown(f"<div style='text-align: right; color: #38bdf8; font-weight: bold;'>${st.session_state.usd_balance:.2f} USD</div>", unsafe_allow_html=True)

st.markdown("---")

# Navegación con pestañas
menu_tabs = st.tabs(["🏠 Inicio & Juegos", "⚔️ Desafíos", "🎡 Carrusel", "📢 Eventos", "🔥 Premios", "💰 Billetera"])

# ----------------- 🏠 INICIO & JUEGOS REALES -----------------
with menu_tabs[0]:
    st.markdown("### 🏆 Conversión de Monedas")
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<span class='metric-title'>Surge Coins</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='metric-value'>{st.session_state.coins:,}</span>", unsafe_allow_html=True)
    with col2:
        st.markdown("<span class='metric-title'>Equivalente USD</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='metric-value'>${st.session_state.coins / 232500:.2f}</span>", unsafe_allow_html=True)
    
    if st.button("¡Cobrar y Convertir Monedas!"):
        earned = st.session_state.coins / 232500
        st.session_state.usd_balance += earned
        st.session_state.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Conversión +${earned:.2f} USD")
        st.session_state.coins = 0
        st.success(f"¡Has convertido tus monedas con éxito por ${earned:.2f} USD!")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🕹️ Sala de Minijuegos Interactivos")
    selected_game = st.selectbox("Elige un juego real para ganar monedas:", ["Word Kitchen (Adivina Palabra)", "Merge Blast (Combinar Bloques)", "Water Sorter (Clasificar Colores)", "Nailed It! (Precisión al Clavar)"])
    
    st.markdown("---")
    
    # 1. WORD KITCHEN REAL
    if selected_game == "Word Kitchen (Adivina Palabra)":
        st.markdown("#### 🍳 Word Kitchen")
        st.markdown(f"Pista: Palabra oculta de {len(st.session_state.word_secret)} letras relacionada con tecnología o premios.")
        user_word = st.text_input("Ingresa tu palabra en Mayúsculas:", key="word_guess").upper()
        if st.button("Probar Palabra"):
            if user_word == st.session_state.word_secret:
                reward = 800
                st.session_state.coins += reward
                st.success(f"🎉 ¡Correcto! Ganaste +{reward} monedas.")
                st.session_state.word_secret = random.choice(["ZAFIRO", "PYTHON", "STREAMLIT", "NEQUI", "GANAR"])
                st.session_state.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Word Kitchen (Win) +{reward}")
                st.rerun()
            else:
                st.error("❌ Palabra incorrecta. ¡Inténtalo de nuevo!")

    # 2. MERGE BLAST REAL
    elif selected_game == "Merge Blast (Combinar Bloques)":
        st.markdown("#### 🧩 Merge Blast")
        st.markdown("Combina fichas iguales sumando bloques adyacentes para evolucionar.")
        st.write("Tablero actual:", st.session_state.merge_grid)
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            if st.button("Hacer Merge (Combinar 2+2)"):
                st.session_state.merge_grid = [4, 4, 8, 16]
                st.session_state.coins += 500
                st.success("¡Merge exitoso! +500 monedas.")
                st.rerun()
        with col_m2:
            if st.button("Reiniciar Tablero"):
                st.session_state.merge_grid = [2, 2, 4, 8]
                st.rerun()

    # 3. WATER SORTER REAL
    elif selected_game == "Water Sorter (Clasificar Colores)":
        st.markdown("#### 🧪 Water Sorter Puzzle")
        st.markdown("Organiza los líquidos para completar el tubo.")
        st.write(st.session_state.water_tubes)
        if st.button("Trasvasar Líquido"):
            st.session_state.water_tubes["Tubo 1"] = ["Azul", "Azul"]
            st.session_state.water_tubes["Tubo 2"] = ["Rojo", "Rojo"]
            st.session_state.coins += 600
            st.success("¡Puzzle completado con éxito! +600 monedas.")
            st.rerun()

    # 4. NAILED IT! REAL
    elif selected_game == "Nailed It! (Precisión al Clavar)":
        st.markdown("#### 🔨 Nailed It!")
        st.markdown("Detén el golpe en el momento justo de precisión.")
        force = st.slider("Fuerza de impacto", 1, 100, 50)
        if st.button("¡Clavar Clavo!"):
            if 45 <= force <= 55:
                st.session_state.coins += 1000
                st.success(f"🎯 ¡Impacto perfecto con fuerza {force}! +1,000 monedas.")
            else:
                st.session_state.coins += 200
                st.warning(f"🔨 Golpe débil o pasado (Fuerza {force}). Ganaste solo +200 monedas.")
            st.rerun()

# ----------------- ⚔️ DESAFÍOS -----------------
with menu_tabs[1]:
    st.markdown("### 🎯 Desafíos Activos")
    st.markdown("<div class='card-box'><b>Desafío Diario:</b> Gana al menos 2 partidas en los minijuegos interactivos.<br><br><b>Progreso:</b> 1/2</div>", unsafe_allow_html=True)
    if st.button("Completar Misión Diaria"):
        st.session_state.coins += 1500
        st.session_state.gems += 75
        st.success("¡Misión cumplida! +1,500 monedas y +75 Gems.")
        st.rerun()

# ----------------- 🎡 CARRUSEL -----------------
with menu_tabs[2]:
    st.markdown("### 🎡 Ruleta de Premios ZafiroX")
    st.markdown(f"<div class='card-box'><b>Tokens Disponibles:</b> {st.session_state.tokens} 🪙</div>", unsafe_allow_html=True)
    if st.button("Girar Ruleta"):
        if st.session_state.tokens > 0:
            st.session_state.tokens -= 1
            premio = random.choice([500, 1000, 5000, 10000, 50000])
            st.session_state.coins += premio
            st.success(f"🎁 ¡Felicidades! Ganaste {premio:,} monedas en la ruleta.")
            st.rerun()
        else:
            st.error("No tienes tokens. Completa desafíos para ganar más tokens.")

# ----------------- 📢 EVENTOS -----------------
with menu_tabs[3]:
    st.markdown("### 🎒 Weekly Pot - $1,000 en Premios")
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown(f"**Gems recolectados:** {st.session_state.gems}/350")
    st.progress(min(st.session_state.gems / 350, 1.0))
    st.markdown("<br>¡Participa en el evento semanal completando minijuegos!")
    if st.button("Reclamar Bonus de Gems (+50 Gems)"):
        st.session_state.gems += 50
        st.success("¡Bonus reclamado! +50 Gems agregados.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- 🔥 PREMIOS -----------------
with menu_tabs[4]:
    st.markdown("### 🔥 Recompensa de Racha Diaria")
    st.markdown("<div class='card-box'><b>Día 2 - Reclama tu bono</b><br>Mantén tu racha activa ingresando todos los días.</div>", unsafe_allow_html=True)
    if st.button("Reclamar Bono Diario"):
        st.session_state.coins += 2500
        st.success("¡Bono diario reclamado con éxito! +2,500 monedas.")
        st.rerun()

# ----------------- 💰 BILLETERA -----------------
with menu_tabs[5]:
    st.markdown("### 🏦 Retiro Inmediato Colombia")
    cop_total = st.session_state.usd_balance * 4000
    st.markdown(f"<div class='card-box'><b>Saldo Disponible:</b> ${st.session_state.usd_balance:.2f} USD (~${cop_total:,.0f} COP)</div>", unsafe_allow_html=True)
    
    metodo = st.selectbox("Método de Retiro", ["Nequi", "Daviplata", "PSE", "PayPal"])
    destino = st.text_input("Número de celular / Cuenta / Correo", placeholder="Ej: 3185312231")
    monto_retiro = st.number_input("Monto a retirar en USD", min_value=1.0, max_value=max(1.0, st.session_state.usd_balance), value=st.session_state.usd_balance)
    
    cop_valor = monto_retiro * 4000
    st.info(f"Monto a recibir en tu {metodo}: **${cop_valor:,.0f} COP**")
    
    if st.button("🚀 Confirmar Solicitud de Retiro"):
        if st.session_state.usd_balance >= monto_retiro:
            st.session_state.usd_balance -= monto_retiro
            st.session_state.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Retiro {metodo} ({destino}) -${monto_retiro:.2f} USD")
            st.success(f"¡Retiro de ${cop_valor:,.0f} COP procesado con éxito a tu cuenta de {metodo}!")
        else:
            st.error("Saldo insuficiente para realizar el retiro.")

    st.markdown("### 📋 Historial de Transacciones")
    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.markdown(f"- {item}")
    else:
        st.markdown("No hay transacciones recientes.")
