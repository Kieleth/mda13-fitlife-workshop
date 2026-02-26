# Sesión 1 — Repaso completo

Este documento recoge todo lo que hicimos en la sesión 1. Si te perdiste en algún paso, aquí tienes las explicaciones y el código resuelto para cada ejercicio.

Léelo con calma. No hace falta memorizar nada — es una referencia para consultar cuando lo necesites.

---

## La terminal

La terminal es una ventana donde escribes comandos de texto en vez de hacer clic con el ratón. Todo lo que haces con la terminal también se puede hacer con botones, pero la terminal es más rápida cuando sabes qué escribir.

**Cómo abrir la terminal en VS Code:**
- Menú: `Terminal` → `New Terminal`
- Atajo: `Ctrl + `` ` (la tecla al lado del 1, la de los acentos)

**Cosas útiles:**
- Para **ejecutar** un comando: escríbelo y pulsa `Enter`.
- Para **parar** un programa que está corriendo (como Streamlit): pulsa `Ctrl+C`.
- Para **copiar** texto en la terminal: selecciónalo con el ratón y pulsa `Ctrl+C` (Windows) o `Cmd+C` (Mac).
- Para **pegar** texto en la terminal: `Ctrl+V` (Windows) o `Cmd+V` (Mac). En algunas terminales: `Ctrl+Shift+V`.
- La **flecha arriba** repite el último comando que escribiste.

**El entorno `(mda13)`:**

Cuando ves `(mda13)` al principio de la línea de la terminal, significa que el entorno de Python del taller está activo. Si no lo ves, escribe:

```
conda activate mda13
```

---

## ¿Qué es Streamlit?

Streamlit es una librería de Python que convierte código en una página web. Cada línea de código añade un elemento a la página: un título, un texto, una tabla, un gráfico, un chat...

No necesitas saber HTML ni CSS. Solo Python.

**Funciones clave:**

| Función | Qué hace |
|---------|----------|
| `st.title("texto")` | Título grande |
| `st.subheader("texto")` | Subtítulo |
| `st.write("texto")` | Texto normal (acepta **Markdown**: `**negrita**`, `*cursiva*`) |
| `st.dataframe(df)` | Muestra una tabla interactiva |
| `st.chat_input("texto")` | Campo de texto para que el usuario escriba |
| `st.chat_message("user")` | Bocadillo de chat del usuario |
| `st.chat_message("assistant")` | Bocadillo de chat del asistente |
| `st.divider()` | Línea horizontal de separación |

**Cómo ejecutar una app:**

```
streamlit run exercises/paso_0.py
```

Streamlit abre una pestaña en el navegador. Cada vez que guardas el archivo (`Ctrl+S`), la web se actualiza automáticamente.

---

## ¿Qué es pandas?

pandas es una librería de Python para trabajar con datos en tablas (filas y columnas). Es como Excel pero en código.

**Función clave:**

```python
import pandas as pd

df = pd.read_csv("data/fitlife_members.csv")
```

Esto carga un archivo CSV y crea un DataFrame (`df`): una tabla que puedes explorar y manipular.

**Funciones útiles sobre un DataFrame:**

| Función | Qué devuelve |
|---------|-------------|
| `len(df)` | Número de filas |
| `len(df.columns)` | Número de columnas |
| `list(df.columns)` | Lista con los nombres de las columnas |
| `df.head()` | Las primeras 5 filas |
| `df.head(10)` | Las primeras 10 filas |
| `df.describe()` | Estadísticas básicas (media, mín, máx...) |
| `df["columna"].value_counts()` | Cuenta cuántas filas hay de cada valor |

---

## ¿Qué es un LLM?

Un LLM (Large Language Model) es un programa que ha leído cantidades enormes de texto: páginas web, libros, artículos, código. De todo eso aprendió patrones de lenguaje.

Cuando le haces una pregunta, no busca la respuesta en ningún sitio. Genera texto palabra por palabra basándose en los patrones que aprendió. Es como un compañero que ha leído todo internet pero **no tiene calculadora**.

Retén eso: **no tiene calculadora**. Entiende el lenguaje, pero no puede calcular sobre datos que no ha visto.

---

## ¿Qué es una API?

Una API es una puerta de entrada a un servicio externo. En nuestro caso:

```
Tu app → envía mensaje → API de OpenAI → modelo genera respuesta → tu app la recibe
```

Para usar la API necesitas una **API key** (una contraseña que identifica quién hace la petición). La API key va en un archivo `.env` que el código lee automáticamente pero que nunca se sube a internet.

---

## ¿Qué es `with`?

En Python, `with` seguido de dos puntos crea un bloque. Todo lo que va **indentado** (con espacios) debajo pertenece a ese bloque:

```python
with st.chat_message("user"):
    st.write("hola")       # ← dentro del bocadillo
    st.write("adiós")      # ← también dentro

st.write("fuera")          # ← esto ya NO está en el bocadillo
```

