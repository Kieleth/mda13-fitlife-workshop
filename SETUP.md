# Guía de instalación

**Taller MDA13 — Analítica conversacional con GenAI**

Preparación previa a la primera sesión. Necesitas completar todos los pasos de este documento ANTES de la primera clase. Tiempo estimado: 30-45 minutos, dependiendo de tu conexión y sistema operativo.

La configuración final del entorno en VS Code (intérprete, terminal, API key) se hará en clase con el profesor. Aquí solo instalas los componentes.

Si encuentras algún problema durante la instalación, contacta al profesor con tiempo.

**Sobre la API key del LLM:** no necesitas crear ninguna cuenta ni obtener claves. El profesor te facilitará la clave API durante la sesión.

---

## Checklist rápido

Todos son necesarios salvo los indicados como opcionales.

- [ ] Visual Studio Code instalado
- [ ] Git instalado
- [ ] Cuenta en GitHub creada
- [ ] Proyecto clonado y abierto en VS Code
- [ ] Python instalado (Anaconda o Python estándar)
- [ ] Extensión Python para VS Code instalada
- [ ] Extensión GitHub Copilot instalada en VS Code
- [ ] Entorno del taller creado y dependencias instaladas
- [ ] Verificación: `streamlit run test_app.py` muestra todos los checks en verde
- [ ] Leído el enunciado del caso FitLife (`ENUNCIADO.md`)
- [ ] Cuenta en Streamlit Community Cloud (opcional, puede esperar a la sesión 4)

---

# Parte 1 — Obtener el proyecto

Los primeros 4 pasos te llevan a tener el proyecto abierto en VS Code. Una vez lo consigas, podrás seguir el resto de la guía cómodamente desde el propio editor.

---

## 1. Visual Studio Code

**Qué es:** VS Code es un editor de código gratuito desarrollado por Microsoft.

**Para qué lo usamos:** Será tu herramienta principal. Desde VS Code escribirás código Python, ejecutarás tu aplicación Streamlit y gestionarás los archivos del proyecto.

**Instalación:**

Descarga el instalador desde https://code.visualstudio.com

- **Windows:** descarga el archivo .exe. Durante la instalación, marca la casilla "Añadir a PATH" si aparece.
- **Mac:** descarga el archivo .zip, descomprímelo y arrastra Visual Studio Code a la carpeta Aplicaciones.

Abre VS Code una vez para confirmar que se ha instalado correctamente. Verás una pantalla de bienvenida. Puedes cerrarla.

---

## 2. Git

**Qué es:** Git es un sistema de control de versiones. Registra los cambios que haces en tus archivos a lo largo del tiempo, como un historial infinito de "Ctrl+Z" pero mucho más potente.

**Para qué lo usamos:** Para descargar ("clonar") el material del curso desde GitHub a tu ordenador.

> Si nunca has oído hablar de Git y quieres entender la idea general antes de instalarlo, lee [GIT_INTRO.md](GIT_INTRO.md) (5 minutos). No es imprescindible ahora — puedes leerlo después — pero te dará contexto.

**Instalación:**

- **Windows:** descarga desde https://git-scm.com. Ejecuta el instalador .exe y acepta todos los valores por defecto. Git se integrará automáticamente con VS Code.
- **Mac:** abre la aplicación "Terminal" (busca "Terminal" en Spotlight con `Cmd+Espacio`) y escribe `git --version`. Si no está instalado, macOS te ofrecerá instalarlo automáticamente (Xcode Command Line Tools). Haz clic en "Instalar" y espera a que termine.

**Verificación:**

Abre una terminal (en Windows: busca "PowerShell" en el menú de inicio; en Mac: abre "Terminal") y escribe:

```
git --version
```

Deberías ver algo como `git version 2.x.x`. Si sale un error, cierra la terminal, vuelve a abrirla e inténtalo de nuevo (a veces necesita reiniciar la terminal tras la instalación).

---

## 3. Cuenta en GitHub

**Qué es:** GitHub es una plataforma web donde se comparte código. El material de este taller está publicado ahí. También necesitarás la cuenta para activar GitHub Copilot (un asistente de programación que usaremos en clase).

**Si ya tienes cuenta en GitHub**, puedes saltar al paso 4.

**Crear una cuenta:**

