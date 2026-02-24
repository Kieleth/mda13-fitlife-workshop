# Guia de instalacion

**Taller MDA13 — Analitica conversacional con GenAI**

Preparacion previa a la primera sesion. Necesitas completar todos los pasos de este documento ANTES de la primera clase. Tiempo estimado: 30-45 minutos, dependiendo de tu conexion y sistema operativo.

La configuracion final del entorno en VS Code (interprete, terminal, API key) se hara en clase con el profesor. Aqui solo instalas los componentes.

Si encuentras algun problema durante la instalacion, contacta al profesor con tiempo.

**Sobre la API key del LLM:** no necesitas crear ninguna cuenta ni obtener claves. El profesor te facilitara la clave API durante la sesion.

---

## Checklist rapido

Todos son necesarios salvo los indicados como opcionales.

- [ ] Visual Studio Code instalado
- [ ] Git instalado
- [ ] Cuenta en GitHub creada
- [ ] Proyecto clonado y abierto en VS Code
- [ ] Python instalado (Anaconda o Python estandar)
- [ ] Extension Python para VS Code instalada
- [ ] Extension GitHub Copilot instalada en VS Code
- [ ] Entorno del taller creado y dependencias instaladas
- [ ] Verificacion: `streamlit run test_app.py` muestra todos los checks en verde
- [ ] Leido el caso FitLife (`CASO_FITLIFE.md`)
- [ ] Cuenta en Streamlit Community Cloud (opcional, puede esperar a la sesion 4)

---

# Parte 1 — Obtener el proyecto

Los primeros 4 pasos te llevan a tener el proyecto abierto en VS Code. Una vez lo consigas, podras seguir el resto de la guia comodamente desde el propio editor.

---

## 1. Visual Studio Code

**Que es:** VS Code es un editor de codigo gratuito desarrollado por Microsoft.

**Para que lo usamos:** Sera tu herramienta principal. Desde VS Code escribiras codigo Python, ejecutaras tu aplicacion Streamlit y gestionaras los archivos del proyecto.

**Instalacion:**

Descarga el instalador desde https://code.visualstudio.com

- **Windows:** descarga el archivo .exe. Durante la instalacion, marca la casilla "Anadir a PATH" si aparece.
- **Mac:** descarga el archivo .zip, descomprimelo y arrastra Visual Studio Code a la carpeta Aplicaciones.

Abre VS Code una vez para confirmar que se ha instalado correctamente. Veras una pantalla de bienvenida. Puedes cerrarla.

---

## 2. Git

**Que es:** Git es un sistema de control de versiones. Registra los cambios que haces en tus archivos a lo largo del tiempo, como un historial infinito de "Ctrl+Z" pero mucho mas potente.

**Para que lo usamos:** Para descargar ("clonar") el material del curso desde GitHub a tu ordenador.

> Si nunca has oido hablar de Git y quieres entender la idea general antes de instalarlo, lee [GIT_INTRO.md](GIT_INTRO.md) (5 minutos). No es imprescindible ahora — puedes leerlo despues — pero te dara contexto.

**Instalacion:**

- **Windows:** descarga desde https://git-scm.com. Ejecuta el instalador .exe y acepta todos los valores por defecto. Git se integrara automaticamente con VS Code.
- **Mac:** abre la aplicacion "Terminal" (busca "Terminal" en Spotlight con `Cmd+Espacio`) y escribe `git --version`. Si no esta instalado, macOS te ofrecera instalarlo automaticamente (Xcode Command Line Tools). Haz clic en "Instalar" y espera a que termine.

**Verificacion:**

Abre una terminal (en Windows: busca "PowerShell" en el menu de inicio; en Mac: abre "Terminal") y escribe:

```
git --version
```

Deberias ver algo como `git version 2.x.x`. Si sale un error, cierra la terminal, vuelve a abrirla e intentalo de nuevo (a veces necesita reiniciar la terminal tras la instalacion).

---

## 3. Cuenta en GitHub

**Que es:** GitHub es una plataforma web donde se comparte codigo. El material de este taller esta publicado ahi. Tambien necesitaras la cuenta para activar GitHub Copilot (un asistente de programacion que usaremos en clase).

**Si ya tienes cuenta en GitHub**, puedes saltar al paso 4.

**Crear una cuenta:**

