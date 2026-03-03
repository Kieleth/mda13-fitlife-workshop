# ============================================================
# PASO 13 — El analista explica
# ============================================================
#
# ── ¿Qué tenemos hasta ahora? ──────────────────────────────
#
# Un chat con memoria que genera código, lo ejecuta, y muestra
# el resultado. Si preguntas "¿Cuál es la tasa de churn del
# plan básico?" ves algo como:
#
#   0.0685267857142857
#
# Es correcto. Pero no es muy útil. Un analista humano no te
# diría solo "0.068". Te diría:
#
#   "La tasa de churn del plan básico es del 6.85%, casi el
#    doble que la del plan premium (3.2%). Esto sugiere que
#    los socios del plan más económico son más sensibles al
#    precio del competidor low-cost."
#
# ── La idea: dos pasadas ───────────────────────────────────
#
# Vamos a hacer DOS llamadas al LLM:
#
#   Pasada 1: "Genera código para calcular X"
#             → código → exec() → resultado numérico
#
#   Pasada 2: "El usuario preguntó X. El resultado calculado
#              es Y. Explica qué significa en el contexto del
#              negocio de FitLife."
#             → interpretación en lenguaje natural
#
# La primera pasada es la calculadora (ya la tenemos).
# La segunda es el analista (lo nuevo de este paso).
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa las dos líneas marcadas con ___ :
#
#   1. El prompt de interpretación (qué le pedimos al LLM)
#   2. La llamada a la API para obtener la interpretación
#
# Cuando funcione, prueba:
#   "¿Cuál es la tasa de churn del plan básico?"
#
# Ahora deberías ver el número Y una explicación en contexto.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Compara las interpretaciones de estas preguntas:
#        "¿Cuál es el margen medio por plan?"
#        "¿Los socios con app tienen menos churn?"
#        "¿Qué canal de captación trae socios más fieles?"
#      ¿Las explicaciones son útiles? ¿Añaden contexto real?
#
#   B. Prueba una pregunta donde el resultado sea un DataFrame
#      grande (como "Muestra el churn por centro y plan").
#      ¿La interpretación resume bien una tabla compleja?
#
#   C. Prueba a cambiar el tono del prompt de interpretación.
#      En vez de "analista de datos", pon "consultor senior
#      de McKinsey". ¿Cambia la calidad de la explicación?
#
# Ejecuta:  streamlit run exercises3/paso_13.py
# ============================================================

import streamlit as st
import pandas as pd
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
MODEL = "gpt-4.1-mini"
MAX_RETRIES = 3

# ── Datos ───────────────────────────────────────────────────

@st.cache_data
def load_data():
    members = pd.read_csv("data/fitlife_members.csv")
    context = pd.read_csv("data/fitlife_context.csv")
    return members, context

df_members, df_context = load_data()

# ── Funciones auxiliares ────────────────────────────────────

def extract_code(text):
    """Extrae código Python de un bloque Markdown."""
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


# ── Prompt del sistema (generación de código) ──────────────

SYSTEM_PROMPT = f"""Genera solo código Python/pandas que responda a la pregunta del usuario.

Tienes acceso a dos DataFrames ya cargados:

1. df_members — datos de socios ({len(df_members)} filas)
   Columnas: {list(df_members.columns)}
   Valores de 'plan': basic (29€), premium (49€), family (69€)
   Valores de 'center': downtown, northside, eastpark, westfield, southgate
   Valores de 'status': active, churned
   Valores de 'churn_reason': price, competitor, no_use, relocation, personal (null si activo)
   Valores de 'acquisition_channel': walk_in, referral, digital, january_campaign, corporate

2. df_context — contexto mensual ({len(df_context)} filas)
   Columnas: {list(df_context.columns)}

Reglas:
- Usa pandas para las operaciones.
- El código debe terminar con: resultado = <lo que calcules>
- NO uses print(). Solo asigna el resultado final a la variable "resultado".
- NO incluyas import ni read_csv — los datos ya están cargados.
- Devuelve SOLO el bloque de código, sin explicaciones antes ni después.
- Envuelve el código en triple backtick python.
- Si la pregunta requiere cruzar las dos tablas, usa df_members.merge(df_context, on="month").
- Para calcular tasa de churn: churned / total * 100."""

# ── Interfaz ────────────────────────────────────────────────

st.title("FitLife Analytics")
st.caption(f"Paso 13 — El analista explica · {len(df_members):,} registros")

col1, col2 = st.columns([3, 1])
with col1:
    st.write(f"Socios: **{len(df_members):,}** | Contexto: **{len(df_context)}** meses")
with col2:
    show_code = st.toggle("Mostrar código", value=False)

st.divider()

# ── Historial ───────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("code") and show_code:
            with st.expander("Código ejecutado"):
                st.code(msg["code"], language="python")

# ── Chat ────────────────────────────────────────────────────

if prompt := st.chat_input("Pregunta sobre los datos de FitLife..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generando y ejecutando código..."):

            # ── Pasada 1: generar y ejecutar código ─────────
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]

            resultado = None
            last_error = None
            last_code = None

            for intento in range(MAX_RETRIES):
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                )
                generated = response.choices[0].message.content
                code = extract_code(generated)

                if not code:
                    last_error = "No se pudo extraer código de la respuesta."
                    last_code = generated
                    break

                last_code = code
                resultado, error = run_code(code, df_members, df_context)

                if error is None:
                    break
                else:
                    last_error = error
                    messages.append({"role": "assistant", "content": generated})
                    messages.append({
                        "role": "user",
                        "content": f"El código falló con este error:\n{error}\n\nCorrige el código.",
                    })
                    if intento < MAX_RETRIES - 1:
                        st.info(f"Intento {intento + 1} falló: {error}. Reintentando...")

        # ── Pasada 2: interpretar el resultado ──────────────
        if resultado is not None:
            if show_code and last_code:
                with st.expander("Código ejecutado"):
                    st.code(last_code, language="python")

            with st.spinner("Interpretando..."):

                # ── PASO A: construir el prompt de interpretación
                # Le damos al LLM la pregunta original, el resultado
                # calculado, y le pedimos que explique.
                #
                # ↓ Borra ___ y escribe el prompt. Ejemplo:
                #   f"""Eres un analista de datos experto en el negocio de FitLife,
                #   una red de 5 gimnasios de proximidad.
                #
                #   El usuario preguntó: {prompt}
                #   El resultado calculado sobre los datos reales es: {resultado}
                #
                #   Explica este resultado en el contexto del negocio.
                #   Sé conciso (2-3 frases). Usa los números reales.
                #   Si el resultado sugiere algo accionable, menciónalo."""

                interpretation_prompt = ___

                # ── PASO B: llamar al LLM para interpretar ──
                # Misma estructura que la pasada 1, pero esta vez
                # le pasamos el prompt de interpretación.
                #
                # ↓ Borra ___ y escribe:
                #   client.chat.completions.create(
                #       model=MODEL,
                #       messages=[
                #           {"role": "system", "content": interpretation_prompt},
                #           {"role": "user", "content": prompt}
                #       ]
                #   )

                interpretation_response = ___

                interpretation = interpretation_response.choices[0].message.content
                st.markdown(interpretation)
                answer_text = interpretation
        else:
            error_msg = f"No se pudo obtener un resultado después de {MAX_RETRIES} intentos."
            if last_error:
                error_msg += f"\nÚltimo error: `{last_error}`"
            st.error(error_msg)
            answer_text = error_msg

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer_text,
            "code": last_code,
        })
