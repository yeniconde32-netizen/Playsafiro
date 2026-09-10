import streamlit as st
import streamlit.components.v1 as components
import random

# Configuración inicial de la página
st.set_page_config(
    page_title="ZafiroX - Recompensas y Juegos",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- INICIALIZACIÓN DE VARIABLES DE SESIÓN ---
if "tokens" not in st.session_state:
    st.session_state.tokens = 3  # Tokens iniciales para la ruleta
if "saldo_usd" not in st.session_state:
    st.session_state.saldo_usd = 0.00
if "surge_coins" not in st.session_state:
    st.session_state.surge_coins = 10000000  # 10M+ Monedas iniciales
if "gemas" not in st.session_state:
    st.session_state.gemas = 15
if "daily_challenge_progress" not in st.session_state:
    st.session_state.daily_challenge_progress = 3
if "daily_challenge_max" not in st.session_state:
    st.session_state.daily_challenge_max = 5
if "weekly_gems_collected" not in st.session_state:
    st.session_state.weekly_gems_collected = 1000
if "weekly_gem_goal" not in st.session_state:
    st.session_state.weekly_gem_goal = 3500
if "streak_day" not in st.session_state:
    st.session_state.streak_day = 2

# --- BARRA DE NAVEGACIÓN LATERAL ---
st.sidebar.markdown("## 🧭 Navegación ZafiroX")
menu = st.sidebar.radio(
    "Selecciona una sección:",
    ["🏠 Inicio", "⚔️ Desafíos", "🎡 Carrusel (Ruleta)", "🔥 Recompensas (Racha)", "🎒 Eventos (Weekly Pot)", "💰 Billetera & Retiros"]
)

# --- PANEL SUPERIOR GLOBAL DE ESTADO ---
col_s1, col_s2, col_s3, col_s4 = st.columns(4)
with col_s1:
    st.metric("🪙 Monedas", f"{st.session_state.surge_coins:,}")
with col_s2:
    st.metric("💎 Gemas", f"{st.session_state.gemas}")
with col_s3:
    st.metric("🎟️ Tokens", f"{st.session_state.tokens}")
with col_s4:
    st.metric("💵 Saldo", f"${st.session_state.saldo_usd:.2f}")

st.markdown("---")

# ==========================================
# 1. 🏠 SECCIÓN DE INICIO
# ==========================================
if menu == "🏠 Inicio":
    st.markdown("## 🏠 Bienvenido a ZafiroX")
    st.markdown("¡Tu plataforma centralizada de minijuegos, desafíos diarios y recompensas reales!")
    
    st.info("💡 Usa el menú lateral para navegar entre los desafíos activos, girar la ruleta de premios o cobrar tus ganancias a tu método de pago preferido.")
    
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        if st.button("🚀 Ir a Desafíos Diarios"):
            st.session_state.menu_override = "⚔️ Desafíos"
            st.rerun()
    with col_i2:
        if st.button("🎡 Girar la Ruleta Pro"):
            st.rerun()

# ==========================================
# 2. ⚔️ SECCIÓN DE DESAFÍOS (Merge Blast)
# ==========================================
elif menu == "⚔️ Desafíos":
    st.markdown("## 🎯 Desafíos Activos")
    st.markdown("¡Completa misiones para ganar monedas, gemas y tokens para el carrusel!")

    with st.container():
        st.markdown("""
        <div style='background-color: #262730; padding: 20px; border-radius: 12px; border: 1px solid #3a3b42;'>
            <h4 style='color: #ffffff; margin-top: 0;'>Desafío Diario: Merge Blast</h4>
            <p style='color: #b0b0b0; font-size: 14px;'>Completa 5 niveles en Merge Blast para ganar 1,000 monedas y 50 Gemas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        progreso_actual = st.session_state.daily_challenge_progress
        progreso_max = st.session_state.daily_challenge_max
        st.text(f"Progreso: {progreso_actual}/{progreso_max}")
        st.progress(progreso_actual / progreso_max)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🎮 Jugar / Avanzar Nivel"):
                if st.session_state.daily_challenge_progress < st.session_state.daily_challenge_max:
                    st.session_state.daily_challenge_progress += 1
                    st.session_state.surge_coins += 200
                    st.success("¡Nivel completado! +200 Monedas añadidas.")
                    st.rerun()
                else:
                    st.info("¡El desafío diario ya fue completado hoy!")
                    
        with col_btn2:
            if st.button("🚀 Completar Tarea (Simular Anuncio)"):
                st.session_state.gemas += 50
                st.session_state.tokens += 1
                st.session_state.daily_challenge_progress = st.session_state.daily_challenge_max
                st.success("¡Anuncio simulado! +50 Gemas y +1 Token de regalo.")
                st.rerun()

# ==========================================
# 3. 🎡 SECCIÓN CARRUSEL (RULETA DE PREMIOS)
# ==========================================
elif menu == "🎡 Carrusel (Ruleta)":
    st.markdown("## 🎡 Ruleta de Premios ZafiroX")
    st.markdown("¡Gira la ruleta y gana tokens, gemas o saldo real para tus retiros!")

    if st.session_state.tokens > 0:
        ruleta_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    background-color: transparent;
                    color: white;
                    text-align: center;
                    font-family: sans-serif;
                    margin: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                }}
                .wheel-container {{
                    position: relative;
                    width: 260px;
                    height: 260px;
                    margin: 5px auto;
                }}
                .pointer {{
                    position: absolute;
                    top: -12px;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 0;
                    height: 0;
                    border-left: 12px solid transparent;
                    border-right: 12px solid transparent;
                    border-bottom: 22px solid #ef4444;
                    z-index: 10;
                }}
                canvas {{
                    border-radius: 50%;
                    box-shadow: 0 0 20px rgba(124, 58, 237, 0.6);
                    transition: transform 4s cubic-bezier(0.15, 0.90, 0.15, 1);
                }}
                .spin-btn {{
                    background: linear-gradient(135deg, #8b5cf6, #6366f1);
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 10px;
                    cursor: pointer;
                    margin-top: 15px;
                    box-shadow: 0 4px 12px rgba(110, 68, 255, 0.4);
                }}
                .spin-btn:active {{ transform: scale(0.95); }}
                #result-msg {{
                    margin-top: 12px;
                    font-size: 15px;
                    color: #c084fc;
                    font-weight: bold;
                    min-height: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="wheel-container">
                <div class="pointer"></div>
                <canvas id="wheel" width="260" height="260"></canvas>
            </div>
            <button class="spin-btn" id="spinBtn" onclick="triggerSpin()">¡Girar Ruleta Pro!</button>
            <div id="result-msg">¡Listo para girar!</div>

            <script>
                const canvas = document.getElementById("wheel");
                const ctx = canvas.getContext("2d");
                const sectors = [
                    {{ color: "#7c3aed", label: "+20 Gemas", type: "gemas", val: 20 }},
                    {{ color: "#3b82f6", label: "$0.02 USD", type: "usd", val: 0.02 }},
                    {{ color: "#10b981", label: "+50 Gemas", type: "gemas", val: 50 }},
                    {{ color: "#f59e0b", label: "¡Suerte Next!", type: "nada", val: 0 }},
                    {{ color: "#ec4899", label: "$0.05 USD", type: "usd", val: 0.05 }},
                    {{ color: "#6366f1", label: "+10 Gemas", type: "gemas", val: 10 }}
                ];
                let currentAngle = 0;
                let isSpinning = false;
                const arc = Math.PI / (sectors.length / 2);

                function drawSector(sector, i) {{
                    const angle = arc * i;
                    ctx.beginPath();
                    ctx.arc(130, 130, 130, angle, angle + arc, false);
                    ctx.lineTo(130, 130);
                    ctx.fillStyle = sector.color;
                    ctx.fill();
                    ctx.save();
                    ctx.translate(130, 130);
                    ctx.rotate(angle + arc / 2);
                    ctx.fillStyle = "#fff";
                    ctx.font = "bold 12px sans-serif";
                    ctx.fillText(sector.label, 55, 8);
                    ctx.restore();
                }}

                function drawWheel() {{ sectors.forEach(drawSector); }}
                drawWheel();

                function triggerSpin() {{
                    if (isSpinning) return;
                    isSpinning = true;
                    document.getElementById("spinBtn").style.opacity = "0.6";
                    document.getElementById("result-msg").innerText = "Girando la ruleta...";
                    
                    const randomDegree = Math.floor(Math.random() * 360) + 1800;
                    currentAngle += randomDegree;
                    canvas.style.transform = `rotate(-${currentAngle}deg)`;
                    
                    setTimeout(() => {{
                        isSpinning = false;
                        document.getElementById("spinBtn").style.opacity = "1";
                        const actualDegree = currentAngle % 360;
                        const winningIndex = Math.floor((360 - (actualDegree % 360)) / (360 / sectors.length)) % sectors.length;
                        const winningSector = sectors[winningIndex];
                        document.getElementById("result-msg").innerText = "¡Premio: " + winningSector.label + "!";
                    }}, 4000);
                }}
            </script>
        </body>
        </html>
        """
        components.html(ruleta_html, height=385)

        if st.button("🎁 Reclamar Resultado del Giro"):
            st.session_state.tokens -= 1
            premio_tipo = random.choice(["gemas", "usd", "gemas", "nada", "usd"])
            if premio_tipo == "gemas":
                g_gemas = random.choice([10, 20, 50])
                st.session_state.gemas += g_gemas
                st.success(f"¡Felicidades! Has ganado +{g_gemas} Gemas.")
            elif premio_tipo == "usd":
                g_usd = random.choice([0.01, 0.02, 0.05])
                st.session_state.saldo_usd += g_usd
                st.success(f"¡Excelente! Has ganado ${g_usd:.2f} USD sumados a tu billetera.")
            else:
                st.warning("¡Vaya! Cayó en 'Suerte Next'. ¡Sigue intentando!")
            st.rerun()
    else:
        st.error("⚠️ No tienes tokens disponibles en este momento.")
        if st.button("🔄 Conseguir Token de Prueba (Modo Dev)"):
            st.session_state.tokens += 1
            st.rerun()

# ==========================================
# 4. 🔥 RECOMPENSAS (RACHA DIARIA)
# ==========================================
elif menu == "🔥 Recompensas (Racha)":
    st.markdown("## 🔥 Recompensa de Racha Diaria")
    
    with st.container():
        st.markdown(f"""
        <div style='background-color: #262730; padding: 20px; border-radius: 12px; border: 1px solid #3a3b42;'>
            <h4 style='color: #ffffff; margin-top: 0;'>Día {st.session_state.streak_day} - Reclamable</h4>
            <p style='color: #b0b0b0; font-size: 14px;'>Mira anuncios cortos o juega para desbloquear tu progreso diario y acumular bonos masivos.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    if st.button("🎁 Reclamar Bono Diario"):
        st.session_state.gemas += 30
        st.session_state.streak_day += 1
        st.success("¡Bono diario reclamado con éxito! +30 Gemas añadidas.")
        st.rerun()

# ==========================================
# 5. 🎒 EVENTOS (WEEKLY POT)
# ==========================================
elif menu == "🎒 Eventos (Weekly Pot)":
    st.markdown("## 🎒 Weekly Pot - $1,000 en Premios")

    with st.container():
        st.markdown("""
        <div style='background-color: #262730; padding: 20px; border-radius: 12px; border: 1px solid #3a3b42;'>
            <h4 style='color: #ffffff; margin-top: 0;'>¡Califica, protege y gana en el evento semanal de ZafiroX!</h4>
            <p style='color: #b0b0b0; font-size: 14px;'>Acumula gemas recolectadas para asegurar tu participación en el pozo global.</p>
        </div>
        """, unsafe_allow_html=True)

    gems_col = st.session_state.weekly_gems_collected
    gems_meta = st.session_state.weekly_gem_goal
    
    st.text(f"Gems recolectados: {gems_col} / {gems_meta}")
    st.progress(min(1.0, gems_col / gems_meta))

    if st.button("📺 Ver Anuncio Corto para Gems (+50 Gems)"):
        st.session_state.weekly_gems_collected += 50
        st.session_state.gemas += 25
        st.success("¡Anuncio visto! +50 Gems sumadas a tu pozo y +25 Gemas a tu inventario.")
        st.rerun()

# ==========================================
# 6. 💰 BILLETERA & RETIROS (CORREGIDA)
# ==========================================
elif menu == "💰 Billetera & Retiros":
    st.markdown("## 💰 Billetera & Retiros ZafiroX")
    
    # Conversión segura y métricas
    coins_disponibles = st.session_state.surge_coins
    equivalente_usd = coins_disponibles / 28571400  # Tasa de conversión estimada
    
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.metric("Equivalente en Monedas", f"{coins_disponibles:,}")
    with col_w2:
        st.metric("Saldo Disponible USD", f"${st.session_state.saldo_usd:.2f} USD")

    st.markdown("---")
    st.markdown("### 🏦 Retiro Inmediato (Nequi / Daviplata / PayPal)")

    metodo_retiro = st.selectbox("Método de Retiro", ["Nequi", "Daviplata", "PayPal", "PSE"])
    destino = st.text_input("Número de celular / Cuenta / Correo", placeholder="Ej: 3185312231")

    # Corrección blindada para evitar el StreamlitValueBelowMinError
    monto_maximo = max(0.01, float(st.session_state.saldo_usd if st.session_state.saldo_usd > 0 else 0.01))
    
    monto_retiro = st.number_input(
        "Monto a retirar en USD",
        min_value=0.01,
        max_value=float(monto_maximo),
        value=min(0.01, monto_maximo),
        step=0.01
    )

    if st.button("🚀 ¡Cobrar y Convertir Fondos!"):
        if st.session_state.saldo_usd >= monto_retiro and destino:
            st.session_state.saldo_usd -= monto_retiro
            st.success(f"¡Solicitud de retiro por ${monto_retiro:.2f} USD hacia {metodo_retiro} ({destino}) procesada con éxito!")
        else:
            st.error("Verifica que tengas saldo disponible en USD y el número/cuenta de destino escrito correctamente.")
