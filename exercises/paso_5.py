# ============================================================
# PASO 5 — Conecta el cerebro
# ============================================================
#
# ── ¿Qué es un LLM? ────────────────────────────────────────
#
# Un LLM (Large Language Model) es un programa que ha leído
# cantidades absurdas de texto: miles de millones de páginas
# web, libros, artículos, código. De todo eso ha aprendido
# patrones de lenguaje.
#
# Cuando le hacéis una pregunta, no busca la respuesta en
# ningún sitio. Genera texto palabra por palabra basándose en
# los patrones que aprendió. Es como un compañero que ha leído
# todo internet, tiene una memoria impresionante para el
# lenguaje, pero no tiene calculadora.
#
# Retened eso: no tiene calculadora. Es importante después.
#
# ── ¿Qué es una API? ───────────────────────────────────────
#
# Una API es una puerta de entrada. Vosotros enviáis un mensaje
# de texto a través de internet, OpenAI lo recibe, se lo pasa
# al modelo, el modelo genera una respuesta, y os la devuelve.
# Todo en 2-3 segundos.
#
#   Tu app → mensaje → API de OpenAI → modelo → respuesta → tu app
#
# ── ¿Qué es una API key? ───────────────────────────────────
#
# Una contraseña que os identifica. Cada petición cuesta dinero
# (fracciones de céntimo), así que OpenAI necesita saber quién
# pide qué. El profesor os da una clave para el taller — no la
# compartáis fuera de clase.
#
# ── Cómo crear el archivo .env ──────────────────────────────
#
# La API key no va en el código (si lo subierais a internet,
# todo el mundo la vería). Va en un archivo separado llamado
# .env que el código lee automáticamente.
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
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Prueba preguntas de distintos tipos:
#      - Conocimiento: "¿Quién escribió El Quijote?"
#      - Matemáticas: "¿Cuánto es 347 × 28?"
#      - Código: "Escribe una función en Python que sume dos números"
#      - Creatividad: "Escribe un haiku sobre datos"
#      ¿En cuáles responde mejor? ¿En cuáles peor?
#
#   B. Prueba a preguntarle en inglés y en español la misma
#      cosa. ¿Cambia la calidad de la respuesta?
#
#   C. Prueba: "¿Qué sabes sobre FitLife, una red de gimnasios?"
#      ¿Sabe algo? ¿Se lo inventa? ¿Cómo lo sabrías?
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
