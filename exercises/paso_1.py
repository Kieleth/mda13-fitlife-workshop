# ============================================================
# PASO 1 — Muestra información en pantalla
# ============================================================
#
# ── ¿Cómo funciona Streamlit? ──────────────────────────────
#
# Cada función st.algo() pone un elemento en la página web.
# El orden importa: lo que va primero en el código aparece
# primero en la página.
#
#   st.title("...")       ->  título grande
#   st.subheader("...")   ->  subtítulo
#   st.write("...")       ->  texto normal (acepta Markdown)
#
# Markdown es un formato sencillo para dar estilo al texto:
#   **negrita**   *cursiva*   `código`
#
# Por ejemplo: st.write("Esto es **importante** y esto *no*")
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa las líneas marcadas con ___ para que la app
# muestre un título, un subtítulo y un texto descriptivo.
#
# ¿Cómo? Borra la línea entera que dice ___ y escribe en su
# lugar la función completa. Por ejemplo, si el comentario dice
# "Ejemplo: st.subheader(...)", escribe exactamente eso.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Prueba st.markdown() — funciona igual que st.write()
#      pero es más explícito:
#        st.markdown("## Esto es un subtítulo en Markdown")
#        st.markdown("Lista:\n- Uno\n- Dos\n- Tres")
#
#   B. Prueba a mostrar un número importante con estilo:
#        st.metric("Socios totales", "16.334", "+2.1%")
#      Esto crea una tarjeta con el número grande y un delta.
#
#   C. Prueba st.divider() — pone una línea horizontal para
#      separar secciones visualmente.
#
# Ejecuta:  streamlit run exercises/paso_1.py
# ============================================================

import streamlit as st

st.title("FitLife Dashboard")

# ↓ Borra esta línea entera y escribe: st.subheader("Análisis de socios")
___

# ↓ Borra esta línea entera y escribe: st.write("Bienvenido al panel de control de FitLife.")
___
