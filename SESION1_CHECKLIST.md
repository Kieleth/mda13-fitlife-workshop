# Sesión 1 — Checklist de inicio

Antes de empezar la sesión, verifica que todo funciona.

## Antes de clase (hazlo en casa)

- [ ] Entorno `mda13` creado y dependencias instaladas (ver `SETUP.md`)
- [ ] VS Code instalado con extensión de Python, intérprete apuntando a `mda13`
- [ ] Proyecto descargado (repositorio clonado o zip descomprimido)
- [ ] `streamlit run test_app.py` muestra todos los checks en verde
- [ ] Leído el enunciado del caso FitLife (`ENUNCIADO.md`)

## Al empezar la clase

- [ ] Abrir VS Code en la carpeta del proyecto
- [ ] Abrir una terminal en VS Code
- [ ] Ejecutar `streamlit run exercises/paso_0.py` — verás un error (es intencionado, lo arreglamos juntos)

## Lo que haremos en la sesión 1

1. Completar los ejercicios guiados (paso 0 a 6, más paso 7 bonus si hay tiempo)
2. Conocer el caso FitLife y la pregunta clave
3. Conectar un LLM a nuestra app
4. Probar preguntas y documentar qué funciona y qué falla
5. Descubrir por qué el LLM se inventa las respuestas

## Lo que necesitarás durante la clase

- El profesor compartirá una API key de OpenAI al inicio de la sesión
- Crea un archivo `.env` en la carpeta del proyecto con:

```
OPENAI_API_KEY=la-key-que-te-de-el-profesor
```

## Al final de la sesión deberás tener

- [ ] App Streamlit funcionando con chat de IA integrado
- [ ] Lista personal de preguntas probadas: cuáles funcionan, cuáles fallan, y por qué crees que fallan
- [ ] Reflexión sobre las limitaciones de enviar datos directamente al LLM

El profesor compartirá el código de referencia de la sesión 1 al final de la clase. Ese código es el punto de partida de la sesión 2.

## Si algo no funciona

Avisa al profesor antes de la sesión si puedes. Si no, al inicio de la clase verificaremos juntos.
