import streamlit as st
import random
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="ZafiroX - Recompensas y Juegos Pro",
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
    st.session_state.username = "Ñopio"
if "coins" not in st.session_state:
    st.session_state.coins = 12420
if "usd_balance" not in st.session_state:
    st.session_state.usd_balance = 5.34
if "gems" not in st.session_state:
    st.session_state.gems = 15
if "tokens" not in st.session_state:
    st.session_state.tokens = 3
if "history" not in st.session_state:
    st.session_state.history = []

# Estados para los minijuegos clásicos
if "invader_score" not in st.session_state:
    st.session_state.invader_score = 0
if "solitaire_deck" not in st.session_state:
    st.session_state.solitaire_deck = ["A♠", "10♥", "K♦", "7♣", "J♠"]
if "chess_puzzle" not in st.session_state:
    st.session_state.chess_puzzle = {"problema": "Mate en 1: Dama en f7", "resuelto": False}

# Autenticación Simulada si no ha iniciado sesión
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>💎 ZafiroX Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>¡Arcades clásicos, juegos de mesa y retiros instantáneos!</p>", unsafe_allow_html=True)
    
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
            st.session_state.username = reg_u if reg_u else "Ñopio"
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

# Navegación con pestañas mejoradas
menu_tabs = st.tabs(["🏠 Billetera & Juegos", "👾 Arcade Marcianitos", "🃏 Solitario & ♟️ Ajedrez", "🎡 Carrusel", "📢 Eventos", "💰 Retiros"])

# ----------------- 🏠 INICIO & CONVERSIÓN -----------------
with menu_tabs[0]:
    st.markdown("### 🏆 Panel de Monedas y Balance")
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<span class='metric-title'>Surge Coins</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='metric-value'>{st.session_state.coins:,}</span>", unsafe_allow_html=True)
    with col2:
        st.markdown("<span class='metric-title'>Equivalente USD</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='metric-value'>${st.session_state.coins / 232500:.2f}</span>", unsafe_allow_html=True)
    
    if st.button("⚡ Convertir Monedas a USD"):
        earned = st.session_state.coins / 232500
        st.session_state.usd_balance += earned
        st.session_state.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Conversión +${earned:.2f} USD")
        st.session_state.coins = 0
        st.success(f"¡Has convertido tus monedas con éxito por ${earned:.2f} USD!")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 🕹️ Centro de Entretenimiento Rápido")
    st.info("💡 Explora las pestañas **'Arcade Marcianitos'** y **'Solitario & Ajedrez'** para jugar en vivo y ganar miles de monedas para tu cuenta.")