1. Abre tu navegador y ve a https://github.com
2. Haz clic en el botón **"Sign up"** (esquina superior derecha).
3. Introduce tu **email** (usa uno que tengas a mano durante las sesiones del taller).
4. Crea una **contraseña**.
5. Elige un **nombre de usuario** (será tu identidad pública en GitHub, puede ser tu nombre o un alias).
6. GitHub te pedirá resolver un puzzle sencillo para verificar que eres humano. Complétalo.
7. Haz clic en **"Create account"**.
8. GitHub te enviará un **código de verificación** al email que proporcionaste. Abre tu correo, busca el email de GitHub y copia el código.
9. Introduce el código en la pantalla de verificación de GitHub.
10. En la pantalla de personalización ("What kind of work do you do?", etc.) puedes hacer clic en **"Skip personalization"** en la parte inferior. No es necesario rellenarla.

Listo. Ya tienes cuenta en GitHub.

---

## 4. Clonar el proyecto y abrirlo en VS Code

**Qué es clonar:** "Clonar" es descargar una copia completa del proyecto desde GitHub a tu ordenador. Es como descargar un ZIP, pero con la ventaja de que Git mantiene un historial de cambios y te permite actualizar fácilmente si el profesor sube modificaciones.

### Paso a paso:

1. **Abre VS Code.**

2. **Abre la terminal integrada de VS Code:**
   - En el menú superior: `Terminal` > `New Terminal`
   - O usa el atajo de teclado: `` Ctrl+` `` (Windows) / `` Cmd+` `` (Mac)
   - Aparecerá un panel en la parte inferior de VS Code con una línea de comandos.

3. **Navega a la carpeta donde quieres guardar el proyecto.** Por ejemplo, para guardarlo en tu escritorio:
   - **Windows:** escribe `cd Desktop` y pulsa Enter.
   - **Mac:** escribe `cd ~/Desktop` y pulsa Enter.
   
   (Puedes elegir cualquier otra carpeta. Lo importante es que sepas dónde está.)

4. **Clona el repositorio.** Copia y pega este comando exacto en la terminal y pulsa Enter:

   ```
   git clone https://github.com/Kieleth/mda13-fitlife-workshop.git
   ```

   Verás algo como:
   ```
   Cloning into 'mda13-fitlife-workshop'...
   remote: Enumerating objects: ...
   Receiving objects: 100% ...
   ```

   Esto crea una carpeta llamada `mda13-fitlife-workshop` con todo el material del taller.

5. **Abre la carpeta del proyecto en VS Code:**
   - En VS Code, ve a `File` > `Open Folder...` (en Mac: `File` > `Open Folder...` o `Cmd+O`)
   - Navega hasta la carpeta `mda13-fitlife-workshop` (estará en tu escritorio o donde hayas clonado).
   - Selecciona la carpeta y haz clic en "Abrir" / "Open".
   - Si VS Code pregunta "Do you trust the authors of the files in this folder?", haz clic en **"Yes, I trust the authors"**.

6. **Verifica que ves los archivos del proyecto.** En la barra lateral izquierda de VS Code debería aparecer el explorador de archivos con:
   - `exercises/` (ejercicios guiados)
   - `test_app.py`
   - `SETUP.md` (este archivo)
   - `ENUNCIADO.md`
   - `data/`
   - etc.

**Si no usas git:** el profesor puede facilitarte un ZIP. Descomprímelo y abre la carpeta resultante en VS Code con `File` > `Open Folder...`.

---

> **A partir de aquí, trabaja desde VS Code.** Puedes abrir este mismo archivo (`SETUP.md`) en VS Code para seguir las instrucciones sin salir del editor. Para verlo con formato, haz clic derecho sobre `SETUP.md` en el explorador lateral y selecciona "Open Preview" (o pulsa `Ctrl+Shift+V` / `Cmd+Shift+V`).

---

# Parte 2 — Preparar el entorno de desarrollo

Ya tienes el proyecto abierto en VS Code. Ahora vamos a instalar Python, las extensiones y las librerías necesarias.

---

## 5. Python

**Qué es:** Python es el lenguaje de programación que usaremos. Es el estándar en análisis de datos e inteligencia artificial. Cuando instalas Python, instalas el "intérprete": el motor que lee tu código y lo ejecuta.

**Para qué lo usamos:** Todo el código del taller está escrito en Python: la aplicación web (Streamlit), las llamadas a la API del LLM y la lógica de análisis de datos.

### Opción A: Anaconda Distribution (recomendada)

Anaconda incluye Python junto con librerías científicas preinstaladas (pandas, numpy...) y un gestor de entornos llamado conda. Es la opción recomendada porque evita problemas de compatibilidad.

