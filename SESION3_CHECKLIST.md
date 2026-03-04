# Checklist — Sesión 3

Completa estos pasos **antes** de la tercera sesión.

---

## 1. Actualiza el proyecto

Abre la terminal en VS Code y ejecuta:

```
git pull
```

Deberías ver archivos nuevos descargados. Verifica que ves la carpeta `exercises3/` en el explorador.

## 2. Verifica tu entorno

```
conda activate mda13
streamlit run test_app.py
```

Todo en verde → listo.

## 3. Verifica tu API key

Comprueba que tienes el archivo `.env` en la raíz del proyecto:

```
OPENAI_API_KEY=tu-clave-aquí
```

## 4. Repasa la sesión 2

Lee [`SESION2_REPASO.md`](SESION2_REPASO.md). Tiene un resumen de los conceptos y el código resuelto de cada ejercicio.

Lo más importante que debes recordar:
- El LLM genera **código Python** en vez de responder directamente.
- Python ejecuta el código y calcula sobre los **datos reales** (16.334 filas).
- `try/except` maneja los errores sin que la app se rompa.
- El prompt necesita incluir los **valores reales** de las columnas para que el LLM no adivine.

## 5. (Opcional) Prueba paso_11

Si no lo hiciste en la sesión 2, prueba el paso bonus:

```
streamlit run exercises2/paso_11.py
```

Introduce reintentos automáticos: si el código falla, el LLM lo corrige. Es la base de lo que veremos en la sesión 3.
