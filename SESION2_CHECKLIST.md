# Checklist — Sesión 2

Completa estos pasos **antes** de la segunda sesión.

---

## 1. Actualiza el proyecto

Abre la terminal en VS Code y ejecuta:

```
git pull
```

Deberías ver archivos nuevos descargados. Si da error, consulta [`ACTUALIZAR.md`](ACTUALIZAR.md).

Verifica que ves estas carpetas nuevas en el explorador de archivos:
- `exercises2/` — ejercicios de la sesión 2
- `extras/` — ejercicios opcionales

## 2. Verifica tu entorno

```
conda activate mda13
streamlit run test_app.py
```

Todo en verde → listo.

## 3. Verifica tu API key

Comprueba que tienes el archivo `.env` en la raíz del proyecto con tu API key:

```
OPENAI_API_KEY=tu-clave-aquí
```

Si no lo tienes, créalo. La clave te la facilitó el profesor en la sesión 1.

## 4. Repasa la sesión 1

Lee [`SESION1_REPASO.md`](SESION1_REPASO.md). Tiene un resumen de todos los conceptos y el código resuelto de cada ejercicio.

Lo más importante que debes recordar:
- El LLM entiende el lenguaje pero **no puede calcular** sobre datos que no ha visto.
- Cuando no sabe, se inventa la respuesta (**alucinación**).
- En la sesión 2 vamos a hacer que el LLM **escriba código** en vez de responder directamente.

## 5. (Opcional) Explora los datos

Si quieres adelantar, ejecuta:

```
streamlit run extras/opcional_analisis.py
```

Responde las 5 preguntas del paso_6 pero con código real. Te dará las respuestas correctas como referencia.
