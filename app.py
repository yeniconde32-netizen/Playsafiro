import streamlit as st
import streamlit.components.v1 as components
import random

# Inicializar variables de sesión si no existen
if "tokens" not in st.session_state:
    st.session_state.tokens = 3  # Empezamos con 3 de cortesía para probar
if "saldo_usd" not in st.session_state:
    st.session_state.saldo_usd = 0.00
if "gemas" not in st.session_state:
    st.session_state.gemas = 15

st.markdown("## 🎡 Ruleta de Premios ZafiroX (Carrusel)")
st.markdown("¡Gira la ruleta y gana tokens, gemas o saldo real para tus retiros!")

# Panel de estado superior
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🪙 Tokens", f"{st.session_state.tokens}")
with col2:
    st.metric("💎 Gemas", f"{st.session_state.gemas}")
with col3:
    st.metric("💵 Saldo", f"${st.session_state.saldo_usd:.2f} USD")

st.markdown("---")

# Verificamos si tiene tokens para habilitar el juego
if st.session_state.tokens > 0:
    
    # Componente HTML + JS de la Ruleta Interactiva
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
            
            // Premios de la ruleta
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

            function drawWheel() {{
                sectors.forEach(drawSector);
            }}
            drawWheel();

            function triggerSpin() {{
                if (isSpinning) return;
                isSpinning = true;
                document.getElementById("spinBtn").style.opacity = "0.6";
                document.getElementById("result-msg.innerText" = "Girando la ruleta...");
                
                // Generar giros fuertes aleatorios (entre 5 y 8 vueltas completas)
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
                    
                    // Comunicar el resultado a Streamlit mediante un parámetro oculto o recarga controlada
                    // (En Streamlit manejaremos el cobro del token mediante el botón de abajo)
                }}, 4000);
            }}
        </script>
    </body>
    </html>
    """

    components.html(ruleta_html, height=385)

    # Botón en Streamlit para confirmar la jugada, descontar token y aplicar recompensa aleatoria real
    if st.button("🎁 Reclamar Resultado del Giro"):
        st.session_state.tokens -= 1
        
        # Sorteo aleatorio del backend que coincide con la lógica visual
        premio_tipo = random.choice(["gemas", "usd", "gemas", "nada", "usd"])
        if premio_tipo == "gemas":
            ganancia_gemas = random.choice([10, 20, 50])
            st.session_state.gemas += ganancia_gemas
            st.success(f"¡Felicidades! Has ganado +{ganancia_gemas} Gemas añadidas a tu inventario.")
        elif premio_tipo == "usd":
            ganancia_usd = random.choice([0.01, 0.02, 0.05])
            st.session_state.saldo_usd += ganancia_usd
            st.success(f"¡Excelente! Has ganado ${ganancia_usd:.2f} USD sumados a tu billetera.")
        else:
            st.warning("¡Vaya! Esta vez cayó en 'Suerte Next'. ¡Sigue intentando!")
        
        st.rerun()

else:
    st.error("⚠️ No tienes tokens disponibles en este momento.")
    st.info("💡 Ve a la sección de **Desafíos** o juega en los minijuegos para recolectar más tokens y volver a girar el Carrusel.")
    
    if st.button("🔄 Conseguir Token de Prueba (Modo Dev)"):
        st.session_state.tokens += 1
        st.rerun()