**Importante:** instala "Anaconda Distribution", NO "Miniconda". Son productos distintos.

1. Descarga desde https://www.anaconda.com/download
2. Selecciona tu sistema operativo y sigue el asistente con las opciones por defecto.
   - **Windows:** ejecuta el instalador .exe. Cuando pregunte si quieres añadir Anaconda a PATH, selecciona "Sí" (aunque el instalador no lo recomiende, para este taller es más práctico).
   - **Mac:** descarga el instalador .pkg y sigue las instrucciones.

Ocupará en torno a 3 GB en disco. Si tu espacio es limitado, usa la Opción B.

### Opción B: Python estándar

La instalación oficial desde python.org. Mucho más ligera (~100 MB) y suficiente para el taller.

1. Descarga desde https://www.python.org/downloads (versión 3.11 o superior).
   - **Windows:** ejecuta el instalador .exe. **Marca la casilla "Add Python to PATH"** en la primera pantalla (es fácil pasarla por alto y es imprescindible). Luego "Install Now".
   - **Mac:** descarga el archivo .pkg y sigue el asistente.

### Verificación (ambas opciones)

Abre la terminal integrada de VS Code (`Terminal` > `New Terminal` o `` Ctrl+` `` / `` Cmd+` ``) y escribe:

```
python --version
```

Deberías ver algo como `Python 3.11.x` o superior. Si Mac responde "command not found", prueba con `python3 --version`.

---

## 6. Extensión Python para VS Code

**Qué es:** Una extensión que añade funcionalidades a VS Code. La extensión de Python (Microsoft) le enseña al editor a "entender" Python: colorea la sintaxis, detecta errores mientras escribes y ofrece autocompletado.

**Sin esta extensión, VS Code trata tus archivos .py como texto plano.**

**Instalación:**

1. En VS Code, en la barra lateral izquierda, haz clic en el icono de extensiones (cuatro cuadrados, o pulsa `Ctrl+Shift+X` en Windows / `Cmd+Shift+X` en Mac).
2. En el buscador que aparece arriba, escribe "Python".
3. El primer resultado debería ser **"Python"** de **Microsoft** (identificador: `ms-python.python`). Haz clic en **"Install"**.

> Lo que se configurará en clase: la extensión necesita saber qué intérprete de Python usar. Esa vinculación la haremos juntos.

---

## 7. GitHub Copilot (extensión VS Code)

**Qué es:** Un asistente de programación basado en inteligencia artificial. Mientras escribes código, Copilot sugiere líneas o bloques completos en tiempo real. También tiene un chat integrado donde puedes hacerle preguntas sobre tu código.

**Para qué lo usamos:** Como herramienta de apoyo para acelerar la escritura de código y resolver dudas de sintaxis.

**Importante:** Copilot estará desactivado por defecto durante las sesiones. El profesor indicará en qué momentos activarlo. El objetivo del taller es que entiendas qué hace el código, no que lo generes automáticamente sin comprenderlo.

**Instalación:**

1. En VS Code, ve a extensiones (`Ctrl+Shift+X` / `Cmd+Shift+X`) y busca "GitHub Copilot".
2. Instala la extensión **GitHub Copilot** (identificador: `GitHub.copilot`). Se instalará también GitHub Copilot Chat automáticamente.
3. VS Code te pedirá que inicies sesión con tu cuenta de GitHub. Haz clic en **"Sign in"** y autoriza el acceso en el navegador que se abrirá.

**Acceso gratuito:** GitHub Copilot ofrece un plan gratuito con límite de uso mensual, más que suficiente para este taller. Si te solicita un plan de pago, verifica que estás seleccionando el tier "Free".

---

## 8. Crear el entorno del taller e instalar dependencias

**Qué es un entorno:** Un espacio aislado donde instalamos las librerías de Python que necesita este taller, sin afectar al resto de tu ordenador. Piensa en ello como una "caja" separada donde ponemos solo lo que necesitamos.

**Qué son las dependencias:** Librerías de Python escritas por otros desarrolladores que nuestro código utiliza. Las principales son:
- **Streamlit** — para crear la aplicación web
- **OpenAI** — para conectar con el modelo de lenguaje
- **pandas** — para analizar datos

### Con Anaconda (si instalaste la Opción A)

Abre la terminal de VS Code (`Terminal` > `New Terminal`) y ejecuta estos comandos **uno a uno** (copia, pega, Enter, espera a que termine, siguiente):

