# Debugging en Streamlit y LLMs

Cuando algo no funciona (o funciona raro), necesitas ver que esta pasando por dentro. Esta guia te da los trucos practicos para investigar problemas en tus apps de Streamlit y en las llamadas al LLM.

---

## 1. print() no funciona en Streamlit (y que usar en su lugar)

Si escribes `print("hola")` en una app de Streamlit, no ves nada. Ni en la app ni en la terminal. Parece que se lo traga.

**Por que?** Streamlit captura la salida estandar (stdout) para su propio uso. Tu `print()` se ejecuta, pero nadie lo ve.

**Solucion: usa `logging`**

```python
import logging
logging.basicConfig(level=logging.INFO)

# En cualquier parte de tu codigo:
logging.info("Esto SI aparece en la terminal")
```

Esto escribe directamente en la terminal donde ejecutaste `streamlit run`. No en la app, no en el navegador — en la terminal de VS Code.

**Regla:** `print()` para scripts normales de Python. `logging` para Streamlit.

---

## 2. Ver que le envias al LLM

El error mas comun con LLMs no es un error de Python. Es que le estas enviando algo diferente a lo que crees. Para verlo, pon un `logging.info` justo antes de la llamada a la API:

```python
import logging
logging.basicConfig(level=logging.INFO)

# ... tu codigo ...

# Justo ANTES de la llamada:
logging.info("=== PROMPT DEL SISTEMA ===")
logging.info(context)
logging.info("=== PREGUNTA DEL USUARIO ===")
logging.info(prompt)
logging.info("=== FIN ===")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": context},
        {"role": "user", "content": prompt}
    ]
)
```

Ahora mira la terminal. Veras exactamente el texto que recibe el LLM. Si ves que falta algo (por ejemplo, no aparecen los valores "basic", "premium", "family"), ya sabes por que responde mal.

**Truco:** si el prompt es muy largo y cuesta leerlo en la terminal, puedes guardarlo en un archivo:

```python
with open("ultimo_prompt.txt", "w") as f:
    f.write(context)
logging.info("Prompt guardado en ultimo_prompt.txt")
```

---

## 3. Ver que te responde el LLM (la respuesta cruda)

A veces la app muestra un error, pero no sabes si el problema es del LLM o de tu codigo. Inspecciona la respuesta:

```python
response = client.chat.completions.create(...)

# Ver la respuesta completa:
logging.info("=== RESPUESTA DEL LLM ===")
logging.info(response.choices[0].message.content)
logging.info("=== FIN RESPUESTA ===")
```

Esto es especialmente util en text-to-code. Si el LLM genera codigo con errores, lo veras en la terminal antes de que `exec()` lo intente ejecutar.

---

## 4. Ver los errores de exec() con detalle

Cuando `exec()` falla, Python genera un traceback (la pila de errores). En la app solo ves el mensaje resumido. Para ver el traceback completo:

```python
import traceback

try:
    exec(code, exec_globals)
except Exception as e:
    logging.info("=== ERROR EN EXEC ===")
    logging.info(f"Codigo que fallo:\n{code}")
    logging.info(f"Error: {e}")
    logging.info(traceback.format_exc())
    logging.info("=== FIN ERROR ===")
```

Ahora en la terminal ves: que codigo se intento ejecutar, que error dio, y en que linea del codigo generado fallo.

---

## 5. Mostrar cosas en la app (para depuracion visual)

A veces es mas facil ver la informacion directamente en la app. Streamlit tiene herramientas para esto:

### st.expander: informacion que se puede abrir y cerrar

```python
with st.expander("Ver prompt enviado"):
    st.code(context)
```

Esto crea un bloque plegable. No molesta al usuario normal, pero si lo abres, ves todo el prompt.

### st.sidebar: informacion en la barra lateral

```python
with st.sidebar:
    st.write("Ultimo prompt:", len(context), "caracteres")
    st.write("Modelo:", MODEL)
    st.write("Tokens aprox:", len(context.split()))
```

### st.json: para ver estructuras de datos

```python
st.json({
    "modelo": MODEL,
    "mensajes_enviados": len(messages),
    "ultimo_rol": messages[-1]["role"],
})
```

---

## 6. El LLM responde bien pero la app no muestra nada

Checklist rapido:

1. **El resultado es `None`?** El codigo generado no tiene `resultado = ...` al final. Anade al prompt: "Asigna el resultado final a una variable llamada resultado."

2. **El resultado es un DataFrame vacio?** El filtro no encontro nada. Probablemente el LLM uso un valor incorrecto (como "basico" en vez de "basic"). Mira el codigo generado.

3. **Streamlit se re-ejecuta y lo borra todo?** Cada interaccion re-ejecuta todo el archivo. Si no usas `st.session_state`, los resultados desaparecen.

4. **El spinner se queda girando para siempre?** La llamada a la API esta tardando. Espera 15-20 segundos. Si pasa de 30, probablemente hay un error de conexion.

---

## 7. Errores comunes y que significan

| Error | Que significa | Que hacer |
|-------|--------------|-----------|
| `AuthenticationError` | La API key esta mal o no existe | Revisa el archivo `.env` |
| `RateLimitError` | Demasiadas llamadas en poco tiempo | Espera 30 segundos |
| `ModuleNotFoundError: openai` | El paquete no esta instalado o el entorno no esta activo | `conda activate mda13` y luego `pip install openai` |
| `KeyError: 'basico'` | El codigo busca un valor que no existe en los datos | Los valores estan en ingles: "basic", no "basico" |
| `NameError: 'resultado'` | El codigo generado no creo la variable `resultado` | Revisa el prompt — debe pedir que use esa variable |
| `JSONDecodeError` | La respuesta del LLM no es el formato esperado | El LLM mezclo texto con codigo. Revisa el prompt |

---

## 8. Setup rapido para depurar

Copia estas 3 lineas al principio de cualquier ejercicio para activar el logging:

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.info
```

Despues, usa `log()` como si fuera `print()`:

```python
log(f"Prompt tiene {len(context)} caracteres")
log(f"Respuesta: {response.choices[0].message.content[:200]}...")
log(f"Codigo generado:\n{code}")
```

Todo aparece en la terminal de VS Code.

---

## Resumen

| Quieres ver... | Usa esto |
|---|---|
| Cualquier cosa en la terminal | `logging.info(...)` |
| El prompt que envias al LLM | `logging.info(context)` antes de la llamada |
| La respuesta cruda del LLM | `logging.info(response.choices[0].message.content)` |
| El codigo generado | `logging.info(code)` |
| Informacion en la app (plegable) | `st.expander(...)` |
| Datos en la barra lateral | `st.sidebar.write(...)` |
