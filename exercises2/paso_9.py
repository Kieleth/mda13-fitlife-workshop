# ============================================================
# PASO 9 — Ejecuta el código generado
# ============================================================
#
# ── ¿Qué hicimos en paso_8? ────────────────────────────────
#
# Cambiamos el prompt para que el LLM genere código Python en
# vez de responder con texto. El LLM devuelve algo como:
#
#   ```python
#   churned = df_members[df_members["status"] == "churned"]
#   resultado = len(churned) / len(df_members) * 100
#   ```
#
# Pero solo lo mostramos en pantalla. No lo ejecutamos.
#
# ── ¿Cómo ejecutamos código generado? ──────────────────────
#
# Python tiene una función llamada exec() que ejecuta texto
# como si fuera código:
#
#   codigo = "x = 2 + 3"
#   exec(codigo)          # ahora x vale 5
#
# Pero hay un truco: exec() ejecuta el código en un "espacio"
# separado. Para acceder al resultado, necesitamos pasarle un
# diccionario donde guardar las variables:
#
#   espacio = {"df_members": df_members}  # le damos acceso al df
#   exec(codigo, espacio)
#   print(espacio["resultado"])  # leemos la variable "resultado"
#
# ── ¿Cómo extraemos el código de la respuesta del LLM? ────
#
# El LLM envuelve el código en un bloque Markdown:
#
#   ```python
#   ... código aquí ...
#   ```
#
# Necesitamos extraer solo lo que hay entre los backticks.
# Para eso usamos una expresión regular (regex):
#
#   import re
#   match = re.search(r"```(?:python)?\n(.*?)```", texto, re.DOTALL)
#   codigo = match.group(1)
#
# No te preocupes por entender la regex — es una receta.
# Lo importante: toma la respuesta del LLM y extrae el código.
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa las dos líneas marcadas con ___ :
#
#   1. Extraer el código de la respuesta del LLM (regex)
#   2. Ejecutar el código con exec()
#
# Cuando funcione, prueba las 5 preguntas del paso_6.
# Ahora las respuestas serán REALES — calculadas sobre
# las 16.334 filas de verdad.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Compara las respuestas con las del paso_6 (sesión 1).
#      ¿Cuáles eran inventadas? ¿Cuáles ahora son correctas?
#
#   B. Prueba preguntas más complejas:
#        "¿Cuál es el margen medio por plan?"
#        "¿Qué canal de captación trae socios más fieles?"
#        "¿En qué mes hubo más bajas?"
#
#   C. Prueba una pregunta que haga fallar el código:
#        "Dibuja un gráfico de barras del churn por centro"
#      ¿Qué pasa? ¿Qué error da?
#
#   D. Fíjate en el código generado. ¿Tiene sentido?
#      ¿Lo habrías escrito igual? ¿Ves algún error lógico?
#
# Ejecuta:  streamlit run exercises2/paso_9.py
# ============================================================

import streamlit as st
import pandas as pd
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.title("FitLife — Text-to-Code")
st.caption("Paso 9 — Ejecuta el código y obtén números reales")

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

        system_prompt = f"""Genera solo código Python/pandas que responda a la pregunta del usuario.

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

        # ── PASO A: extraer el código del bloque Markdown ───
        # El LLM devuelve algo como: ```python\n...código...\n```
        # Necesitamos sacar solo el código de dentro.
        #
        # ↓ Borra ___ y escribe:
        #   re.search(r"```(?:python)?\n(.*?)```", generated, re.DOTALL)

        match = ___

        if match:
            code = match.group(1)

            # Mostrar el código generado
            st.write("**Código generado:**")
            st.code(code, language="python")

            # ── PASO B: ejecutar el código ──────────────────
            # exec() ejecuta texto como código Python.
            # Le pasamos un diccionario con los DataFrames para
            # que el código pueda acceder a ellos.
            #
            # ↓ Borra ___ y escribe:
            #   exec(code, exec_globals)

            exec_globals = {
                "df_members": df_members,
                "df_context": df_context,
                "pd": pd,
            }

            ___

            # Mostrar el resultado
            if "resultado" in exec_globals:
                st.write("**Resultado:**")
                st.write(exec_globals["resultado"])
            else:
                st.warning("El código se ejecutó pero no definió la variable 'resultado'.")
        else:
            st.warning("No se pudo extraer código de la respuesta del LLM.")
            st.code(generated)
