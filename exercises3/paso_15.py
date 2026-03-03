# ============================================================
# PASO 15 — El analista completo  (Bonus)
# ============================================================
#
# ── ¿Qué hay aquí? ─────────────────────────────────────────
#
# Este es el resultado final de las 3 sesiones. Integra todo:
#
#   ✓ Text-to-code (sesión 2)
#   ✓ Manejo de errores y reintentos (sesión 2)
#   ✓ Prompt enriquecido con valores y ejemplos (sesión 3)
#   ✓ Memoria de conversación (sesión 3)
#   ✓ Interpretación de resultados (sesión 3)
#
# Este paso NO tiene blancos ___. Funciona tal cual.
# Es la app que desplegaréis a la nube en la sesión 4.
#
# ── Tu misión ───────────────────────────────────────────────
#
# Usa esta herramienta para investigar el caso FitLife.
# Recuerda la pregunta central:
#
#   "¿Debería FitLife bajar el precio del plan básico?"
#
# Haz las 12 preguntas de PREGUNTAS_TEST.md. Para cada una,
# evalúa si la respuesta es correcta, parcial o incorrecta.
#
# Después, intenta responder la pregunta con datos:
#   - ¿Cuánto margen pierde FitLife por cada baja del básico?
#   - ¿Las bajas son por precio o por otras razones?
#   - ¿Qué pasa si baja de 29€ a 24€? ¿Cuánto dejaría
#     de ingresar con los socios actuales?
#   - ¿Los socios que se van por precio son rentables?
#
# ── Para pensar ─────────────────────────────────────────────
#
# Has construido en 3 sesiones un sistema que:
#   1. Entiende preguntas en español
#   2. Las traduce a código Python
#   3. Ejecuta el código contra datos reales
#   4. Explica el resultado en contexto de negocio
#
# Es el mismo patrón que usan herramientas como ChatGPT
# Code Interpreter, GitHub Copilot, o asistentes de BI.
#
# En la sesión 4 veremos:
#   - Cómo desplegar esta app en la nube (Streamlit Cloud)
#   - Modelos que "piensan" antes de actuar (razonamiento)
#   - Cómo un LLM puede usar herramientas (tool use)
#   - Varios modelos trabajando juntos (orquestación)
#
# ── Retos avanzados ─────────────────────────────────────────
#
#   A. Cambia MODEL a "gpt-4.1" (en vez de "gpt-4.1-mini")
#      para la interpretación. ¿Mejora la calidad de las
#      explicaciones? ¿Tarda más? ¿Merece la pena?
#
#   B. Añade más ejemplos al SYSTEM_PROMPT para tipos de
#      preguntas que fallan. ¿Cuántos ejemplos necesitas
#      para que las 12 preguntas funcionen?
#
#   C. Piensa: ¿qué preguntas NO puede responder este
#      sistema? ¿Qué necesitaría para responderlas?
#      (Pista: datos externos, predicciones, simulaciones...)
#
# Ejecuta:  streamlit run exercises3/paso_15.py
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


def interpret_result(client, model, prompt, resultado):
    """Pide al LLM que interprete el resultado en contexto de negocio."""
    interp_prompt = f"""Eres un analista de datos experto en el negocio de FitLife,
una red de 5 gimnasios de proximidad con planes basic (29€), premium (49€) y family (69€).
Su competidor low-cost cobra 19€ y los socios del plan básico se están dando de baja.

El usuario preguntó: {prompt}
El resultado calculado sobre los datos reales ({len(df_members):,} registros) es:
{resultado}

Explica este resultado en el contexto del negocio de FitLife.
Sé conciso (2-3 frases). Usa los números reales del resultado.
Si el resultado sugiere algo accionable para la decisión de precios, menciónalo."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": interp_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# ── Prompt del sistema (experto, con ejemplos) ─────────────

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

EJEMPLOS DE CÓDIGO:

Ejemplo 1 — Tasa de churn por plan:
  churn_plan = df_members.groupby('plan')['status'].apply(
      lambda x: (x == 'churned').sum() / len(x) * 100
  )
  resultado = churn_plan

Ejemplo 2 — Cruzar tablas (socios + contexto por mes):
  merged = df_members.merge(df_context, on='month')
  resultado = merged.groupby('month')[['visits_this_month', 'competitor_lowcost_price']].mean()

Ejemplo 3 — Margen por socio y plan:
  df_members['margin'] = df_members['price_paid'] - df_members['cost_to_serve']
  resultado = df_members.groupby('plan')['margin'].mean()

Ejemplo 4 — Comparar churn entre dos grupos:
  group_a = df_members[df_members['uses_app'] == True]
  group_b = df_members[df_members['uses_app'] == False]
  churn_a = (group_a['status'] == 'churned').sum() / len(group_a) * 100
  churn_b = (group_b['status'] == 'churned').sum() / len(group_b) * 100
  resultado = f"Con app: {{churn_a:.2f}}% churn, Sin app: {{churn_b:.2f}}% churn"

REGLAS DE CÁLCULO:
- Tasa de churn = (status == 'churned').sum() / total * 100
- Margen = price_paid - cost_to_serve
- Para cruzar tablas: df_members.merge(df_context, on='month')
- 'month' es string YYYY-MM. Para año: pd.to_datetime(df['month']).dt.year
- Un socio churned es uno con status == 'churned' en ese mes
- Para LTV: agrupa por member_id, suma price_paid de todos los meses

Reglas generales:
- Usa pandas para las operaciones.
- El código debe terminar con: resultado = <lo que calcules>
- NO uses print(). Solo asigna el resultado final a la variable "resultado".
- NO incluyas import ni read_csv — los datos ya están cargados.
- Devuelve SOLO el bloque de código, sin explicaciones antes ni después.
- Envuelve el código en triple backtick python."""

# ── Interfaz ────────────────────────────────────────────────

st.set_page_config(page_title="FitLife Analytics v3", layout="wide")

st.title("FitLife Analytics v3")
st.caption(f"Analista conversacional · {len(df_members):,} registros · {MODEL}")

col1, col2 = st.columns([3, 1])
with col1:
    st.write(f"Socios: **{len(df_members):,}** | Contexto: **{len(df_context)}** meses")
with col2:
    show_code = st.toggle("Mostrar código", value=False)

st.divider()

# ── Historial ───────────────────────────────────────────────

if "messages_v3" not in st.session_state:
    st.session_state.messages_v3 = []

for msg in st.session_state.messages_v3:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("code") and show_code:
            with st.expander("Código ejecutado"):
                st.code(msg["code"], language="python")

# ── Chat ────────────────────────────────────────────────────

if prompt := st.chat_input("Pregunta sobre los datos de FitLife..."):
    st.session_state.messages_v3.append({"role": "user", "content": prompt})
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

        if resultado is not None:
            if show_code and last_code:
                with st.expander("Código ejecutado"):
                    st.code(last_code, language="python")

            with st.spinner("Interpretando..."):
                interpretation = interpret_result(client, MODEL, prompt, resultado)
                st.markdown(interpretation)
                answer_text = interpretation
        else:
            error_msg = f"No se pudo obtener un resultado después de {MAX_RETRIES} intentos."
            if last_error:
                error_msg += f"\nÚltimo error: `{last_error}`"
            st.error(error_msg)
            answer_text = error_msg

        st.session_state.messages_v3.append({
            "role": "assistant",
            "content": answer_text,
            "code": last_code,
        })
