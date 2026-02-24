# ============================================================
# PASO 4 — Habla con la app
# ============================================================
#
# Streamlit tiene componentes para crear un chat:
#
#   st.chat_input("texto")     ->  campo de texto donde el
#                                   usuario escribe. Devuelve
#                                   el mensaje o None si no
#                                   ha escrito nada.
#
#   st.chat_message("user")    ->  bloque visual con icono de
#                                   usuario. Usa with: ... para
#                                   poner contenido dentro.
#
#   st.chat_message("assistant") -> igual, pero con icono de
#                                   asistente.
#
# ¿Qué es "with"?
#
#   with st.chat_message("user"):
#       st.write("hola")        ← esto aparece dentro del bocadillo
#
#   Todo lo que va indentado (con espacios) debajo de "with"
#   se muestra dentro de ese bloque de chat. Es como decir:
#   "todo esto va dentro del bocadillo del usuario/asistente".
#
#   VS Code indenta automáticamente cuando pulsas Enter después
#   de una línea que termina en ":"
#
# Tu reto: completa el bloque del final para que cuando el
# usuario escriba algo, la app lo repita como un eco.
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
        ___
