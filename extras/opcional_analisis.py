# ============================================================
# OPCIONAL — Analiza los datos de FitLife con código
# ============================================================
#
# ── ¿Para qué es este ejercicio? ────────────────────────────
#
# En paso_6 le pediste al LLM que respondiera preguntas sobre
# los datos de FitLife. Algunas respuestas eran correctas y
# otras inventadas.
#
# En este ejercicio vas a responder las MISMAS preguntas, pero
# usando código de verdad. Pandas puede calcular sobre las
# 16.334 filas — el LLM no podía.
#
# Esto te dará dos cosas:
#   1. Las respuestas REALES (tu fuente de verdad)
#   2. Una idea de lo que la sesión 2 automatizará:
#      "¿Y si el LLM pudiera escribir este código por ti?"
#
# ── Cómo funciona ──────────────────────────────────────────
#
# Cada sección tiene:
#   - Una pregunta (las mismas 5 del paso_6)
#   - El código resuelto que la responde
#   - Espacio para que compares con lo que dijo el LLM
#
# No tienes que escribir código — solo leerlo, ejecutarlo, y
# entender qué hace. Si quieres experimentar, modifica lo que
# quieras.
#
# ── Funciones de pandas que se usan ────────────────────────
#
#   df["columna"]                 -> seleccionar una columna
#   df[df["col"] == "valor"]      -> filtrar filas
#   df["col"].value_counts()      -> contar valores únicos
#   df.groupby("col")             -> agrupar por una columna
#   len(df)                       -> número de filas
#   df["col"].sum()               -> suma de una columna
#   df["col"].mean()              -> media de una columna
#
# ── Retos extra (si te sobra tiempo) ───────────────────────
#
#   Al final del archivo hay preguntas más avanzadas para
#   quienes quieran profundizar.
#
# Ejecuta:  streamlit run extras/opcional_analisis.py
# ============================================================

import streamlit as st
import pandas as pd

st.title("FitLife — Análisis con código")
st.caption("Las respuestas reales que el LLM no podía darte")

df_members = pd.read_csv("data/fitlife_members.csv")
df_context = pd.read_csv("data/fitlife_context.csv")

# ============================================================
# PREGUNTA 1: ¿Cuántos registros tiene el dataset de socios?
# ============================================================

st.header("Pregunta 1: ¿Cuántos registros?")

total_registros = len(df_members)
total_columnas = len(df_members.columns)

st.write(f"**{total_registros:,}** filas, **{total_columnas}** columnas")
st.write("Cada fila es un socio en un mes concreto.")
st.write("El LLM acertaba esta porque el número estaba en el prompt.")

st.divider()

# ============================================================
# PREGUNTA 2: ¿Qué planes ofrece FitLife?
# ============================================================

st.header("Pregunta 2: ¿Qué planes ofrece FitLife?")

# value_counts() cuenta cuántas filas hay de cada valor
planes = df_members["plan"].value_counts()
st.write("**Distribución de planes (total de registros):**")
st.write(planes)
st.write("""
Los tres planes son: **basic** (29€), **premium** (49€), **family** (69€).
El LLM solo veía los planes que aparecían en las 5 filas de muestra.
""")

st.divider()

# ============================================================
# PREGUNTA 3: ¿Cuál es el centro con más socios?
# ============================================================

st.header("Pregunta 3: ¿Cuál es el centro con más socios?")

centros = df_members["center"].value_counts()
st.write("**Registros por centro:**")
st.write(centros)
st.write(f"""
El centro con más registros es **{centros.index[0]}** con **{centros.iloc[0]:,}**.
El LLM no podía contar sobre 16.334 filas — solo veía 5.
""")

st.divider()

# ============================================================
# PREGUNTA 4: ¿Cuál es la tasa de churn del plan básico?
# ============================================================

st.header("Pregunta 4: ¿Tasa de churn del plan básico?")

# Filtrar solo registros del plan básico
basico = df_members[df_members["plan"] == "basic"]

# Contar churned vs total
total_basico = len(basico)
churned_basico = len(basico[basico["status"] == "churned"])
tasa_churn = churned_basico / total_basico * 100

