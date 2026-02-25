# ============================================================
# PASO 0 — Arranca la app
# ============================================================
#
# ── ¿Qué es Streamlit? ─────────────────────────────────────
#
# Streamlit es una librería de Python que convierte código en
# una página web. Una línea de Python = un elemento en la
# página. Sin HTML, sin CSS, sin complicaciones.
#
# Pensad en ello así: si sabéis escribir print("hola"), sabéis
# hacer una web con Streamlit. En vez de print, usáis st.write.
#
# Cada vez que guardáis el archivo, la web se actualiza sola.
# No tenéis que parar y arrancar nada.
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Hacer que esta app funcione. Tiene un error.
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
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Prueba a cambiar el texto del título y del st.write.
#      Guarda y mira cómo se actualiza la web al instante.
#
#   B. Añade una línea nueva al final del archivo:
#        st.balloons()
#      ¿Qué pasa? Prueba también: st.snow()
#
#   C. Añade:
#        st.slider("Tu edad", 0, 100, 25)
#      Aparece un slider interactivo en la web. Streamlit
#      tiene decenas de componentes así. Los iremos viendo.
#
# Ejecuta:  streamlit run exercises/paso_0.py
# ============================================================

import streamlt as st

st.title("Hola Mundo")
st.write("Si ves esto en el navegador, tu primer app web funciona.")
