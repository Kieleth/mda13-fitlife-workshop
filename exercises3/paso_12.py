# ============================================================
# PASO 12 — El chat recuerda
# ============================================================
#
# ── ¿Qué hicimos en la sesión 2? ───────────────────────────
#
# Construimos un sistema text-to-code: el LLM genera código
# Python, lo ejecutamos con exec(), y mostramos el resultado.
# Añadimos manejo de errores y, opcionalmente, reintentos.
#
# Pero hay un problema: cada vez que escribes una pregunta,
# la app se OLVIDA de todo lo anterior. No puedes preguntar:
#
#   "¿Cuántos planes tiene FitLife?"
#   "¿Cuál es el más caro?"          ← no sabe de qué hablas
#
# ── ¿Por qué se olvida? ────────────────────────────────────
#
# Streamlit funciona de una forma especial: cada vez que
# el usuario hace CUALQUIER acción (escribir en el chat,
# pulsar un botón...), Streamlit ejecuta TODO el archivo
# de arriba a abajo, desde la línea 1.
#
# Es como si pulsaras "play" de nuevo cada vez. Todas las
# variables se reinician. Todo lo que no esté guardado en
# un sitio especial, desaparece.
#
# ── ¿Qué es st.session_state? ──────────────────────────────
#
# st.session_state es un diccionario especial que Streamlit
# mantiene vivo entre ejecuciones. Lo que guardes ahí,
# sobrevive:
#
#   # Primera ejecución:
#   st.session_state["nombre"] = "Ana"
#
#   # Segunda ejecución (el usuario hizo algo):
#   st.session_state["nombre"]  # → "Ana" (¡sigue ahí!)
#
# Para el chat, lo usamos así:
#
#   # Al principio del archivo (solo la primera vez):
#   if "mensajes" not in st.session_state:
#       st.session_state.mensajes = []
#
#   # Cuando el usuario escribe algo:
#   st.session_state.mensajes.append({"role": "user", ...})
#
#   # Para mostrar el historial:
#   for msg in st.session_state.mensajes:
#       with st.chat_message(msg["role"]):
#           st.write(msg["content"])
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa las tres líneas marcadas con ___ :
#
#   1. Inicializar la lista de mensajes en session_state
#   2. Guardar el mensaje del usuario en el historial
#   3. Guardar la respuesta del asistente en el historial
#
# Cuando funcione, prueba este diálogo:
#   "¿Cuántos planes tiene FitLife?"
#   "¿Cuál es el que tiene más socios?"
#   "¿Y el que tiene más churn?"
#
# Las preguntas anteriores se mantienen en pantalla, y el
# LLM puede ver el contexto de la conversación.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Haz 5-6 preguntas seguidas. ¿El historial se mantiene?
#      ¿Las respuestas tienen en cuenta las preguntas anteriores?
#
#   B. Recarga la página (F5). ¿Qué pasa con el historial?
#      ¿Por qué? (Pista: session_state vive mientras la
#      sesión del navegador esté abierta.)
#
#   C. Prueba las preguntas de PREGUNTAS_TEST.md una a una.
#      ¿Cuántas responde correctamente? Anota los resultados.
#
# Ejecuta:  streamlit run exercises3/paso_12.py
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

# ── Funciones auxiliares (de la sesión 2) ───────────────────

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


# ── Prompt del sistema (enriquecido) ───────────────────────

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
st.caption(f"Paso 12 — El chat recuerda · {len(df_members):,} registros")

col1, col2 = st.columns([3, 1])
with col1:
    st.write(f"Socios: **{len(df_members):,}** | Contexto: **{len(df_context)}** meses")
with col2:
    show_code = st.toggle("Mostrar código", value=False)

st.divider()

# ── PASO 1: Inicializar el historial ───────────────────────
# session_state es un diccionario que Streamlit mantiene vivo
# entre ejecuciones. Lo usamos para guardar los mensajes.
#
# Solo hay que inicializarlo UNA VEZ (la primera ejecución).
# Por eso comprobamos si ya existe antes de crearlo.
#
# ↓ Borra ___ y escribe:
#   st.session_state.messages = []

if "messages" not in st.session_state:
    ___

# ── Mostrar el historial de mensajes ───────────────────────
# Cada vez que Streamlit ejecuta el archivo, necesitamos
# re-dibujar todos los mensajes anteriores.

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("code") and show_code:
            with st.expander("Código ejecutado"):
                st.code(msg["code"], language="python")

# ── Chat ────────────────────────────────────────────────────

if prompt := st.chat_input("Pregunta sobre los datos de FitLife..."):

    # ── PASO 2: Guardar el mensaje del usuario ──────────────
    # Añadimos el mensaje del usuario al historial para que
    # se muestre en la siguiente ejecución y el LLM lo vea.
    #
    # ↓ Borra ___ y escribe:
    #   st.session_state.messages.append({"role": "user", "content": prompt})

    ___

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generando y ejecutando código..."):

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

            # Mostrar resultado
            if resultado is not None:
                st.write(resultado)
                answer_text = str(resultado)
            else:
                error_msg = f"No se pudo obtener un resultado después de {MAX_RETRIES} intentos."
                if last_error:
                    error_msg += f"\nÚltimo error: `{last_error}`"
                st.error(error_msg)
                answer_text = error_msg

            if last_code and show_code:
                with st.expander("Código ejecutado"):
                    st.code(last_code, language="python")

        # ── PASO 3: Guardar la respuesta del asistente ──────
        # Igual que con el usuario, guardamos la respuesta
        # para que se muestre en el historial.
        #
        # ↓ Borra ___ y escribe:
        #   st.session_state.messages.append({"role": "assistant", "content": answer_text, "code": last_code})

        ___
