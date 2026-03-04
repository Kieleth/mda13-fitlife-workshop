# Sesión 2 — Repaso completo

Este documento recoge todo lo que hicimos en la sesión 2. Si te perdiste en algún paso, aquí tienes las explicaciones y el código resuelto.

---

## La idea clave de la sesión 2

En la sesión 1 descubrimos que el LLM se inventaba los números. No puede calcular sobre 16.334 filas que no ha visto.

La solución: en vez de pedirle **la respuesta**, le pedimos **el código** para calcularla. Python ejecuta el código contra los datos reales. El resultado es correcto.

Esto se llama **text-to-code**: el LLM traduce lenguaje natural a código Python.

---

## Conceptos nuevos

### exec()

Python tiene una función que ejecuta texto como si fuera código:

```python
codigo = "x = 2 + 3"
espacio = {}
exec(codigo, espacio)
print(espacio["x"])  # → 5
```

Le pasamos un diccionario (`espacio`) donde el código guarda sus variables. Así podemos leer el resultado después.

### Expresiones regulares (regex)

El LLM devuelve el código envuelto en un bloque Markdown:

````
```python
resultado = len(df_members)
```
````

Necesitamos extraer solo el código de dentro. Usamos una "receta" (regex):

```python
import re
match = re.search(r"```(?:python)?\n(.*?)```", texto, re.DOTALL)
codigo = match.group(1)
```

No hace falta entenderla — es una receta para extraer código de bloques Markdown.

### try / except

Maneja errores sin que la app se rompa:

```python
try:
    # código que puede fallar
    exec(code, exec_globals)
except Exception as e:
    # qué hacer si falla
    st.error(f"Error: {e}")
```

### st.expander()

Un bloque que se abre y cierra. Para mostrar información sin saturar la pantalla:

```python
with st.expander("Ver detalles"):
    st.write("Esto está oculto hasta que haces clic")
```

---

## Ejercicios resueltos

### paso_8 — Text-to-code

**El reto:** completar el prompt del sistema para que el LLM genere código.

**Código corregido (línea 111):**

```python
system_prompt = f"""Genera solo código Python/pandas que responda a la pregunta del usuario.
```

Cualquier variación que diga "genera código" funciona.

**Lección:** el cambio de "responde con texto" a "genera código Python" está en UNA línea del prompt. Mismo modelo, misma API.

---

### paso_9 — Ejecutar el código

**El reto:** extraer el código y ejecutarlo.

**Código corregido (línea 145 — regex):**

```python
match = re.search(r"```(?:python)?\n(.*?)```", generated, re.DOTALL)
```

**Código corregido (línea 168 — exec):**

```python
exec(code, exec_globals)
```

**Descubrimiento importante:** si preguntas "¿Cuál es la tasa de churn del plan básico?", el LLM puede usar `'básico'` en vez de `'basic'`. El LLM no conoce los valores reales de las columnas — solo los nombres. Para que funcione, hay que decirle en el prompt que el plan básico se llama `'basic'` en los datos.

**Lección:** text-to-code es potente, pero el LLM necesita conocer el vocabulario de los datos.

---

### paso_10 — Manejo de errores

**El reto:** tres huecos para manejar errores y mostrar transparencia.

**Código corregido (línea 150 — expander):**

```python
with st.expander("Ver código generado"):
```

**Código corregido (línea 176 — error):**

```python
st.error(f"Error al ejecutar el código: {e}")
```

**Código corregido (línea 184 — expander de detalles):**

```python
with st.expander("Detalles del error"):
```

**Lección:** `try/except` evita que la app se rompa. `st.expander` muestra el código para que el usuario pueda verificar qué se ejecutó. Transparencia.

---

### paso_11 — Autocorrección (bonus)

**Sin huecos.** Este paso funciona tal cual.

El código implementa un bucle de reintentos: si el código generado falla, le envía el error al LLM y le pide que corrija. Hasta 3 intentos.

**Lección:** el LLM puede corregir sus propios errores si le das feedback. Pero hay errores que no se corrigen solos (como pedir una columna que no existe si el LLM no sabe los nombres correctos).

---

## Las 5 preguntas — comparativa sesión 1 vs sesión 2

| Pregunta | Sesión 1 (paso_6) | Sesión 2 (paso_9/10) |
|----------|-------------------|----------------------|
| ¿Cuántos registros? | Correcto (estaba en el prompt) | Correcto (código lo calcula) |
| ¿Qué planes hay? | Parcial | Correcto con conteos |
| ¿Centro con más socios? | Inventado | Correcto: southgate |
| ¿Churn del básico? | Inventado (diferente cada vez) | Correcto: ~6.85% |
| ¿Bajar el precio? | Genérica, sin datos | Mejor, pero sigue siendo difícil |

---

## Errores comunes y soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `AuthenticationError` | API key mal configurada | Revisar `.env`, sin espacios |
| `ModuleNotFoundError: openai` | Entorno no activo | `conda activate mda13` |
| `RateLimitError` | Muchas peticiones seguidas | Esperar unos segundos |
| El código genera `'básico'` en vez de `'basic'` | Prompt sin valores de columnas | Añadir valores reales al prompt |
| `KeyError: 'columna_inventada'` | El LLM inventa columnas | Incluir lista de columnas en el prompt |
| La app se congela | exec() tardando | Esperar — preguntas complejas tardan |
