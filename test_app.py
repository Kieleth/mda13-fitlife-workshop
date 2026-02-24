"""
Test de verificacion — MDA13
Ejecuta esto para confirmar que tu entorno esta listo:
    streamlit run test_app.py
Si ves la pagina sin errores, estas listo para el taller.
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="MDA13 — Test de verificacion", page_icon="✅")

st.title("Test de verificacion")

# 1. Python + Streamlit funcionan (si ves esto, ya esta)
st.success("Streamlit funciona correctamente.")

# 2. Pandas funciona
try:
    df = pd.DataFrame({"test": [1, 2, 3], "valor": [10, 20, 30]})
    st.success(f"Pandas funciona correctamente. (v{pd.__version__})")
except Exception as e:
    st.error(f"Error con pandas: {e}")

# 3. OpenAI instalado (no necesita API key, solo verifica el import)
try:
    import openai
    st.success(f"OpenAI instalado correctamente. (v{openai.__version__})")
except ImportError:
    st.error("OpenAI no esta instalado. Ejecuta: pip install openai")

# 4. python-dotenv instalado
try:
    import dotenv
    st.success("python-dotenv instalado correctamente.")
except ImportError:
    st.error("python-dotenv no esta instalado. Ejecuta: pip install python-dotenv")

# 5. Datos accesibles
try:
    members = pd.read_csv("data/fitlife_members.csv")
    context = pd.read_csv("data/fitlife_context.csv")
    st.success(f"Datos cargados: {len(members):,} filas en members, {len(context)} filas en context.")
except FileNotFoundError as e:
    st.error(f"No se encontraron los datos: {e}")
    st.info("Asegurate de estar ejecutando desde la carpeta del proyecto.")

st.divider()
st.markdown("Si todos los checks son verdes, tu entorno esta listo para el taller.")
