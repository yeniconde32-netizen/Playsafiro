import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components

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
    .ad-banner {
        background: rgba(15, 23, 42, 0.9);
        border: 2px dashed #475569;
        padding: 12px;
        text-align: center;
        border-radius: 12px;
        color: #94a3b8;
        font-size: 13px;
        margin: 15px 0;
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

# Estados dinámicos para los 8 minijuegos
if "invader_score" not in st.session_state:
    st.session_state.invader_score = 21
if "alien_positions" not in st.session_state:
    st.session_state.alien_positions = ["👾", "👾", "🛸", "👾", "👾"]
if "solitaire_deck" not in st.session_state:
    st.session_state.solitaire_deck = ["Q♣", "A♦", "9♥"]
if "chess_puzzle" not in st.session_state:
    st.session_state.chess_puzzle = {"problema": "Mate en 1: Dama en f7", "resuelto": False}
if "slots_result" not in st.session_state:
    st.session_state.slots_result = ["🍒", "🍋", "🔔"]
if "box_status" not in st.session_state:
    st.session_state.box_status = "Caja cerrada esperando apertura..."
if "memory_score" not in st.session_state:
    st.session_state.memory_score = 0
if "coin_flip_res" not in st.session_state:
    st.session_state.coin_flip_res = "¡Elige Cara o Sello!"

# Función para mostrar bloques de anuncios monetizables
def render_ad_slot(slot_name="Banner Principal"):
    st.markdown(f"""
        <div class="ad-banner">
            📢 [Espacio Publicitario Monetizable - {slot_name}]<br>
            <span style="font-size: 11px; color: #64748b;">Aquí se carga tu código de AdSense / Red de Anuncios automáticamente</span>
        </div>
    """, unsafe_allow_html=True)

# Autenticación Simulada si no ha iniciado sesión
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>💎 ZafiroX Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>¡8 Minijuegos arcade, ruletas y retiros instantáneos!</p>", unsafe_allow_html=True)
    
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

render_ad_slot("Cabecera Superior")
st.markdown("---")

# Navegación con pestañas mejoradas (Organizadas para incluir los 8 juegos)
menu_tabs = st.tabs(["🏠 Billetera", "🕹️ Juegos 1-3 (Arcade)", "🎰 Juegos 4-6 (Azar)", "🎯 Juegos 7-8 & Ruleta", "📢 Eventos", "💰 Retiros"])

# ----------------- 🏠 BILLETERA & INICIO -----------------
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
    
    st.markdown("### 🕹️ Catálogo de Entretenimiento ZafiroX")
    st.info("💡 Explora las pestañas de **Juegos** para divertirte con los 8 títulos interactivos y acumular miles de monedas para tus retiros.")
    render_ad_slot("Mitad de Página Inicio")

# ----------------- 🕹️ JUEGOS 1 al 3 (ARCADE, CARTAS Y AJEDREZ) -----------------
with menu_tabs[1]:
    st.markdown("### 🕹️ Sala Arcade & Mesa (Juegos 1, 2 y 3)")
    
    # JUEGO 1: INVASORES GALÁCTICOS
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 1️⃣ 👾 Invasores Galácticos (Marcianitos Pro)")
    st.markdown(f"**Naves Derribadas:** {st.session_state.invader_score}")
    cols_inv = st.columns(len(st.session_state.alien_positions))
    for i, alien in enumerate(st.session_state.alien_positions):
        with cols_inv[i]:
            st.markdown(f"<div style='background: #1e293b; text-align: center; padding: 10px; border-radius: 8px; font-size: 22px;'>{alien}</div>", unsafe_allow_html=True)
    
    if st.button("🚀 Disparar Láser Principal (Juego 1)"):
        bounty = random.choice([300, 500, 1000])
        st.session_state.invader_score += 1
        st.session_state.coins += bounty
        random.shuffle(st.session_state.alien_positions)
        st.success(f"🎯 ¡Impacto! +{bounty} monedas.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # JUEGO 2: SOLITARIO ZAFIRO
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 2️⃣ 🃏 Solitario Zafiro (Klondike Rápido)")
    cols_cards = st.columns(len(st.session_state.solitaire_deck))
    for i, card in enumerate(st.session_state.solitaire_deck):
        with cols_cards[i]:
            st.markdown(f"<div style='background: #f8fafc; color: #0f172a; text-align: center; padding: 12px; border-radius: 8px; font-weight: bold;'>{card}</div>", unsafe_allow_html=True)
            
    if st.button("🎴 Robar y Combinar Cartas (Juego 2)"):
        pool_cartas = ["A♠", "10♥", "K♦", "7♣", "J♠", "Q♣", "A♦", "9♥", "8♠", "J♥"]
        st.session_state.solitaire_deck = random.sample(pool_cartas, 3)
        st.session_state.coins += 750
        st.success("¡Cartas combinadas en mesa! +750 monedas.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # JUEGO 3: AJEDREZ TÁCTICO
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 3️⃣ ♟️ Ajedrez Táctico (Reto de Mate)")
    st.markdown(f"**Reto:** {st.session_state.chess_puzzle['problema']}")
    chess_move = st.selectbox("Tu jugada maestra:", ["Caballo a c6", "Dama a f7 (Mate)", "Torre a d8", "Peón a e4"], key="chess_sel")
    if st.button("Validar Movimiento de Ajedrez (Juego 3)"):
        if chess_move == "Dama a f7 (Mate)":
            st.session_state.coins += 2000
            st.success("🏆 ¡Mate exacto! +2,000 monedas.")
            st.rerun()
        else:
            st.warning("⚠️ El rey escapó. ¡Prueba otra combinación!")
    st.markdown("</div>", unsafe_allow_html=True)
    render_ad_slot("Pie de Sala Arcade")

# ----------------- 🎰 JUEGOS 4 al 6 (SLOTS, CAJAS Y MEMORIA) -----------------
with menu_tabs[2]:
    st.markdown("### 🎰 Sala de Azar y Suerte (Juegos 4, 5 y 6)")
    
    # JUEGO 4: MINI TRAGAMONEDAS (SLOTS)
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 4️⃣ 🎰 Mini Tragamonedas Zafiro")
    cols_slots = st.columns(3)
    for i, sym in enumerate(st.session_state.slots_result):
        with cols_slots[i]:
            st.markdown(f"<div style='background: #1e293b; text-align: center; padding: 15px; border-radius: 8px; font-size: 28px;'>{sym}</div>", unsafe_allow_html=True)
            
    if st.button("🎲 Jirar Slots / Tragamonedas (Juego 4)"):
        simbolos = ["🍒", "🍋", "🔔", "💎", "⭐", "7️⃣"]
        st.session_state.slots_result = [random.choice(simbolos), random.choice(simbolos), random.choice(simbolos)]
        if st.session_state.slots_result[0] == st.session_state.slots_result[1] == st.session_state.slots_result[2]:
            st.session_state.coins += 10000
            st.success("JACKPOT TRIPLE 💎 +10,000 monedas ganadas.")
        else:
            st.session_state.coins += 400
            st.success("¡Buen intento! +400 monedas acreditadas.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # JUEGO 5: CAJA MISTERIOSA
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 5️⃣ 📦 Caja Misteriosa de Recompensas")
    st.markdown(f"**Estado:** {st.session_state.box_status}")
    if st.button("🎁 Abrir Caja Misteriosa (Juego 5)"):
        premio_caja = random.choice([500, 1500, 3000, 5000])
        st.session_state.coins += premio_caja
        st.session_state.box_status = f"¡Caja abierta! Encontraste {premio_caja:,} monedas."
        st.success(f"¡Tesoro descubierto! +{premio_caja:,} monedas.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # JUEGO 6: MEMORIA FLASH
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 6️⃣ 🧠 Memoria Flash Numérica")
    st.markdown(f"**Puntuación de Memoria:** {st.session_state.memory_score} aciertos")
    secuencia_activa = random.randint(100, 999)
    st.info(f"🔢 Secuencia clave a memorizar: **{secuencia_activa}**")
    guess_mem = st.text_input("Introduce los dígitos recordados:", placeholder="Ej: 482", key="mem_input")
    if st.button("Verificar Memoria Flash (Juego 6)"):
        st.session_state.memory_score += 1
        st.session_state.coins += 1200
        st.success("🧠 ¡Excelente memoria! +1,200 monedas acreditadas.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    render_ad_slot("Pie de Sala de Azar")

# ----------------- 🎯 JUEGOS 7 al 8 & RULETA -----------------
with menu_tabs[3]:
    st.markdown("### 🎯 Retos Rápidos y Ruleta (Juegos 7 y 8)")
    
    # JUEGO 7: ADIVINA LA MONEDA (CARA O SELLO)
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 7️⃣ 🪙 Duelo Cara o Sello")
    st.markdown(f"**Resultado:** {st.session_state.coin_flip_res}")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        if st.button("Elegir Cara (🪙)"):
            res = random.choice(["Cara", "Sello"])
            if res == "Cara":
                st.session_state.coins += 1500
                st.success("¡Cayó Cara! Ganaste +1,500 monedas.")
            else:
                st.warning("Cayó Sello. ¡Sigue intentando!")
            st.rerun()
    with col_c2:
        if st.button("Elegir Sello (🪙)"):
            res = random.choice(["Cara", "Sello"])
            if res == "Sello":
                st.session_state.coins += 1500
                st.success("¡Cayó Sello! Ganaste +1,500 monedas.")
            else:
                st.warning("Cayó Cara. ¡Sigue intentando!")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # JUEGO 8: RULETA DE LA FORTUNA PRO (CONSERVANDO LA RULETA ORIGINAL)
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("#### 8️⃣ 🎡 Ruleta de Premios ZafiroX")
    st.markdown(f"<b>Tokens Disponibles:</b> {st.session_state.tokens} 🪙", unsafe_allow_html=True)
    if st.button("Girar Ruleta Pro (Juego 8)"):
        if st.session_state.tokens > 0:
            st.session_state.tokens -= 1
            premio = random.choice([1000, 2500, 5000, 10000, 25000])
            st.session_state.coins += premio
            st.success(f"🎁 ¡Felicidades! Ganaste {premio:,} monedas en la ruleta.")
            st.rerun()
        else:
            st.error("No tienes tokens disponibles.")
    st.markdown("</div>", unsafe_allow_html=True)
    render_ad_slot("Patrocinador de Ruleta")

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

render_ad_slot("Footer Inferior Global")
