# ============================================================
# PASO 6 — Pregúntale sobre los datos
# ============================================================
#
# ── ¿Qué pasa cuando un LLM habla de datos que no ha visto?
#
# En paso_5 el LLM respondía bien a preguntas generales:
# historia, matemáticas, código. Pero esos son temas que
# estaban en su entrenamiento (todo internet).
#
# FitLife es un caso inventado. El LLM nunca ha visto estos
# datos. Si le preguntas "¿cuántos socios tiene FitLife?"
# sin darle ningún contexto, se inventará un número.
#
# En este paso le pasamos algo de contexto: una muestra de
# 5 filas y los nombres de las columnas. Así "sabe" de qué
# estamos hablando. ¿Es suficiente?
#
# ── Tu reto ─────────────────────────────────────────────────
#
# ESTE PASO NO TIENE NADA ROTO. Funciona tal cual.
#
# Tu misión es de detective: prueba estas 5 preguntas y anota
# para cada una si la respuesta es correcta o inventada.
#
#   1. ¿Cuántos registros tiene el dataset de socios?
#   2. ¿Qué planes ofrece FitLife?
#   3. ¿Cuál es el centro con más socios?
#   4. ¿Cuál es la tasa de churn del plan básico?
#   5. ¿Debería FitLife bajar el precio del plan básico?
#
# ── Anota tus resultados ────────────────────────────────────
#
#   Pregunta 1 (registros):  ¿Correcto?       ¿Qué dijo?
#   Pregunta 2 (planes):     ¿Correcto?       ¿Qué dijo?
#   Pregunta 3 (centro):     ¿Correcto?       ¿Qué dijo?
#   Pregunta 4 (churn):      ¿Correcto?       ¿Qué dijo?
#   Pregunta 5 (precio):     ¿Correcto?       ¿Qué dijo?
#
# Pista: en paso_3 viste los datos reales con st.dataframe().
# Puedes volver a ejecutar paso_3 para comprobar las respuestas
# del LLM contra los datos de verdad.
#
# Cuando termines, comparte tus resultados en el chat de clase.
#
# ── Pregunta para pensar ────────────────────────────────────
#
# Fíjate en el código de abajo, en la variable "context".
# ¿Qué datos le estamos pasando realmente al LLM?
# ¿Cuántas filas ve de 16.334? ¿Es suficiente para calcular
# una tasa de churn o decidir si bajar precios?
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Haz la pregunta 4 (tasa de churn) tres veces seguidas.
#      ¿Da el mismo número? Si cambia cada vez, es que no lo
#      está calculando — se lo está inventando.
#
#   B. Prueba una pregunta que SÍ pueda responder bien:
#        "Describe las columnas del dataset de socios"
#      ¿Por qué esta sí funciona y las numéricas no?
#
#   C. Prueba a preguntarle algo que no está en los datos:
#        "¿Cuál es el NPS de FitLife?"
#      ¿Dice que no lo sabe o se inventa un número?
#
#   D. Mira la línea 89: head(). Eso muestra solo 5 filas.
#      ¿Qué pasaría si cambias head() por head(50)?
#      ¿Mejorarían las respuestas? ¿Y head(1000)?
#      ¿Dónde está el límite? (No hace falta probarlo —
#      solo pensadlo. Lo exploraremos en el paso 7.)
#
# Ejecuta:  streamlit run exercises/paso_6.py
# ============================================================

import streamlit as st
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.title("FitLife Dashboard")

df_members = pd.read_csv("data/fitlife_members.csv")
df_context = pd.read_csv("data/fitlife_context.csv")

st.subheader("Datos cargados")
st.write(f"Socios: **{len(df_members)}** registros | Contexto: **{len(df_context)}** meses")

st.divider()

prompt = st.chat_input("Pregunta sobre los datos de FitLife...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        context = f"""Eres un analista de datos. Tienes acceso a datos de FitLife,
una red de gimnasios.

Dataset 1 - Socios (muestra de 5 filas de {len(df_members)} totales):
{df_members.head().to_string()}

Columnas: {list(df_members.columns)}

Dataset 2 - Contexto mensual (muestra de 5 filas de {len(df_context)} totales):
{df_context.head().to_string()}

Columnas: {list(df_context.columns)}"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
