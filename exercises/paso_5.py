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
#      El profesor la compartirá por el chat de clase.
#
#   2. Un archivo .env en la raíz del proyecto.
#
# ── Cómo crear el archivo .env ──────────────────────────────
#
#   1. En VS Code, ve al explorador de archivos (panel izquierdo)
#   2. Haz clic derecho en la carpeta raíz del proyecto
#      (mda13-fitlife-workshop)
#   3. Selecciona "New File" (Nuevo archivo)
#   4. Escribe exactamente:  .env
#      (sí, empieza con un punto, sin extensión)
#   5. Dentro del archivo, escribe esta línea:
#      OPENAI_API_KEY=aquí-pega-la-clave-del-profesor
#   6. Guarda el archivo: Ctrl+S (Windows) o Cmd+S (Mac)
#
#   ¿No ves el archivo en el explorador? A veces VS Code
#   oculta archivos que empiezan con punto. Ve a Archivo →
#   Preferencias → Configuración, busca "files.exclude" y
#   asegúrate de que .env no esté excluido.
#
# ── Errores comunes ─────────────────────────────────────────
#
#   "AuthenticationError" o "Incorrect API key"
#     → Revisa que la clave en .env esté bien copiada,
#       sin espacios extra al principio o final.
#
#   "No module named 'openai'"
#     → Ejecuta en la terminal: pip install openai
#
#   "No module named 'dotenv'"
#     → Ejecuta en la terminal: pip install python-dotenv
#
#   "RateLimitError"
#     → Has hecho muchas peticiones seguidas. Espera unos
#       segundos y prueba otra vez.
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa la línea marcada con ___ para crear el cliente
# de OpenAI. Es solo una palabra: OpenAI()
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
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
