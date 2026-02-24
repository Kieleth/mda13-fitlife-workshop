# MDA13 — Analítica conversacional con GenAI

Taller práctico de 4 sesiones donde construirás, paso a paso, una aplicación web que permite hacerle preguntas en lenguaje natural a un dataset real y obtener respuestas basadas en datos.

El caso de estudio es **FitLife**, una red de gimnasios con un problema de churn. Tu aplicación usará un LLM (modelo de lenguaje) para analizar sus datos y ayudar a responder una pregunta de negocio real.

---

## Qué hay en este repositorio

| Archivo | Qué es |
|---------|--------|
| `exercises/` | Ejercicios guiados (paso 0 a 6) que irás completando en clase |
| `data/` | Los datasets de FitLife (miembros + contexto mensual) |
| `test_app.py` | App de verificación — confirma que tu entorno está bien configurado |
| `ENUNCIADO.md` | El caso de negocio: contexto, datos disponibles y la pregunta a resolver |
| `PREGUNTAS_TEST.md` | Preguntas para probar tu aplicación de analítica conversacional |
| `SETUP.md` | Guía de instalación paso a paso |
| `GIT_INTRO.md` | Qué es Git y GitHub en 5 minutos (lectura opcional) |
| `SESION1_CHECKLIST.md` | Checklist para la primera sesión |

---

## Cómo empezar

1. **Sigue la guía de instalación:** abre [`SETUP.md`](SETUP.md) y completa todos los pasos. Te llevará unos 30-45 minutos.

2. **Lee el enunciado del caso:** abre [`ENUNCIADO.md`](ENUNCIADO.md) para entender el negocio, los datos y la pregunta que guiará el taller.

3. **Verifica tu entorno:** ejecuta `streamlit run test_app.py` y confirma que todo aparece en verde.

4. **Ven a clase** con todo instalado. El profesor hará la configuración final contigo. Los ejercicios de la carpeta `exercises/` los haremos juntos en sesión.

---

## Ejercicios (sesión 1)

Cada ejercicio es un archivo Python que puedes ejecutar con `streamlit run exercises/paso_X.py` (desde la raíz del proyecto). Todos tienen algo que arreglar o completar — lee las instrucciones al inicio de cada archivo.

| Ejercicio | Qué construyes | El reto | Pista |
|-----------|---------------|---------|-------|
| `paso_0.py` | Tu primera app web | La app no arranca. Lee el error en la terminal. | El problema está en la línea del `import`. Compara lo que pone con el nombre real de la librería. |
| `paso_1.py` | Título y texto en pantalla | Hay líneas incompletas marcadas con `___`. | Mira las funciones que se explican en el comentario de arriba: `st.subheader()` y `st.write()`. |
| `paso_2.py` | Cargar un archivo de datos | La app arranca pero falla al leer el CSV. | Fíjate en dónde están los archivos CSV (carpeta `data/`) y en la ruta que usa el código. |
| `paso_3.py` | Explorar los dos datasets | El primer dataset se carga, pero el segundo no. Completa las líneas con `___`. | Ya tienes el patrón en las líneas de arriba — el segundo dataset es `data/fitlife_context.csv`. |
| `paso_4.py` | Un chat que repite lo que escribes | El chat del usuario funciona, pero el asistente no responde. | Completa la línea `___` dentro del bloque `with st.chat_message("assistant")`. |
| `paso_5.py` | Conectar un LLM de verdad | Falta crear el cliente de OpenAI. Necesitarás una API key en un archivo `.env`. | La línea que falta es `OpenAI()`. La API key te la dará el profesor. Mira `.env.template` para el formato del archivo. |
| `paso_6.py` | Preguntarle al LLM sobre los datos | Nada está roto. Tu reto es probar preguntas y evaluar si las respuestas son correctas. | Prueba preguntas concretas ("¿cuántos registros hay?") y preguntas analíticas ("¿cuál es la tasa de churn?"). Compara las respuestas con lo que ves en los datos reales. ¿Qué descubres? |

**La idea clave:** al final del paso 6 verás que el LLM se inventa números cuando le preguntas cosas que requieren calcular sobre los datos. Solo ve una muestra de 5 filas, así que adivina el resto. Esto es exactamente el problema que resolveremos en las siguientes sesiones.

---

## Requisitos previos

No se requiere experiencia en programación. El taller está diseñado para que sigas las instrucciones paso a paso. Todo el software necesario es gratuito.

Lo único que necesitas traer: un portátil con conexión a internet.
