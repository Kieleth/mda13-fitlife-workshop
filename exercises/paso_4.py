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
    with st.chat_message("assistant"):
        ___  # Escribe aquí: st.write(f"Has dicho: {prompt}")
