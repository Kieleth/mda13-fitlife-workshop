# ============================================================
# PASO 5 — Conecta el cerebro
# ============================================================
#
# Hasta ahora la app solo repite lo que escribes. Vamos a
# conectar un LLM (Large Language Model) para que responda
# de verdad.
#
# Un LLM es un modelo de inteligencia artificial entrenado
# para entender y generar texto. Lo usaremos a través de la
# API de OpenAI — una puerta de entrada que nos permite
# enviarle texto y recibir una respuesta.
#
# Para usarlo necesitas dos cosas:
#
#   1. Una API key (una contraseña que te identifica).
#      El profesor te la dará.
#
#   2. Un archivo .env en la raíz del proyecto con:
#      OPENAI_API_KEY=la-clave-que-te-de-el-profesor
#
# Tu reto: completa la línea marcada con ___ para crear el
# cliente de OpenAI. Es solo: OpenAI()
#
# Ejecuta:  streamlit run exercises/paso_5.py
# ============================================================

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = ___  # Crea el cliente: OpenAI()

st.title("FitLife Dashboard")

prompt = st.chat_input("Pregunta lo que quieras...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