1. Abre tu navegador y ve a https://github.com
2. Haz clic en el boton **"Sign up"** (esquina superior derecha).
3. Introduce tu **email** (usa uno que tengas a mano durante las sesiones del taller).
4. Crea una **contrasena**.
5. Elige un **nombre de usuario** (sera tu identidad publica en GitHub, puede ser tu nombre o un alias).
6. GitHub te pedira resolver un puzzle sencillo para verificar que eres humano. Completalo.
7. Haz clic en **"Create account"**.
8. GitHub te enviara un **codigo de verificacion** al email que proporcionaste. Abre tu correo, busca el email de GitHub y copia el codigo.
9. Introduce el codigo en la pantalla de verificacion de GitHub.
10. En la pantalla de personalizacion ("What kind of work do you do?", etc.) puedes hacer clic en **"Skip personalization"** en la parte inferior. No es necesario rellenarla.

Listo. Ya tienes cuenta en GitHub.

---

## 4. Clonar el proyecto y abrirlo en VS Code

**Que es clonar:** "Clonar" es descargar una copia completa del proyecto desde GitHub a tu ordenador. Es como descargar un ZIP, pero con la ventaja de que Git mantiene un historial de cambios y te permite actualizar facilmente si el profesor sube modificaciones.

### Paso a paso:

1. **Abre VS Code.**

2. **Abre la terminal integrada de VS Code:**
   - En el menu superior: `Terminal` > `New Terminal`
   - O usa el atajo de teclado: `` Ctrl+` `` (Windows) / `` Cmd+` `` (Mac)
   - Aparecera un panel en la parte inferior de VS Code con una linea de comandos.

3. **Navega a la carpeta donde quieres guardar el proyecto.** Por ejemplo, para guardarlo en tu escritorio:
   - **Windows:** escribe `cd Desktop` y pulsa Enter.
   - **Mac:** escribe `cd ~/Desktop` y pulsa Enter.
   
   (Puedes elegir cualquier otra carpeta. Lo importante es que sepas donde esta.)

4. **Clona el repositorio.** Copia y pega este comando exacto en la terminal y pulsa Enter:

   ```
   git clone https://github.com/Kieleth/mda13-fitlife-workshop.git
   ```

   Veras algo como:
   ```
   Cloning into 'mda13-fitlife-workshop'...
   remote: Enumerating objects: ...
   Receiving objects: 100% ...
   ```

   Esto crea una carpeta llamada `mda13-fitlife-workshop` con todo el material del taller.

5. **Abre la carpeta del proyecto en VS Code:**
   - En VS Code, ve a `File` > `Open Folder...` (en Mac: `File` > `Open Folder...` o `Cmd+O`)
   - Navega hasta la carpeta `mda13-fitlife-workshop` (estara en tu escritorio o donde hayas clonado).
   - Selecciona la carpeta y haz clic en "Abrir" / "Open".
   - Si VS Code pregunta "Do you trust the authors of the files in this folder?", haz clic en **"Yes, I trust the authors"**.

6. **Verifica que ves los archivos del proyecto.** En la barra lateral izquierda de VS Code deberia aparecer el explorador de archivos con:
   - `app.py`
   - `test_app.py`
   - `SETUP.md` (este archivo)
   - `CASO_FITLIFE.md`
   - `data/`
   - etc.

**Si no usas git:** el profesor puede facilitarte un ZIP. Descomprimelo y abre la carpeta resultante en VS Code con `File` > `Open Folder...`.

---

> **A partir de aqui, trabaja desde VS Code.** Puedes abrir este mismo archivo (`SETUP.md`) en VS Code para seguir las instrucciones sin salir del editor. Para verlo con formato, haz clic derecho sobre `SETUP.md` en el explorador lateral y selecciona "Open Preview" (o pulsa `Ctrl+Shift+V` / `Cmd+Shift+V`).

---

# Parte 2 — Preparar el entorno de desarrollo

Ya tienes el proyecto abierto en VS Code. Ahora vamos a instalar Python, las extensiones y las librerias necesarias.

---

## 5. Python

**Que es:** Python es el lenguaje de programacion que usaremos. Es el estandar en analisis de datos e inteligencia artificial. Cuando instalas Python, instalas el "interprete": el motor que lee tu codigo y lo ejecuta.