st.write(f"Registros plan básico: **{total_basico:,}**")
st.write(f"De esos, churned: **{churned_basico:,}**")
st.write(f"**Tasa de churn global: {tasa_churn:.2f}%**")

st.write("""
Este es el número REAL. El LLM se inventaba un porcentaje diferente
cada vez que preguntabas. Si hiciste la pregunta 3 veces y te dio
3 números distintos, ahora sabes por qué.
""")

# Churn por año (más detallado)
st.subheader("Churn del plan básico por año")
basico_con_year = basico.copy()
basico_con_year["year"] = pd.to_datetime(basico_con_year["month"]).dt.year
churn_por_year = basico_con_year.groupby("year").apply(
    lambda g: (g["status"] == "churned").sum() / len(g) * 100
).reset_index(name="churn_rate")
st.write(churn_por_year)
st.write("Fíjate: el churn del básico sube cada año. ¿Por qué?")

st.divider()

# ============================================================
# PREGUNTA 5: ¿Debería FitLife bajar el precio del plan básico?
# ============================================================

st.header("Pregunta 5: ¿Debería FitLife bajar el precio?")

st.write("Esta pregunta no se responde con una sola línea de código. Necesitas datos.")

# Datos clave para la decisión
st.subheader("Dato 1: Evolución del precio del competidor")
st.line_chart(df_context.set_index("month")["competitor_lowcost_price"])
st.write("El competidor low-cost bajó de 25€ a 19€. FitLife cobra 29€ en el plan básico.")

st.subheader("Dato 2: Motivos de baja del plan básico")
motivos = basico[basico["status"] == "churned"]["churn_reason"].value_counts()
st.write(motivos)
st.write("¿Cuántas bajas son por 'price' o 'competitor'?")

st.subheader("Dato 3: Margen de los socios que se van por precio")
baja_precio = basico[basico["churn_reason"].isin(["price", "competitor"])]
margen_baja = (baja_precio["price_paid"] - baja_precio["cost_to_serve"]).mean()
margen_activos = (basico[basico["status"] == "active"]["price_paid"] -
                  basico[basico["status"] == "active"]["cost_to_serve"]).mean()
st.write(f"Margen medio de los que se van por precio: **{margen_baja:.2f}€**")
st.write(f"Margen medio de los activos del básico: **{margen_activos:.2f}€**")
st.write("""
Sorpresa: los socios que se van por precio tienen MAYOR margen que los
que se quedan. Visitan poco, cuestan poco, pero pagan lo mismo.
Perderlos duele más de lo que parece.
""")

st.subheader("Dato 4: ¿Cuánto margen se pierde si bajamos a 24€?")
activos_basico = len(basico[basico["status"] == "active"])
# Esto es una estimación simplificada
perdida_mes = activos_basico * 5  # 5€ menos por cada socio activo del básico
st.write(f"Socios activos del básico (acumulado): ~{activos_basico}")
st.write(f"Si cada uno paga 5€ menos: ~{perdida_mes}€ menos al mes")

st.write("""
---
**No hay una respuesta fácil.** Los datos permiten argumentar en varias
direcciones — pero con números, no con intuición. Eso es lo que construiremos
en las próximas sesiones: un sistema que te deje explorar estas preguntas
en lenguaje natural y obtener respuestas reales.
""")

st.divider()

# ============================================================
# RETOS EXTRA (para quienes quieran más)
# ============================================================

st.header("Retos extra")

st.write("""
Si has llegado hasta aquí y quieres más, intenta responder estas preguntas
añadiendo código debajo. Usa las funciones de pandas que has visto arriba.

1. **¿Los socios que usan la app se dan menos de baja?**
   Pista: filtra por `uses_app == True` y `uses_app == False`,
   calcula la tasa de churn de cada grupo.

2. **¿Qué canal de captación trae socios más fieles?**
   Pista: agrupa por `acquisition_channel`, calcula % de churned en cada grupo.

3. **¿Cuánto ingresa FitLife al mes en promedio?**
   Pista: agrupa por `month`, suma `price_paid`, calcula la media.

4. **¿Las incidencias de servicio correlacionan con más bajas?**
   Pista: necesitas cruzar las dos tablas. Mira qué meses tienen
   `service_incident` en el dataset de contexto y compara el churn
   de esos meses con los que no tienen incidencias.
""")
