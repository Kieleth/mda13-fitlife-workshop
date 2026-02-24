# Sesion 1 — Checklist de inicio

Antes de empezar la sesion, verifica que todo funciona.

## Antes de clase (hazlo en casa)

- [ ] Entorno `mda13` creado y dependencias instaladas (ver `SETUP.md`)
- [ ] VS Code instalado con extension de Python, interprete apuntando a `mda13`
- [ ] Proyecto descargado (repositorio clonado o zip descomprimido)
- [ ] `streamlit run test_app.py` muestra todos los checks en verde
- [ ] Leido el caso FitLife (`CASO_FITLIFE.md`)

## Al empezar la clase

- [ ] Abrir VS Code en la carpeta del proyecto
- [ ] Abrir una terminal en VS Code
- [ ] Ejecutar `streamlit run app.py` — debe abrir el dashboard de FitLife
- [ ] Verificar que ves los graficos y los filtros funcionan

## Lo que haremos en la sesion 1

1. Explorar el dashboard (ya hecho, lo explicamos)
2. Conocer el caso FitLife y la pregunta clave
3. Anadir un chat con IA al dashboard
4. Probar 10 preguntas y documentar que funciona y que falla
5. Mejorar el prompt y volver a probar

## Lo que necesitaras durante la clase

- El profesor compartira una API key de OpenAI al inicio de la sesion
- Crea un archivo `.env` en la carpeta del proyecto con:

```
OPENAI_API_KEY=la-key-que-te-de-el-profesor
```

## Al final de la sesion deberas tener

- [ ] App Streamlit funcionando con chat de IA integrado
- [ ] Lista personal de las 10 preguntas probadas: cuales funcionan, cuales fallan, y por que crees que fallan
- [ ] Prompt enriquecido documentado (que anadiste y que efecto tuvo)

El profesor compartira el codigo de referencia de la sesion 1 al final de la clase. Ese codigo es el punto de partida de la sesion 2.

## Si algo no funciona

Avisa al profesor antes de la sesion si puedes. Si no, al inicio de la clase verificaremos juntos.
