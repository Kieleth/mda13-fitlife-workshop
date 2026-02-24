# ============================================================
# PASO 2 — Carga datos
# ============================================================
#
# pandas es una librería de Python para trabajar con tablas de
# datos (como Excel, pero en código). La función clave es:
#
#   pd.read_csv("ruta/al/archivo.csv")
#
# Carga un archivo CSV y lo convierte en un DataFrame: una tabla
# con filas y columnas que puedes explorar y manipular.
#
# Tu reto: esta app intenta cargar datos pero falla.
# Ejecútala, lee el error y arregla la ruta del archivo.
#
# Pista: los archivos CSV están dentro de la carpeta data/
#
# Ejecuta:  streamlit run exercises/paso_2.py
# ============================================================

import streamlit as st
import pandas as pd

st.title("FitLife Dashboard")

df = pd.read_csv("fitlife_members.csv")

st.write(f"El dataset tiene **{len(df)}** filas y **{len(df.columns)}** columnas.")
st.dataframe(df)