Si algo no aparece donde esperabas, revisa la indentación.

---

## Ejercicios resueltos

### paso_0 — Arranca la app

**El error:** `streamlt` en vez de `streamlit` (falta la `i`).

**Código corregido:**

```python
import streamlit as st

st.title("Hola Mundo")
st.write("Si ves esto en el navegador, tu primer app web funciona.")
```

**Lección:** los errores de Python te dicen exactamente qué va mal y en qué línea. Léelos de abajo arriba.

---

### paso_1 — Muestra información en pantalla

**El reto:** rellenar los huecos `___`.

**Código corregido:**

```python
import streamlit as st

st.title("FitLife Dashboard")

st.subheader("Análisis de socios")

st.write("Bienvenido al panel de control de FitLife.")
```

**Lección:** cada función `st.algo()` pone un elemento en la página. El orden importa.

---

### paso_2 — Carga datos

**El error:** la ruta del archivo es `"fitlife_members.csv"` pero el archivo está dentro de la carpeta `data/`.

**Código corregido (línea 69):**

```python
df = pd.read_csv("data/fitlife_members.csv")
```

**Lección:** las rutas de archivo son como direcciones. Si el archivo está en una subcarpeta, la ruta debe incluirla.

---

### paso_3 — Explora los dos datasets

**El reto:** cargar el segundo CSV y rellenar los huecos.

**Código corregido (líneas 72-77):**

```python
# Dataset 2: contexto mensual
df_context = pd.read_csv("data/fitlife_context.csv")

st.subheader("Contexto mensual")
st.write(f"**{len(df_context)}** filas, **{len(df_context.columns)}** columnas")
st.write("Columnas:", list(df_context.columns))
st.dataframe(df_context.head())
```

**Lección:** cuando ves un patrón resuelto en el código, cópialo y adapta los nombres. Programar es mucho copiar y adaptar.

---

### paso_4 — Habla con la app

**El reto:** completar el eco del asistente.

**Código corregido (línea 87):**

```python
with st.chat_message("assistant"):
    st.write(f"Has dicho: {prompt}")
```

**Lección:** `with st.chat_message("assistant"):` crea un bocadillo. Todo lo indentado debajo aparece dentro.

---

### paso_5 — Conecta el cerebro

**El reto:** crear el cliente de OpenAI. También necesitas el archivo `.env`.

**El archivo `.env` (en la raíz del proyecto):**

```
OPENAI_API_KEY=tu-clave-aquí
```

**Código corregido (línea 102):**

```python
client = OpenAI()
```

**Lección:** la API key nunca va directamente en el código. Va en `.env`, que es un archivo que el código lee pero que no se sube a internet.

---

### paso_6 — Pregúntale sobre los datos

**No hay nada que arreglar.** Tu reto era probar 5 preguntas y descubrir cuáles el LLM respondía bien y cuáles se inventaba.

**Resultados esperados:**

| Pregunta | ¿Correcta? | Por qué |
|----------|------------|---------|
| 1. ¿Cuántos registros? | Sí | El número (16.334) está explícito en el prompt |
| 2. ¿Qué planes? | Parcial | Puede listar los que ve en las 5 filas de muestra |
| 3. ¿Centro con más socios? | No fiable | Solo ve 5 filas, no puede contar sobre 16.334 |
| 4. ¿Tasa de churn del básico? | Inventada | No tiene calculadora, se inventa el número |
| 5. ¿Bajar el precio? | Genérica | Da consejos de consultoría sin datos reales |

**Lección:** el LLM entiende el lenguaje perfectamente pero no puede calcular sobre datos que no ha visto. Cuando no sabe, se inventa la respuesta con total confianza. Esto se llama **alucinación**.

---

### paso_7 — Bonus: prompt enriquecido

**El reto:** rellenar los 4 huecos del prompt con las variables que ya estaban calculadas.

**Código corregido (líneas 165-174):**

```python
Distribución por plan:
{planes}

Distribución por centro:
{centros}

Distribución por estado:
{status}

Distribución por canal de captación:
{canales}
```

**Lección:** dar más contexto al LLM mejora las respuestas cualitativas, pero las numéricas siguen sin ser fiables. El LLM sigue sin tener calculadora.

---

## ¿Qué viene en la sesión 2?

Si el LLM no puede calcular... ¿lo descartamos? No. Porque sí entiende la pregunta. Sabe que "tasa de churn del plan básico" significa "filtra por plan basic, cuenta los churned, divide por el total".

¿Y si en vez de pedirle la respuesta, le pedimos que **escriba el código** para calcularla? Y luego ejecutamos ese código contra los datos reales.

Eso es la sesión 2. El LLM traduce la pregunta a Python. Python calcula. El número es real.
