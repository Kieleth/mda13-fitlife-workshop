# ============================================================
# PASO 3 — Explora los dos datasets
# ============================================================
#
# ── Los datos de FitLife ────────────────────────────────────
#
# FitLife tiene dos archivos de datos:
#
#   fitlife_members.csv  — Un registro por socio y mes.
#      Cada fila es un socio en un mes concreto. Contiene:
#      plan, centro, visitas, si usa la app, si se dio de
#      baja (churned), etc. ~16.000 filas.
#
#   fitlife_context.csv  — Contexto del negocio por mes.
#      Precio del competidor, campañas activas, incidencias,
#      costes fijos. 36 filas (una por mes, 3 años).
#
# Las dos tablas se conectan por la columna "month".
#
# ── Funciones útiles ────────────────────────────────────────
#
#   len(df)            ->  número de filas
#   len(df.columns)    ->  número de columnas
#   list(df.columns)   ->  lista con los nombres de las columnas
#   df.head()          ->  las primeras 5 filas
#
# ── Tu reto ─────────────────────────────────────────────────
#
# El primer dataset ya está cargado. Completa las líneas con
# ___ para cargar el segundo y mostrar su información.
#
# Recuerda: borra cada ___ y escribe en su lugar el código.
# El patrón que necesitas ya está resuelto arriba para el
# primer dataset — solo tienes que repetirlo para el segundo.
#
# ── Si has terminado antes ──────────────────────────────────
#
#   A. Prueba:
#        st.write(df_members["status"].value_counts())
#      ¿Cuántos socios activos hay vs. churned? ¿Te parece
#      mucho o poco churn?
#
#   B. Prueba:
#        st.write(df_members["churn_reason"].value_counts())
#      ¿Cuál es la razón de baja más frecuente? ¿Tiene
#      sentido con lo que sabes del caso?
#
#   C. Prueba:
#        st.line_chart(df_context.set_index("month")["competitor_lowcost_price"])
#      Esto dibuja la evolución del precio del competidor.
#      ¿Qué tendencia ves? ¿Cómo se compara con los 29€
#      del plan básico de FitLife?
#
# Ejecuta:  streamlit run exercises/paso_3.py
# ============================================================

import streamlit as st
import pandas as pd

st.title("FitLife Dashboard")

# --- Dataset 1: socios (ya resuelto — fíjate en el patrón) ---
df_members = pd.read_csv("data/fitlife_members.csv")

st.subheader("Datos de socios")
st.write(f"**{len(df_members)}** filas, **{len(df_members.columns)}** columnas")
st.write("Columnas:", list(df_members.columns))
st.dataframe(df_members.head())

# --- Dataset 2: contexto mensual ---
# ↓ Mismo patrón que la línea 63: pd.read_csv("data/...")
df_context = ___  # Carga data/fitlife_context.csv

st.subheader("Contexto mensual")
# ↓ Mismo patrón que la línea 66: len(df_context) y len(df_context.columns)
st.write(f"**{___}** filas, **{___}** columnas")
st.write("Columnas:", list(df_context.columns))
st.dataframe(df_context.head())