**Para que lo usamos:** Todo el codigo del taller esta escrito en Python: la aplicacion web (Streamlit), las llamadas a la API del LLM y la logica de analisis de datos.

### Opcion A: Anaconda Distribution (recomendada)

Anaconda incluye Python junto con librerias cientificas preinstaladas (pandas, numpy...) y un gestor de entornos llamado conda. Es la opcion recomendada porque evita problemas de compatibilidad.

**Importante:** instala "Anaconda Distribution", NO "Miniconda". Son productos distintos.

1. Descarga desde https://www.anaconda.com/download
2. Selecciona tu sistema operativo y sigue el asistente con las opciones por defecto.
   - **Windows:** ejecuta el instalador .exe. Cuando pregunte si quieres anadir Anaconda a PATH, selecciona "Si" (aunque el instalador no lo recomiende, para este taller es mas practico).
   - **Mac:** descarga el instalador .pkg y sigue las instrucciones.

Ocupara en torno a 3 GB en disco. Si tu espacio es limitado, usa la Opcion B.

### Opcion B: Python estandar

La instalacion oficial desde python.org. Mucho mas ligera (~100 MB) y suficiente para el taller.

1. Descarga desde https://www.python.org/downloads (version 3.11 o superior).
   - **Windows:** ejecuta el instalador .exe. **Marca la casilla "Add Python to PATH"** en la primera pantalla (es facil pasarla por alto y es imprescindible). Luego "Install Now".
   - **Mac:** descarga el archivo .pkg y sigue el asistente.

### Verificacion (ambas opciones)

Abre la terminal integrada de VS Code (`Terminal` > `New Terminal` o `` Ctrl+` `` / `` Cmd+` ``) y escribe:

```
python --version
```

Deberias ver algo como `Python 3.11.x` o superior. Si Mac responde "command not found", prueba con `python3 --version`.

---

## 6. Extension Python para VS Code

**Que es:** Una extension que anade funcionalidades a VS Code. La extension de Python (Microsoft) le ensena al editor a "entender" Python: colorea la sintaxis, detecta errores mientras escribes y ofrece autocompletado.

**Sin esta extension, VS Code trata tus archivos .py como texto plano.**

**Instalacion:**

1. En VS Code, en la barra lateral izquierda, haz clic en el icono de extensiones (cuatro cuadrados, o pulsa `Ctrl+Shift+X` en Windows / `Cmd+Shift+X` en Mac).
2. En el buscador que aparece arriba, escribe "Python".
3. El primer resultado deberia ser **"Python"** de **Microsoft** (identificador: `ms-python.python`). Haz clic en **"Install"**.

> Lo que se configurara en clase: la extension necesita saber que interprete de Python usar. Esa vinculacion la haremos juntos.

---

## 7. GitHub Copilot (extension VS Code)

**Que es:** Un asistente de programacion basado en inteligencia artificial. Mientras escribes codigo, Copilot sugiere lineas o bloques completos en tiempo real. Tambien tiene un chat integrado donde puedes hacerle preguntas sobre tu codigo.

**Para que lo usamos:** Como herramienta de apoyo para acelerar la escritura de codigo y resolver dudas de sintaxis.

**Importante:** Copilot estara desactivado por defecto durante las sesiones. El profesor indicara en que momentos activarlo. El objetivo del taller es que entiendas que hace el codigo, no que lo generes automaticamente sin comprenderlo.

**Instalacion:**

1. En VS Code, ve a extensiones (`Ctrl+Shift+X` / `Cmd+Shift+X`) y busca "GitHub Copilot".
2. Instala la extension **GitHub Copilot** (identificador: `GitHub.copilot`). Se instalara tambien GitHub Copilot Chat automaticamente.
3. VS Code te pedira que inicies sesion con tu cuenta de GitHub. Haz clic en **"Sign in"** y autoriza el acceso en el navegador que se abrira.

**Acceso gratuito:** GitHub Copilot ofrece un plan gratuito con limite de uso mensual, mas que suficiente para este taller. Si te solicita un plan de pago, verifica que estas seleccionando el tier "Free".

---

## 8. Crear el entorno del taller e instalar dependencias

**Que es un entorno:** Un espacio aislado donde instalamos las librerias de Python que necesita este taller, sin afectar al resto de tu ordenador. Piensa en ello como una "caja" separada donde ponemos solo lo que necesitamos.

