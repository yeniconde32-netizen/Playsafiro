import streamlit as st
import streamlit.components.v1 as components
import random

# Configuración inicial de estado para los tokens si no existen
if "tokens" not in st.session_state:
    st.session_state.tokens = 1
if "saldo_usd" not in st.session_state:
    st.session_state.saldo_usd = 0.00

st.title("🎡 ZafiroX - Ruleta de Premios Real")

# Mostrar tokens actuales
st.markdown(f"**Tokens Disponibles:** 🪙 {st.session_state.tokens}")

# Componente HTML + CSS + JavaScript para la ruleta interactiva con físicas reales
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
            width: 250px;
            height: 250px;
            margin: 10px auto;
        }}
        .pointer {{
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 10px solid transparent;
            border-right: 10px solid transparent;
            border-bottom: 20px solid #ef4444;
            z-index: 10;
        }}
        canvas {{
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(124, 58, 237, 0.5);
            transition: transform 4s cubic-bezier(0.15, 0.90, 0.15, 1);
        }}
        .spin-btn {{
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}
        .spin-btn:active {{ transform: scale(0.95); }}
        #result-text {{
            margin-top: 10px;
            font-size: 16px;
            color: #a78bfa;
            font-weight: bold;
        }}
    </style>
</head>
<body>

    <div class="wheel-container">
        <div class="pointer"></div>
        <canvas id="wheel" width="250" height="250"></canvas>
    </div>
    
    <button class="spin-btn" onclick="spinWheel()">Girar Ruleta Pro</button>
    <div id="result-text">¡Gira para ganar tokens o gemas!</div>

    <script>
        const canvas = document.getElementById("wheel");
        const ctx = canvas.getContext("2d");
        const sectors = [
            { color: "#7c3aed", label: "+10 Gemas" },
            { color: "#3b82f6", label: "0.01 USD" },
            { color: "#10b981", label: "+50 Gemas" },
            { color: "#f59e0b", label: "¡Suerte Next!" },
            { color: "#ec4899", label: "0.05 USD" },
            { color: "#6366f1", label: "+5 Gemas" }
        ];
        
        let currentAngle = 0;
        let isSpinning = false;
        const arc = Math.PI / (sectors.length / 2);

        function drawSector(sector, i) {
            const angle = arc * i;
            ctx.beginPath();
            ctx.arc(125, 125, 125, angle, angle + arc, false);
            ctx.lineTo(125, 125);
            ctx.fillStyle = sector.color;
            ctx.fill();
            ctx.save();
            
            ctx.translate(125, 125);
            ctx.rotate(angle + arc / 2);
            ctx.fillStyle = "#fff";
            ctx.font = "bold 12px sans-serif";
            ctx.fillText(sector.label, 50, 10);
            ctx.restore();
        }

        function drawWheel() {
            sectors.forEach(drawSector);
        }
        drawWheel();

        function spinWheel() {
            if (isSpinning) return;
            isSpinning = true;
            document.getElementById("result-text").innerText = "Girando...";
            
            // Generar rotación aleatoria fuerte (entre 5 y 8 vueltas completas extra)
            const randomDegree = Math.floor(Math.random() * 360) + 1800;
            currentAngle += randomDegree;
            
            canvas.style.transform = `rotate(-${currentAngle}deg)`;
            
            setTimeout(() => {
                isSpinning = false;
                const actualDegree = currentAngle % 360;
                const winningIndex = Math.floor((360 - (actualDegree % 360)) / (360 / sectors.length)) % sectors.length;
                const prize = sectors[winningIndex].label;
                
                document.getElementById("result-text").innerText = "¡Premio obtenido: " + prize + "!";
            }, 4000);
        }
    </script>
</body>
</html>
"""

# Renderizar el componente visual interactivo
components.html(ruleta_html, height=380)

# Botón de respaldo en Streamlit para sincronizar lógica de tokens si lo deseas
if st.button("Actualizar mis Tokens / Reclamar Premio"):
    if st.session_state.tokens > 0:
        st.session_state.tokens -= 1
        st.session_state.saldo_usd += 0.01
        st.success("¡Premio procesado y sumado a tu cuenta exitosamente!")
    else:
        st.error("No tienes tokens disponibles. ¡Mira un anuncio o juega para ganar más!")
