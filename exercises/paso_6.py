# ============================================================
# PASO 6 — Pregúntale sobre los datos
# ============================================================
#
# El LLM funciona, pero no sabe nada de FitLife. Si le
# preguntas "¿cuántos socios tiene FitLife?" se inventará
# un número.
#
# En este paso le pasamos los datos como contexto: le
# describimos los datasets en el mensaje para que "sepa"
# de qué estamos hablando.
#
# ESTE PASO NO TIENE NADA ROTO. Funciona tal cual.
#
# Tu reto es otro: prueba estas preguntas y anota para
# cada una si la respuesta es correcta o inventada.
#
#   1. ¿Cuántos registros tiene el dataset de socios?
#   2. ¿Qué planes ofrece FitLife?
#   3. ¿Cuál es el centro con más socios?
#   4. ¿Cuál es la tasa de churn del plan básico?
#   5. ¿Debería FitLife bajar el precio del plan básico?
#
# Pregunta:  ¿funciona bien? ¿qué falla? ¿por qué crees
#            que falla?
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
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
