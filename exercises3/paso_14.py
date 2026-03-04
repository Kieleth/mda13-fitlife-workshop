# ============================================================
# PASO 14 — El prompt experto
# ============================================================
#
# ── ¿Por qué falla con preguntas difíciles? ────────────────
#
# Prueba esta pregunta en paso_13:
#   "¿Las bajas del plan básico aumentaron cuando el
#    competidor bajó precios?"
#
# Probablemente falle o dé un resultado incorrecto. ¿Por qué?
# Porque el LLM tiene que:
#   1. Entender que necesita cruzar dos tablas
#   2. Saber que el competidor está en df_context
#   3. Calcular churn del básico por mes
#   4. Correlacionar con el precio del competidor
#
# Sin ayuda, el LLM tiene que adivinar toda esta lógica.
#
# ── La solución: enseñarle con ejemplos ─────────────────────
#
# Los humanos aprendemos con ejemplos. Los LLMs también.
# Si le muestras CÓMO resolver un tipo de pregunta, genera
# código mucho mejor para preguntas similares.
#
# Esto se llama "few-shot prompting": darle unos pocos
# ejemplos en el prompt para que entienda el patrón.
#
#   Prompt sin ejemplos (zero-shot):
#     "Genera código para responder a la pregunta."
#
#   Prompt con ejemplos (few-shot):
#     "Genera código para responder a la pregunta.
#      Ejemplo: para calcular tasa de churn por plan:
#        churn = df_members.groupby('plan')['status'].apply(
#            lambda x: (x == 'churned').sum() / len(x) * 100
#        )
#        resultado = churn"
#
# ── Tu reto ─────────────────────────────────────────────────
#
# Completa las dos variables marcadas con ___ :
#
#   1. EXAMPLES: añadir ejemplos de código (busca EXAMPLES = """___""")
#   2. RULES: añadir reglas de cálculo del negocio (busca RULES = """___""")
#
# Después, prueba las preguntas difíciles de PREGUNTAS_TEST.md
# (preguntas 7-12). ¿Cuántas más responde correctamente?
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Añade más ejemplos al prompt. ¿Mejora la calidad?
#      ¿Hay un punto donde más ejemplos no ayudan?
#
#   B. Prueba a quitar los ejemplos que has añadido.
#      ¿Cuántas preguntas dejan de funcionar?
#
#   C. Prueba la pregunta 12: "¿Debería FitLife bajar el
#      precio del plan básico?" ¿Qué hace el sistema?
#      ¿La interpretación es útil? ¿Qué le falta?
#
# Ejecuta:  streamlit run exercises3/paso_14.py
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
    """Pide al LLM que interprete el resultado en contexto."""
    interp_prompt = f"""Eres un analista de datos experto en el negocio de FitLife,
una red de 5 gimnasios de proximidad.

El usuario preguntó: {prompt}
El resultado calculado sobre los datos reales es: {resultado}

Explica este resultado en el contexto del negocio.
Sé conciso (2-3 frases). Usa los números reales.
Si el resultado sugiere algo accionable, menciónalo."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": interp_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# ── Prompt del sistema (EXPERTO) ───────────────────────────
# Este es el prompt que vamos a mejorar con ejemplos y reglas.

# ── PASO 1: Escribe los ejemplos de código ──────────────────
# Copia aquí 2-3 ejemplos de las PISTAS de abajo.
# Reemplaza el ___ con el texto de los ejemplos.
#
# ↓ Borra ___ y escribe tus ejemplos (ver PISTAS más abajo)

EXAMPLES = """Ejemplo 1 — Tasa de churn por plan:
churn_plan = df_members.groupby('plan')['status'].apply(
    lambda x: (x == 'churned').sum() / len(x) * 100
)
resultado = churn_plan

Ejemplo 2 — Cruzar tablas (socios + contexto):
merged = df_members.merge(df_context, on='month')
resultado = merged.groupby('month')[['visits_this_month', 'competitor_lowcost_price']].mean()

Ejemplo 3 — Margen por socio:
df_members['margin'] = df_members['price_paid'] - df_members['cost_to_serve']
resultado = df_members.groupby('plan')['margin'].mean()"""

# ── PASO 2: Escribe las reglas de cálculo ───────────────────
# Copia aquí las reglas específicas del negocio.
# Reemplaza el ___ con las reglas.
#
# ↓ Borra ___ y escribe tus reglas (ver PISTAS más abajo)

RULES = """- Tasa de churn = churned / total * 100 (como porcentaje)
- Margen = price_paid - cost_to_serve
- Para cruzar tablas: df_members.merge(df_context, on='month')
- Un socio "churned" es uno con status == 'churned' en ese mes
- 'month' es string con formato YYYY-MM. Para extraer año: pd.to_datetime(df['month']).dt.year"""

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

{EXAMPLES}

REGLAS DE CÁLCULO:

{RULES}

Reglas generales:
- Usa pandas para las operaciones.
- El código debe terminar con: resultado = <lo que calcules>
- NO uses print(). Solo asigna el resultado final a la variable "resultado".
- NO incluyas import ni read_csv — los datos ya están cargados.
- Devuelve SOLO el bloque de código, sin explicaciones antes ni después.
- Envuelve el código en triple backtick python."""

# ═══════════════════════════════════════════════════════════
# PISTAS para los ___ de arriba:
#
# EJEMPLOS DE CÓDIGO — escribe 2-3 ejemplos como estos:
#
#   Ejemplo 1 — Tasa de churn por plan:
#     churn_plan = df_members.groupby('plan')['status'].apply(
#         lambda x: (x == 'churned').sum() / len(x) * 100
#     )
#     resultado = churn_plan
#
#   Ejemplo 2 — Cruzar tablas (socios + contexto):
#     merged = df_members.merge(df_context, on='month')
#     resultado = merged.groupby('month')[['visits_this_month', 'competitor_lowcost_price']].mean()
#
#   Ejemplo 3 — Margen por socio:
#     df_members['margin'] = df_members['price_paid'] - df_members['cost_to_serve']
#     resultado = df_members.groupby('plan')['margin'].mean()
#
# REGLAS DE CÁLCULO — escribe reglas específicas del negocio:
#
#   - Tasa de churn = churned / total * 100 (como porcentaje)
#   - Margen = price_paid - cost_to_serve
#   - Para cruzar tablas: df_members.merge(df_context, on='month')
#   - Un socio "churned" es uno con status == 'churned' en ese mes
#   - 'month' es string con formato YYYY-MM. Para extraer año: pd.to_datetime(df['month']).dt.year
# ═══════════════════════════════════════════════════════════

# ── Interfaz ────────────────────────────────────────────────

st.title("FitLife Analytics")
st.caption(f"Paso 14 — Prompt experto · {len(df_members):,} registros")

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

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer_text,
            "code": last_code,
        })
