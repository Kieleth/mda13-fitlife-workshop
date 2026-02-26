# ============================================================
# PASO 11 — Autocorrección  (Bonus)
# ============================================================
#
# ── ¿Qué pasa cuando el código falla? ──────────────────────
#
# En paso_10 mostramos el error al usuario. Pero podemos
# hacer algo mejor: enviarle el error de vuelta al LLM y
# pedirle que corrija el código.
#
# Es como decirle a un programador: "tu código falló con
# este error, arréglalo". El LLM ve el error, entiende qué
# salió mal, y genera una versión corregida.
#
# El flujo:
#
#   Intento 1: LLM genera código → falla con error X
#   Intento 2: "El código falló con: X. Corrígelo." → nuevo código
#   Intento 3: (si vuelve a fallar) → tercer intento
#   Después de 3 intentos: mostramos el error final
#
# ── ¿Qué es un bucle for? ──────────────────────────────────
#
# Un bucle for repite algo un número fijo de veces:
#
#   for intento in range(3):       # repite 3 veces
#       print(f"Intento {intento}")  # 0, 1, 2
#
# range(3) genera: 0, 1, 2. Así controlamos cuántos intentos
# permitimos antes de rendirse.
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Este paso NO tiene blancos ___. Funciona tal cual.
# Tu misión:
#
#   1. Léelo y entiende cómo funciona el bucle de reintentos.
#   2. Prueba preguntas que generen errores y observa cómo
#      el LLM se autocorrige:
#        "¿Cuál es la satisfacción media de los socios?"
#        "¿Cuántos socios se dieron de alta en fin de semana?"
#   3. Prueba preguntas que funcionen a la primera:
#        "¿Cuántos socios hay por plan?"
#        "¿Cuál es la tasa de churn del plan básico?"
#
# ── Preguntas para pensar ───────────────────────────────────
#
#   - ¿Cuántos reintentos son razonables? ¿Por qué no 10?
#   - ¿Hay errores que NUNCA se van a corregir aunque le des
#     más intentos? (Ejemplo: pedir una columna que no existe
#     y que el LLM no sabe que no existe.)
#   - ¿Cada reintento cuesta dinero (tokens). ¿Merece la pena?
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Cambia MAX_RETRIES a 1. ¿Cuántas preguntas más fallan?
#
#   B. Añade al prompt del sistema información sobre los
#      valores posibles de cada columna (como hicimos en
#      paso_7 con las distribuciones). ¿Reduce los errores
#      de "columna no encontrada"?
#
#   C. Prueba a añadir ejemplos al prompt del sistema:
#        "Ejemplo: para calcular la tasa de churn, usa:
#         churned = len(df_members[df_members['status']=='churned'])
#         total = len(df_members)
#         resultado = churned / total * 100"
#      ¿Mejora la calidad del código generado?
#
#   D. Piensa: ¿cómo harías para que el sistema detecte si
#      el resultado "tiene sentido"? (Por ejemplo: una tasa
#      de churn del 500% claramente está mal.)
#
# Ejecuta:  streamlit run exercises2/paso_11.py
# ============================================================

import streamlit as st
import pandas as pd
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.title("FitLife — Text-to-Code")
st.caption("Paso 11 — Autocorrección con reintentos")

df_members = pd.read_csv("data/fitlife_members.csv")
df_context = pd.read_csv("data/fitlife_context.csv")

st.subheader("Datos cargados")
st.write(f"Socios: **{len(df_members)}** registros | Contexto: **{len(df_context)}** meses")

st.divider()

# ── Configuración ───────────────────────────────────────────
MAX_RETRIES = 3  # número máximo de intentos


def extract_code(text):
    """Extrae el código Python de un bloque Markdown."""
    match = re.search(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    return match.group(1) if match else None


def run_code(code, df_members, df_context):
    """Ejecuta código y devuelve (resultado, error)."""
    exec_globals = {
        "df_members": df_members,
        "df_context": df_context,
        "pd": pd,
    }
    try:
        exec(code, exec_globals)
        if "resultado" in exec_globals:
            return exec_globals["resultado"], None
        else:
            return None, "El código no definió la variable 'resultado'."
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


# ── Prompt del sistema ──────────────────────────────────────
SYSTEM_PROMPT = f"""Genera solo código Python/pandas que responda a la pregunta del usuario.

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


# ── Chat ────────────────────────────────────────────────────

prompt = st.chat_input("Pregunta sobre los datos de FitLife...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]

        resultado = None
        last_error = None
        last_code = None

        # ── Bucle de reintentos ─────────────────────────────
        for intento in range(MAX_RETRIES):

            # 1. Pedir código al LLM
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
            )
            generated = response.choices[0].message.content

            # 2. Extraer el código
            code = extract_code(generated)
            if not code:
                last_error = "No se pudo extraer código de la respuesta."
                last_code = generated
                break

            last_code = code

            # 3. Ejecutar
            resultado, error = run_code(code, df_members, df_context)

            if error is None:
                # ¡Éxito!
                break
            else:
                last_error = error
                # 4. Enviar el error al LLM para que corrija
                messages.append({"role": "assistant", "content": generated})
                messages.append({
                    "role": "user",
                    "content": f"El código falló con este error:\n{error}\n\nCorrige el código.",
                })
                if intento < MAX_RETRIES - 1:
                    st.info(f"Intento {intento + 1} falló: {error}. Pidiendo corrección...")

        # ── Mostrar resultado ───────────────────────────────
        if resultado is not None:
            st.write("**Resultado:**")
            st.write(resultado)
        else:
            st.error(f"No se pudo obtener un resultado después de {MAX_RETRIES} intentos.")
            if last_error:
                st.write(f"Último error: `{last_error}`")

        # ── Código y detalles (siempre disponibles) ─────────
        if last_code:
            with st.expander("Ver código generado"):
                st.code(last_code, language="python")
