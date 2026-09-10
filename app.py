import os
import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="ZafiroX - Web Real", page_icon="💎", layout="wide"
)

# Leer el archivo index.html que subiste al repositorio
html_file_path = "Index.html"

if os.path.exists(html_file_path):
  with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

  # Renderizar la aplicación web HTML5 dentro de Streamlit con altura adaptable
  components.html(html_code, height=850, scrolling=True)
else:
  st.error(
      "No se encontró el archivo Index.html en el repositorio. Por favor"
      " verifícalo."
  )
