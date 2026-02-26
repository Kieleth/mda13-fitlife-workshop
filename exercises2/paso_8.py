# ============================================================
# PASO 8 — Haz que escriba código
# ============================================================
#
# ── ¿Qué aprendimos en la sesión 1? ────────────────────────
#
# El LLM entiende las preguntas perfectamente, pero no puede
# calcular sobre 16.334 filas. Cuando le pides "¿cuál es la
# tasa de churn del plan básico?", se inventa un número.
#
# ── La idea clave de la sesión 2 ────────────────────────────
#
# ¿Y si en vez de pedirle LA RESPUESTA, le pedimos que
# escriba EL CÓDIGO para calcularla?
#
#   Antes (sesión 1):
#     Usuario: "¿Cuál es la tasa de churn?"
#     LLM:     "La tasa de churn es del 12.3%" ← inventado
#
#   Ahora (sesión 2):
#     Usuario: "¿Cuál es la tasa de churn?"
#     LLM:     "churned = df[df['status']=='churned']
#               tasa = len(churned)/len(df)*100"  ← código real
#     Python:  ejecuta el código → 2.52%  ← resultado real
#
# Esto se llama "text-to-code": el LLM traduce lenguaje
# natural a código Python. Python calcula. El número es real.
#
# ── El cambio está en el prompt ─────────────────────────────
#
# En paso_6, el prompt del sistema decía:
#   "Eres un analista de datos. Responde a las preguntas..."
#
# Ahora le vamos a decir:
#   "Genera SOLO código Python que responda a la pregunta.
#    No expliques nada. Solo el código."
#
# Eso es todo. El mismo LLM, la misma API, pero con una
# instrucción diferente.
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa la línea marcada con ___ en el prompt del sistema.
# Necesitas decirle al LLM que genere código Python, no texto.
#
# Cuando funcione, prueba preguntas como:
#   "¿Cuántos registros tiene el dataset?"
#   "¿Cuántos socios de cada plan hay?"
#   "¿Cuál es la tasa de churn del plan básico?"
#
# Verás que el LLM responde con CÓDIGO en vez de con texto.
# En el siguiente paso aprenderemos a ejecutar ese código.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Prueba la misma pregunta que en paso_6:
#        "¿Cuál es la tasa de churn del plan básico?"
#      ¿El código que genera tiene sentido? ¿Lo entiendes?
#
#   B. Prueba una pregunta más compleja:
#        "¿Cuál es el margen medio por plan?"
#      ¿Genera código correcto? ¿Usa las columnas correctas?
#
#   C. Prueba en inglés vs español. ¿Genera mejor código
#      con preguntas en un idioma u otro?
#
#   D. Pregunta algo que NO se puede responder con los datos:
#        "¿Cuál es la satisfacción media de los socios?"
#      ¿Qué hace? ¿Genera código que falla? ¿Inventa una
#      columna que no existe?
#
# Ejecuta:  streamlit run exercises2/paso_8.py
# ============================================================

import streamlit as st
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.title("FitLife — Text-to-Code")
st.caption("Paso 8 — El LLM genera código en vez de responder")

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

        # ── PROMPT DEL SISTEMA ──────────────────────────────
        # La instrucción clave está en la primera línea.
        # Completa el ___ para que el LLM genere código Python
        # en vez de responder con texto.
        #
        # Pista: necesitas decirle algo como
        #   "Genera solo código Python que responda..."
        #   o "Escribe únicamente código Python..."

        system_prompt = f"""___

Tienes acceso a dos DataFrames ya cargados:

1. df_members — datos de socios ({len(df_members)} filas)
   Columnas: {list(df_members.columns)}

2. df_context — contexto mensual ({len(df_context)} filas)
   Columnas: {list(df_context.columns)}

Reglas:
- Usa pandas para las operaciones.
- El código debe terminar con: resultado = <lo que calcules>
- NO uses print(). Solo asigna el resultado final a la variable "resultado".
- NO incluyas import ni read_csv — los datos ya están cargados.
- Devuelve SOLO el bloque de código, sin explicaciones antes ni después.
- Envuelve el código en triple backtick python."""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        generated = response.choices[0].message.content
        st.write("**Código generado por el LLM:**")
        st.code(generated, language="python")
        st.write("👆 De momento solo lo muestra. En el paso 9 lo ejecutaremos.")
