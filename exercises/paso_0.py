# ============================================================
# PASO 0 — Arranca la app
# ============================================================
#
# Tu primer reto: hacer que esta app funcione.
#
# 1. Abre la terminal en VS Code:
#    - Mac:  Ctrl + `  (la tecla al lado del 1)
#    - También: menú Terminal → Nuevo terminal
#
# 2. Asegúrate de que el entorno está activo. Deberías ver
#    (mda13) al principio de la línea. Si no lo ves, escribe:
#
#      conda activate mda13
#
# 3. Ejecuta:
#
#      streamlit run exercises/paso_0.py
#
#    Se abrirá una pestaña en tu navegador automáticamente.
#    Si no se abre, busca en la terminal una línea que diga
#    "Local URL: http://localhost:8501" y ábrela tú.
#
# 4. Verás un error en la terminal (texto rojo). Léelo con
#    calma — el error te dice qué está mal y en qué línea.
#
#    Si ves "ModuleNotFoundError", vas por buen camino.
#    Fíjate en el nombre del módulo que intenta importar.
#    ¿Está bien escrito?
#
# 5. Arregla el error en el código, guarda el archivo (Ctrl+S
#    o Cmd+S), y Streamlit recargará la app automáticamente.
#
# Cuando veas el mensaje en el navegador, has completado el paso.
# ============================================================

import streamlt as st

st.title("Hola Mundo")
st.write("Si ves esto en el navegador, tu primer app web funciona.")