# ----------------- 👾 ARCADE MARCIANITOS (NUEVO) -----------------
with menu_tabs[1]:
    st.markdown("### 👾 Invasores Galácticos (Marcianitos Pro)")
    st.markdown("<p style='color: #94a3b8;'>Defiende la galaxia de los marcianitos invasores disparando tu nave láser en rondas tácticas.</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 🛸 Estado de la Nave: Activa (Escudo al 100%)")
    st.markdown(f"**Naves Derribadas en esta partida:** {st.session_state.invader_score}")
    
    # Representación visual del campo de batalla
    cols_inv = st.columns(5)
    aliens = ["👾", "👾", "🛸", "👾", "👾"]
    for i, alien in enumerate(aliens):
        with cols_inv[i]:
            st.markdown(f"<div style='background: #1e293b; text-align: center; padding: 12px; border-radius: 8px; font-size: 24px;'>{alien}</div>", unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    col_fire1, col_fire2 = st.columns(2)
    with col_fire1:
        if st.button("🚀 Disparar Láser Principal"):
            bounty = random.choice([300, 500, 1000])
            st.session_state.invader_score += 1
            st.session_state.coins += bounty
            st.success(f"🎯 ¡Impacto directo! Marcianito destruido. +{bounty} monedas.")
            st.rerun()
    with col_fire2:
        if st.button("🔄 Reiniciar Oleada"):
            st.session_state.invader_score = 0
            st.info("Oleada reiniciada con nuevos invasores.")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- 🃏 SOLITARIO & ♟️ AJEDREZ (NUEVOS) -----------------
with menu_tabs[2]:
    st.markdown("### 🃏 Solitario Zafiro (Klondike Rápido)")
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("Cartas activas en mesa:")
    cols_cards = st.columns(len(st.session_state.solitaire_deck))
    for i, card in enumerate(st.session_state.solitaire_deck):
        with cols_cards[i]:
            st.markdown(f"<div style='background: #f8fafc; color: #0f172a; text-align: center; padding: 15px; border-radius: 8px; font-weight: bold; font-size: 18px;'>{card}</div>", unsafe_allow_html=True)
            
    if st.button("🎴 Robar y Combinar Cartas"):
        new_cards = ["9♥", "Q♣", "10♦", "J♥", "A♦"]
        st.session_state.solitaire_deck = random.sample(new_cards, 3)
        st.session_state.coins += 750
        st.success("¡Jugada válida en el solitario! +750 monedas acreditadas.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### ♟️ Ajedrez Táctico (Reto de Mate)")
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown(f"**Reto actual:** {st.session_state.chess_puzzle['problema']}")
    st.markdown("Encuentra la jugada ganadora para asegurar el jaque mate en un movimiento:")
    
    chess_move = st.selectbox("Selecciona tu jugada maestra:", ["Caballo a c6", "Dama a f7 (Mate)", "Torre a d8", "Peón a e4"])
    if st.button("Validar Movimiento de Ajedrez"):
        if chess_move == "Dama a f7 (Mate)":
            st.session_state.coins += 2000
            st.success("🏆 ¡Excelente cálculo! Mate exacto. +2,000 monedas ganadas.")
            st.rerun()
        else:
            st.warning("⚠️ Movimiento válido, pero el rey escapó. ¡Prueba otra combinación!")
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- 🎡 CARRUSEL -----------------
with menu_tabs[3]:
    st.markdown("### 🎡 Ruleta de Premios ZafiroX")
    st.markdown(f"<div class='card-box'><b>Tokens Disponibles:</b> {st.session_state.tokens} 🪙</div>", unsafe_allow_html=True)
    if st.button("Girar Ruleta Pro"):
        if st.session_state.tokens > 0:
            st.session_state.tokens -= 1
            premio = random.choice([1000, 2500, 5000, 10000, 25000])
            st.session_state.coins += premio
            st.success(f"🎁 ¡Felicidades! Ganaste {premio:,} monedas en la ruleta.")
            st.rerun()
        else:
            st.error("No tienes tokens disponibles.")

# ----------------- 📢 EVENTOS -----------------
with menu_tabs[4]:
    st.markdown("### 🎒 Torneo Semanal de Arcades")
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown(f"**Gems recolectados en juegos:** {st.session_state.gems}/350")
    st.progress(min(st.session_state.gems / 350, 1.0))
    if st.button("Reclamar Bono de Gems (+50 Gems)"):
        st.session_state.gems += 50
        st.success("¡Bonus reclamado! +50 Gems.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- 💰 RETIROS -----------------
with menu_tabs[5]:
    st.markdown("### 🏦 Retiro Inmediato Colombia")
    cop_total = st.session_state.usd_balance * 4000
    st.markdown(f"<div class='card-box'><b>Saldo Disponible:</b> ${st.session_state.usd_balance:.2f} USD (~${cop_total:,.0f} COP)</div>", unsafe_allow_html=True)
    
    metodo = st.selectbox("Método de Retiro", ["Nequi", "Daviplata", "PSE", "PayPal"])
    destino = st.text_input("Número de celular / Cuenta / Correo", placeholder="Ej: 3185312231")
    
    # Manejo dinámico seguro de límites corregido
    max_val = max(0.01, st.session_state.usd_balance)
    min_val = min(1.0, max_val)
    monto_retiro = st.number_input("Monto a retirar en USD", min_value=min_val, max_value=max_val, value=max_val)
    
    cop_valor = monto_retiro * 4000
    st.info(f"Monto a recibir en tu {metodo}: **${cop_valor:,.0f} COP**")
    
    if st.button("🚀 Confirmar Solicitud de Retiro"):
        if st.session_state.usd_balance >= monto_retiro:
            st.session_state.usd_balance -= monto_retiro
            st.session_state.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Retiro {metodo} ({destino}) -${monto_retiro:.2f} USD")
            st.success(f"¡Retiro de ${cop_valor:,.0f} COP procesado con éxito a tu cuenta de {metodo}!")
            st.rerun()
        else:
            st.error("Saldo insuficiente para realizar el retiro.")

    st.markdown("### 📋 Historial de Transacciones")
    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.markdown(f"- {item}")
    else:
        st.markdown("No hay transacciones recientes.")
