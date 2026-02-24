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
# Estructura del proyecto (mira dónde están los CSV):
#
#   mda13-fitlife-workshop/
#   ├── exercises/
#   │   ├── paso_0.py
#   │   ├── paso_1.py
#   │   ├── paso_2.py  ← estás aquí
#   │   └── ...
#   ├── data/
#   │   ├── fitlife_members.csv   ← este archivo
#   │   └── fitlife_context.csv
#   ├── test_app.py
#   └── ...
#
# Importante: cuando ejecutas "streamlit run exercises/paso_2.py",
# el código se ejecuta desde la raíz del proyecto (la carpeta
# mda13-fitlife-workshop/). Las rutas en el código son relativas
# a esa raíz.
#
# Ejecuta:  streamlit run exercises/paso_2.py
# ============================================================

import streamlit as st
import pandas as pd

st.title("FitLife Dashboard")

df = pd.read_csv("fitlife_members.csv")

st.write(f"El dataset tiene **{len(df)}** filas y **{len(df.columns)}** columnas.")
st.dataframe(df)