```
conda create -n mda13 python=3.12 -y
```

```
conda activate mda13
```

```
pip install -r requirements.txt
```

Sabrás que el entorno está activo cuando veas `(mda13)` al inicio de la línea de la terminal.

**Importante:** cada vez que abras una terminal nueva para trabajar en el taller, necesitas activar el entorno:

```
conda activate mda13
```

### Con Python estándar (si instalaste la Opción B)

Abre la terminal de VS Code y ejecuta:

- **Mac/Linux:**
  ```
  python3 -m venv mda13_env
  source mda13_env/bin/activate
  pip install -r requirements.txt
  ```

- **Windows:**
  ```
  python -m venv mda13_env
  mda13_env\Scripts\activate
  pip install -r requirements.txt
  ```

---

## 9. Verificar que todo funciona

Este es el paso más importante. Si esta verificación pasa, todo está listo.

Asegúrate de que el entorno está activado (ves `(mda13)` o `(mda13_env)` al inicio de la línea en la terminal). Luego ejecuta:

```
streamlit run test_app.py
```

Se abrirá una página en el navegador con una serie de checks. **Si todos aparecen en verde, tu entorno está listo.**

Para cerrar la aplicación, vuelve a la terminal de VS Code y pulsa `Ctrl+C`.

---

## 10. Leer el enunciado del caso

En el explorador lateral de VS Code verás el archivo `ENUNCIADO.md`. Haz clic sobre él para abrirlo (para verlo con formato, clic derecho > "Open Preview" o `Ctrl+Shift+V` / `Cmd+Shift+V`).

Léelo antes de la primera sesión para familiarizarte con los datos y la pregunta que intentaremos responder.

---

## 11. Cuenta en Streamlit Community Cloud (opcional)

**Qué es:** Streamlit Community Cloud es un servicio gratuito que permite publicar tu app para que cualquiera pueda acceder a ella desde un navegador, sin necesidad de servidores propios.

**Para qué lo usamos:** Durante las tres primeras sesiones trabajarás en local. En la cuarta sesión es posible que despleguemos la aplicación a la nube.

**Registro:** crea una cuenta en https://share.streamlit.io. Puedes registrarte directamente con tu cuenta de GitHub (recomendado). Si no la creas ahora, podrás hacerlo antes de la cuarta sesión.

---

## Resumen

Lo que debes tener antes de la primera sesión:

- VS Code instalado
- Git instalado (`git --version` funciona)
- Cuenta en GitHub creada
- Proyecto clonado y abierto en VS Code
- Python funcionando (`python --version` muestra 3.11+)
- Extensión Python instalada en VS Code
- Extensión GitHub Copilot instalada y vinculada a tu cuenta
- Entorno `mda13` creado y dependencias instaladas
- `streamlit run test_app.py` todo en verde
- Enunciado del caso FitLife leído (`ENUNCIADO.md`)

Lo que NO necesitas hacer antes de venir:

- Configurar el intérprete de Python en VS Code (lo haremos juntos)
- Crear una cuenta en un LLM ni obtener API keys (te las proporcionará el profesor)

---

## Problemas frecuentes

**"conda no se reconoce como comando"**
En Windows, usa **Anaconda Prompt** (se instala con Anaconda) en lugar de la terminal normal. O cierra VS Code y vuélvelo a abrir tras instalar Anaconda.

**"python no se reconoce como comando"**
Asegúrate de que el entorno está activado: `conda activate mda13`. Si ves `(mda13)` al inicio de la línea, está activo. Si usaste Python estándar y no tienes entorno activo, prueba `python3 --version`.

**"pip no se reconoce como comando"**
Con el entorno activado, prueba `python -m pip install ...` en lugar de `pip install ...`

**"git no se reconoce como comando"**
En Windows, cierra y vuelve a abrir la terminal después de instalar Git. En Mac, asegúrate de que aceptaste la instalación de Xcode Command Line Tools.

**Streamlit no abre el navegador**
Copia la URL que aparece en la terminal (normalmente `http://localhost:8501`) y pégala en el navegador manualmente.

**Anaconda ocupa demasiado espacio**
Usa la Opción B (Python estándar). Es más ligera y suficiente para el taller.

**VS Code no reconoce conda en la terminal**
En Windows, abre Anaconda Prompt (fuera de VS Code), activa el entorno, y ejecuta los comandos desde ahí. Alternativamente, cierra y reabre VS Code después de instalar Anaconda para que detecte la nueva configuración.