**Que son las dependencias:** Librerias de Python escritas por otros desarrolladores que nuestro codigo utiliza. Las principales son:
- **Streamlit** — para crear la aplicacion web
- **OpenAI** — para conectar con el modelo de lenguaje
- **pandas** — para analizar datos

### Con Anaconda (si instalaste la Opcion A)

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

Sabras que el entorno esta activo cuando veas `(mda13)` al inicio de la linea de la terminal.

**Importante:** cada vez que abras una terminal nueva para trabajar en el taller, necesitas activar el entorno:

```
conda activate mda13
```

### Con Python estandar (si instalaste la Opcion B)

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

Este es el paso mas importante. Si esta verificacion pasa, todo esta listo.

Asegurate de que el entorno esta activado (ves `(mda13)` o `(mda13_env)` al inicio de la linea en la terminal). Luego ejecuta:

```
streamlit run test_app.py
```

Se abrira una pagina en el navegador con una serie de checks. **Si todos aparecen en verde, tu entorno esta listo.**

Para cerrar la aplicacion, vuelve a la terminal de VS Code y pulsa `Ctrl+C`.

---

## 10. Leer el contexto del caso

En el explorador lateral de VS Code veras el archivo `CASO_FITLIFE.md`. Haz clic sobre el para abrirlo (para verlo con formato, clic derecho > "Open Preview" o `Ctrl+Shift+V` / `Cmd+Shift+V`).

Leelo antes de la primera sesion para familiarizarte con los datos y la pregunta que intentaremos responder.

---

## 11. Cuenta en Streamlit Community Cloud (opcional)

**Que es:** Streamlit Community Cloud es un servicio gratuito que permite publicar tu app para que cualquiera pueda acceder a ella desde un navegador, sin necesidad de servidores propios.

**Para que lo usamos:** Durante las tres primeras sesiones trabajaras en local. En la cuarta sesion es posible que despleguemos la aplicacion a la nube.

**Registro:** crea una cuenta en https://share.streamlit.io. Puedes registrarte directamente con tu cuenta de GitHub (recomendado). Si no la creas ahora, podras hacerlo antes de la cuarta sesion.

---

## Resumen

Lo que debes tener antes de la primera sesion:

- VS Code instalado
- Git instalado (`git --version` funciona)
- Cuenta en GitHub creada
- Proyecto clonado y abierto en VS Code
- Python funcionando (`python --version` muestra 3.11+)
- Extension Python instalada en VS Code
- Extension GitHub Copilot instalada y vinculada a tu cuenta
- Entorno `mda13` creado y dependencias instaladas
- `streamlit run test_app.py` todo en verde
- Caso FitLife leido

Lo que NO necesitas hacer antes de venir:

- Configurar el interprete de Python en VS Code (lo haremos juntos)
- Crear una cuenta en un LLM ni obtener API keys (te las proporcionara el profesor)

---

## Problemas frecuentes

**"conda no se reconoce como comando"**
En Windows, usa **Anaconda Prompt** (se instala con Anaconda) en lugar de la terminal normal. O cierra VS Code y vuelvelo a abrir tras instalar Anaconda.

**"python no se reconoce como comando"**
Asegurate de que el entorno esta activado: `conda activate mda13`. Si ves `(mda13)` al inicio de la linea, esta activo. Si usaste Python estandar y no tienes entorno activo, prueba `python3 --version`.

**"pip no se reconoce como comando"**
Con el entorno activado, prueba `python -m pip install ...` en lugar de `pip install ...`

**"git no se reconoce como comando"**
En Windows, cierra y vuelve a abrir la terminal despues de instalar Git. En Mac, asegurate de que aceptaste la instalacion de Xcode Command Line Tools.

**Streamlit no abre el navegador**
Copia la URL que aparece en la terminal (normalmente `http://localhost:8501`) y pegala en el navegador manualmente.

**Anaconda ocupa demasiado espacio**
Usa la Opcion B (Python estandar). Es mas ligera y suficiente para el taller.

**VS Code no reconoce conda en la terminal**
En Windows, abre Anaconda Prompt (fuera de VS Code), activa el entorno, y ejecuta los comandos desde ahi. Alternativamente, cierra y reabre VS Code despues de instalar Anaconda para que detecte la nueva configuracion.
