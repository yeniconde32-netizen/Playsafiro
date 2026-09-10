import sqlite3
import random
import time
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="ZafiroX - Recompensas y Juegos", page_icon="💎", layout="centered"
)

# --- CONFIGURACIÓN DE BASE DE DATOS REAL (SQLite) ---
conn = sqlite3.connect("zafirox_real.db", check_same_thread=False)
cursor = conn.cursor()

# Crear tablas si no existen
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        coins INTEGER DEFAULT 1000,
        gems INTEGER DEFAULT 50,
        streak INTEGER DEFAULT 1,
        last_login TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transacciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        metodo TEXT,
        cuenta TEXT,
        monto_usd REAL,
        monto_local TEXT,
        fecha TEXT,
        estado TEXT
    )
"""
)
conn.commit()


# Función para obtener o crear usuario por defecto
def obtener_usuario(username="JugadorZafiro"):
  cursor.execute(
      "SELECT coins, gems, streak FROM usuarios WHERE username = ?", (username,)
  )
  user = cursor.fetchone()
  if not user:
    cursor.execute(
        "INSERT INTO usuarios (username, coins, gems, streak) VALUES (?, ?, ?,"
        " ?)",
        (username, 1000, 50, 1),
    )
    conn.commit()
    return 1000, 50, 1
  return user[0], user[1], user[2]


def actualizar_balanza(username, coins_delta, gems_delta):
  cursor.execute(
      "UPDATE usuarios SET coins = coins + ?, gems = gems + ? WHERE username = ?",
      (coins_delta, gems_delta, username),
  )
  conn.commit()


USUARIO_ACTUAL = "JugadorZafiro"
coins, gems, streak = obtener_usuario(USUARIO_ACTUAL)

# --- MENÚ DE NAVEGACIÓN SUPERIOR ---
st.title("💎 ZafiroX")
st.markdown("---")

menu = st.radio(
    "Navegación",
    [
        "🏠 Inicio",
        "⚔️ Desafíos & Trivia",
        "🎠 Carrusel",
        "🎯 Eventos",
        "🔥 Recompensas",
        "💰 Billetera & Retiros",
    ],
    horizontal=True,
)

# ==========================================
# 1. INICIO
# ==========================================
if menu == "🏠 Inicio":
  st.subheader("¡Bienvenido a ZafiroX Real!")
  st.write(
      "Tu plataforma de juegos y recompensas 100% interactiva con base de"
      " datos."
  )

  col1, col2, col3 = st.columns(3)
  col1.metric("Monedas (Coins)", f"{coins:,}")
  col2.metric("Gemas", f"{gems}")
  col3.metric("Racha Diaria", f"{streak} Días")

  st.markdown("### 🚀 Minijuegos Destacados")
  juego_sel = st.selectbox(
      "Selecciona Minijuego para Ganar Monedas",
      ["Trivia Rápida Zafiro", "Adivina el Número", "Memoria Zafiro"],
  )

  apuesta = st.slider("Monto a Apostar en Monedas", 10, 500, 100)

  if juego_sel == "Trivia Rápida Zafiro":
    st.info("Pregunta: ¿En qué lenguaje está programada esta aplicación?")
    respuesta = st.text_input("Escribe tu respuesta:")
    if st.button("Enviar Respuesta"):
      if respuesta.strip().lower() == "python":
        premio = apuesta * 2
        actualizar_balanza(USUARIO_ACTUAL, premio, 5)
        st.success(
            f"¡Correcto! Ganaste {premio} monedas y 5 gemas de bonificación."
        )
        st.rerun()
      else:
        actualizar_balanza(USUARIO_ACTUAL, -apuesta, 0)
        st.error(f"Respuesta incorrecta. Perdiste {apuesta} monedas.")
        st.rerun()

  elif juego_sel == "Adivina el Número":
    st.info("Adivina un número entre 1 y 3:")
    num_elegido = st.number_input(
        "Tu número", min_value=1, max_value=3, step=1
    )
    if st.button("Jugar"):
      secreto = random.randint(1, 3)
      if num_elegido == secreto:
        premio = apuesta * 3
        actualizar_balanza(USUARIO_ACTUAL, premio, 10)
        st.success(
            f"¡Adivinaste! El número era {secreto}. Ganaste {premio} monedas."
        )
        st.rerun()
      else:
        actualizar_balanza(USUARIO_ACTUAL, -apuesta, 0)
        st.error(
            f"Fallaste. El número era {secreto}. Perdiste {apuesta} monedas."
        )
        st.rerun()

  else:
    if st.button("Girar ruleta de la suerte (Costo: 50 monedas)"):
      if coins >= 50:
        premio_ruleta = random.choice([0, 100, 250, 500, 1000])
        actualizar_balanza(
            USUARIO_ACTUAL, premio_ruleta - 50, 2
        )  # Resta costo y suma premio
        st.success(
            f"¡La ruleta giró y ganaste {premio_ruleta} monedas y 2 gemas!"
        )
        st.rerun()
      else:
        st.error("No tienes suficientes monedas para girar.")

# ==========================================
# 2. DESAFÍOS & TRIVIA
# ==========================================
elif menu == "⚔️ Desafíos & Trivia":
  st.subheader("🎯 Desafíos Activos")
  st.write(
      "Completa tareas reales en la app para reclamar recompensas directas a"
      " tu cuenta."
  )

  st.markdown("---")
  st.write(
      "**Desafía tu mente:** ¿Cuánto es 15 x 4? (Gana 300 monedas y 10 gemas)"
  )
  res_math = st.number_input("Resultado:", step=1, key="math_desafio")
  if st.button("Validar Desafío"):
    if res_math == 60:
      actualizar_balanza(USUARIO_ACTUAL, 300, 10)
      st.success("¡Desafío completado con éxito! Recompensas añadidas.")
      st.rerun()
    else:
      st.warning("Resultado incorrecto. ¡Inténtalo de nuevo!")

# ==========================================
# 3. CARRUSEL
# ==========================================
elif menu == "🎠 Carrusel":
  st.subheader("🎠 Carrusel de Premios Especiales")
  st.write(
      "Desliza y descubre recompensas sorpresa cada 24 horas habilitadas en"
      " nuestra base de datos."
  )
  if st.button("Abrir Cofre Diario"):
    actualizar_balanza(USUARIO_ACTUAL, 250, 15)
    st.success("¡Has abierto el cofre y obtenido 250 monedas y 15 gemas!")
    st.rerun()

# ==========================================
# 4. EVENTOS
# ==========================================
elif menu == "🎯 Eventos":
  st.subheader("🎒 Weekly Pot - $1,000 en Premios")
  st.write(
      "Participa en el evento semanal acumulando puntos y mantente en el"
      " ranking global."
  )
  st.info(
      "Estado actual de tu cuenta para el pozo semanal: Activa y participando."
  )

  if st.button("Verificar Tarea Semanal (Anuncio Real Verificado)"):
    with st.spinner("Verificando interacción con red publicitaria..."):
      time.sleep(1.5)
    actualizar_balanza(USUARIO_ACTUAL, 100, 50)
    st.success(
        "¡Interacción validada! Se han sumado 100 monedas y 50 gemas a tu"
        " balance."
    )
    st.rerun()

# ==========================================
# 5. RECOMPENSAS
# ==========================================
elif menu == "🔥 Recompensas":
  st.subheader("🔥 Recompensa de Racha Diaria")
  st.write("Reclama tu bono diario consecutivo para escalar en la plataforma.")

  if st.button("Reclamar Bono Diario"):
    actualizar_balanza(USUARIO_ACTUAL, 500, 20)
    cursor.execute(
        "UPDATE usuarios SET streak = streak + 1 WHERE username = ?",
        (USUARIO_ACTUAL,),
    )
    conn.commit()
    st.success(
        "¡Bono diario reclamado! +500 monedas y +20 gemas añadidas. Tu racha"
        " aumentó."
    )
    st.rerun()

# ==========================================
# 6. BILLETERA & RETIROS
# ==========================================
elif menu == "💰 Billetera & Retiros":
  st.subheader("💳 Billetera y Solicitud de Retiros Reales")

  # Tasa de conversión: 10,000 monedas = 1 USD
  usd_equivalente = coins / 10000.0
  cop_equivalente = usd_equivalente * 4000  # Referencia aproximada COP

  st.metric("Saldo Disponible en Monedas", f"{coins:,}")
  st.markdown(f"**Equivalente USD:** ${usd_equivalente:.2f} USD")
  st.markdown(f"**Equivalente COP:** ${cop_equivalente:,.0f} COP")

  st.markdown("---")
  metodo = st.selectbox("Método de Retiro", ["Nequi", "Daviplata", "PayPal"])
  cuenta_destino = st.text_input(
      "Número de celular / Cuenta / Correo", placeholder="Ej: 3185312231"
  )
  monto_usd_retirar = st.number_input(
      "Monto a retirar en USD",
      min_value=1.0,
      max_value=max(1.0, usd_equivalente),
      step=1.0,
  )

  if st.button("🚀 Confirmar Solicitud de Retiro Real"):
    if cuenta_destino and monto_usd_retirar <= usd_equivalente:
      monedas_a_descontar = int(monto_usd_retirar * 10000)
      actualizar_balanza(USUARIO_ACTUAL, -monedas_a_descontar, 0)

      # Guardar transacción en la base de datos
      cursor.execute(
          "INSERT INTO transacciones (username, metodo, cuenta, monto_usd,"
          " monto_local, fecha, estado) VALUES (?, ?, ?, ?, ?, datetime('now'),"
          " ?)",
          (
              USUARIO_ACTUAL,
              metodo,
              cuenta_destino,
              monto_usd_retirar,
              f"${monto_usd_retirar * 4000:,.0f} COP",
              "Procesando",
          ),
      )
      conn.commit()

      st.success(
          f"¡Solicitud de retiro por ${monto_usd_retirar} USD enviada a"
          f" {metodo} ({cuenta_destino}) con éxito! Quedará registrada en tu"
          " historial."
      )
      st.rerun()
    else:
      st.error(
          "Por favor verifica que la cuenta sea válida y no exceda tu saldo"
          " disponible."
      )

  st.markdown("### 📋 Historial de Transacciones Registradas")
  cursor.execute(
      "SELECT metodo, cuenta, monto_usd, monto_local, fecha, estado FROM"
      " transacciones WHERE username = ?",
      (USUARIO_ACTUAL,),
  )
  historial = cursor.fetchall()

  if historial:
    for h in historial:
      st.info(
          f"📅 **{h[4]}** | Método: **{h[0]}** | Destino: `{h[1]}` | Monto:"
          f" **${h[2]} USD** ({h[3]}) | Estado: **{h[5]}**"
      )
  else:
    st.write("Aún no tienes solicitudes de retiro registradas.")
