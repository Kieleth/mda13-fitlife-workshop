# ============================================================
# PASO 3 — Explora los dos datasets
# ============================================================
#
# FitLife tiene dos archivos de datos:
#
#   fitlife_members.csv  — un registro por socio y mes
#   fitlife_context.csv  — contexto del negocio por mes
#
# Tu reto: completa las líneas marcadas con ___ para cargar
# el segundo dataset y mostrar su información.
#
# Funciones útiles:
#   len(df)            ->  número de filas
#   len(df.columns)    ->  número de columnas
#   list(df.columns)   ->  lista con los nombres de las columnas
#   df.head()          ->  las primeras 5 filas
#
# Ejecuta:  streamlit run exercises/paso_3.py
# ============================================================

import streamlit as st
import pandas as pd

st.title("FitLife Dashboard")

# --- Dataset 1: socios ---
df_members = pd.read_csv("data/fitlife_members.csv")

st.subheader("Datos de socios")
st.write(f"**{len(df_members)}** filas, **{len(df_members.columns)}** columnas")
st.write("Columnas:", list(df_members.columns))
st.dataframe(df_members.head())

# --- Dataset 2: contexto mensual ---
df_context = ___  # Carga data/fitlife_context.csv

st.subheader("Contexto mensual")
st.write(f"**{___}** filas, **{___}** columnas")  # Usa len() como arriba
st.write("Columnas:", list(df_context.columns))
st.dataframe(df_context.head())
