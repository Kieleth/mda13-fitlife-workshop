# Cómo actualizar el proyecto

El profesor sube material nuevo al repositorio entre sesiones. Para descargarlo a tu ordenador, solo necesitas un comando.

---

## Paso a paso

1. **Abre VS Code** con el proyecto del taller (la carpeta `mda13-fitlife-workshop`).

2. **Abre la terminal** de VS Code:
   - Menú: `Terminal` → `New Terminal`
   - O atajo: `` Ctrl+` `` (Windows) / `` Cmd+` `` (Mac)

3. **Activa el entorno** (si no está activo):
   ```
   conda activate mda13
   ```
   Deberías ver `(mda13)` al principio de la línea.

4. **Descarga las actualizaciones:**
   ```
   git pull
   ```
   Verás algo como:
   ```
   remote: Enumerating objects: ...
   Updating abc1234..def5678
   Fast-forward
    extras/opcional_analisis.py  | 80 ++++++++++
    exercises2/paso_8.py         | 90 +++++++++++
    ...
   ```
   Eso significa que se han descargado archivos nuevos. Ya está.

5. **Verifica** que ves las carpetas nuevas en el explorador de archivos de VS Code (panel izquierdo):
   - `extras/` — ejercicios opcionales
   - `exercises2/` — ejercicios de la sesión 2

---

## ¿Y si da error?

### "Already up to date"

No es un error. Significa que ya tienes la última versión. Todo bien.

### "Please commit your changes or stash them"

Significa que has modificado archivos que el profesor también ha actualizado. Solución:

1. Guarda tu trabajo: en el explorador de VS Code, copia la carpeta `exercises` y pégala como `mi_trabajo` (clic derecho → Copy, luego clic derecho → Paste).
2. Ejecuta en la terminal:
   ```
   git checkout -- .
   git pull
   ```
3. Ahora tienes: tu trabajo guardado en `mi_trabajo/` y el código actualizado en `exercises/`.

### "fatal: not a git repository"

Estás en la carpeta equivocada. Asegúrate de que VS Code tiene abierta la carpeta `mda13-fitlife-workshop` (no una carpeta padre ni una subcarpeta).

### Otros errores

Contacta al profesor. En el peor de los casos, puedes borrar la carpeta del proyecto y volver a clonar:

```
git clone https://github.com/Kieleth/mda13-fitlife-workshop.git
```

Luego recuerda volver a crear tu archivo `.env` con la API key.
