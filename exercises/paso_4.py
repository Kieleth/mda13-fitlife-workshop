# ============================================================
# PASO 4 — Habla con la app
# ============================================================
#
# ── ¿Qué es un chat en Streamlit? ──────────────────────────
#
# Streamlit tiene componentes para crear una interfaz de chat,
# como la de WhatsApp o ChatGPT. Tres piezas:
#
#   st.chat_input("texto")        -> Campo de texto donde el
#                                    usuario escribe. Devuelve
#                                    el mensaje o None si no
#                                    ha escrito nada.
#
#   st.chat_message("user")       -> Bocadillo con icono de
#                                    usuario.
#
#   st.chat_message("assistant")  -> Bocadillo con icono de
#                                    asistente.
#
# ── ¿Qué es "with"? ────────────────────────────────────────
#
# En Python, "with" seguido de dos puntos significa: todo lo
# que va indentado (con espacios) debajo pertenece a este
# bloque. Es como decir "esto va dentro de este contenedor":
#
#   with st.chat_message("user"):
#       st.write("hola")     ← aparece dentro del bocadillo
#       st.write("adiós")    ← también dentro del bocadillo
#
#   st.write("fuera")        ← esto ya NO está en el bocadillo
#
# VS Code indenta automáticamente cuando pulsáis Enter después
# de una línea que termina en ":"
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa el bloque del final para que cuando el usuario
# escriba algo, la app lo repita como un eco.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Cambia el eco para que responda en mayúsculas:
#        st.write(f"HAS DICHO: {prompt.upper()}")
#      .upper() convierte texto a mayúsculas. ¿Qué otros
#      métodos tiene un string? Prueba .lower(), .title(),
#      len(prompt), prompt[::-1] (lo invierte).
#
#   B. Haz que el asistente responda con la longitud:
#        st.write(f"Tu mensaje tiene {len(prompt)} caracteres.")
#
#   C. Añade un tercer bocadillo después del asistente:
#        with st.chat_message("user", avatar="🤔"):
#            st.write("¿Algo más?")
#      El parámetro avatar cambia el icono. Prueba con otros.
#
# Ejecuta:  streamlit run exercises/paso_4.py
# ============================================================

import streamlit as st
import pandas as pd

st.title("FitLife Dashboard")

df_members = pd.read_csv("data/fitlife_members.csv")
df_context = pd.read_csv("data/fitlife_context.csv")

st.subheader("Datos cargados")
st.write(f"Socios: **{len(df_members)}** registros")
st.write(f"Contexto: **{len(df_context)}** meses")

st.divider()

# --- RETO: completa el chat ---

prompt = st.chat_input("Escribe algo...")

if prompt:
    # 1. Muestra lo que escribió el usuario
    with st.chat_message("user"):
        st.write(prompt)

    # 2. Muestra una respuesta del "asistente" (por ahora, un eco)
    #    ↓ Borra ___ y escribe: st.write(f"Has dicho: {prompt}")
    #    Importante: debe ir indentado (con espacios) dentro del with
    with st.chat_message("assistant"):
        st.write(f"Has dicho: {prompt}")
