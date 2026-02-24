# Guia de instalacion

**Taller MDA13 — Analitica conversacional con GenAI**

Preparacion previa a la primera sesion. Necesitas completar todos los pasos de este documento ANTES de la primera clase. Tiempo estimado: 30-45 minutos, dependiendo de tu conexion y sistema operativo.

La configuracion final del entorno en VS Code (interprete, terminal, API key) se hara en clase con el profesor. Aqui solo instalas los componentes.

Si encuentras algun problema durante la instalacion, contacta al profesor con tiempo.

---

## Checklist rapido

Todos son necesarios salvo los indicados como opcionales.

- [ ] Visual Studio Code instalado
- [ ] Python instalado (Anaconda o Python estandar)
- [ ] Extension Python para VS Code instalada
- [ ] Git instalado
- [ ] Cuenta en GitHub creada
- [ ] Extension GitHub Copilot instalada en VS Code
- [ ] Entorno del taller creado y dependencias instaladas
- [ ] Proyecto descargado
- [ ] Verificacion: `streamlit run test_app.py` muestra todos los checks en verde
- [ ] Leido el caso FitLife (`CASO_FITLIFE.md`)
- [ ] Cuenta en Streamlit Community Cloud (opcional, puede esperar a la sesion 4)

**Sobre la API key del LLM:** no necesitas crear ninguna cuenta ni obtener claves. El profesor te facilitara la clave API durante la sesion.

---

## 1. Visual Studio Code

**Que es:** VS Code es un editor de codigo gratuito desarrollado por Microsoft.

**Para que lo usamos:** Sera tu herramienta principal. Desde VS Code escribiras codigo Python, ejecutaras tu aplicacion Streamlit y gestionaras los archivos del proyecto.

**Instalacion:**

Descarga el instalador desde https://code.visualstudio.com

- **Windows:** descarga el archivo .exe. Durante la instalacion, marca la casilla "Anadir a PATH" si aparece.
- **Mac:** descarga el archivo .zip, descomprimelo y arrastra Visual Studio Code a la carpeta Aplicaciones.

> Lo que se configurara en clase: el interprete de Python, el terminal integrado y la vinculacion con tu entorno. Solo necesitas tener VS Code instalado.

---

## 2. Python

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

Abre una terminal (en Windows: "Simbolo del sistema" o "PowerShell"; en Mac: "Terminal") y escribe:

```
python --version
```

Deberias ver algo como `Python 3.11.x` o superior. Si Mac responde "command not found", prueba con `python3 --version`.

---

## 3. Extension Python para VS Code

**Que es:** Una extension que anade funcionalidades a VS Code. La extension de Python (Microsoft) le ensena al editor a "entender" Python: colorea la sintaxis, detecta errores mientras escribes y ofrece autocompletado.

**Sin esta extension, VS Code trata tus archivos .py como texto plano.**

**Instalacion:**

1. Abre VS Code.
2. En la barra lateral izquierda, haz clic en el icono de extensiones (cuatro cuadrados, o pulsa `Ctrl+Shift+X` en Windows / `Cmd+Shift+X` en Mac).
3. Busca "Python". El primer resultado deberia ser la de Microsoft (identificador: `ms-python.python`). Haz clic en "Install".

> Lo que se configurara en clase: la extension necesita saber que interprete de Python usar. Esa vinculacion la haremos juntos.

---

## 4. Git

**Que es:** Git es un sistema de control de versiones. Registra los cambios que haces en tus archivos a lo largo del tiempo, como un historial infinito de "Ctrl+Z" pero mucho mas potente.

**Para que lo usamos:** Para descargar el material del curso desde GitHub.

**Instalacion:**

- **Windows:** descarga desde https://git-scm.com. Ejecuta el instalador .exe y acepta los valores por defecto. Git se integrara automaticamente con VS Code.
- **Mac:** abre Terminal y escribe `git --version`. Si no esta instalado, macOS te ofrecera instalarlo automaticamente (Xcode Command Line Tools). Acepta e instala.

**Verificacion:**

```
git --version
```

Deberias ver algo como `git version 2.x.x`.

---

## 5. Cuenta en GitHub

**Que es:** GitHub es una plataforma web que aloja repositorios Git. Es donde esta publicado el material del taller.

**Para que la usamos:** Para descargar el codigo del curso y para activar GitHub Copilot.

**Registro:** si no tienes cuenta, crea una en https://github.com. El plan gratuito es suficiente. Usa un email que tengas a mano durante las sesiones.

---

## 6. GitHub Copilot (extension VS Code)

**Que es:** Un asistente de programacion basado en inteligencia artificial. Mientras escribes codigo, Copilot sugiere lineas o bloques completos en tiempo real. Tambien tiene un chat integrado donde puedes hacerle preguntas sobre tu codigo.

**Para que lo usamos:** Como herramienta de apoyo para acelerar la escritura de codigo y resolver dudas de sintaxis.

**Importante:** Copilot estara desactivado por defecto durante las sesiones. El profesor indicara en que momentos activarlo. El objetivo del taller es que entiendas que hace el codigo, no que lo generes automaticamente sin comprenderlo.

**Instalacion:**

1. En VS Code, ve a extensiones (`Ctrl+Shift+X` / `Cmd+Shift+X`) y busca "GitHub Copilot".
2. Instala la extension GitHub Copilot (identificador: `GitHub.copilot`). Se instalara tambien GitHub Copilot Chat automaticamente.
3. VS Code te pedira que inicies sesion con tu cuenta de GitHub. Haz clic en "Sign in" y autoriza el acceso en el navegador.

**Acceso gratuito:** GitHub Copilot ofrece un plan gratuito con limite de uso mensual, mas que suficiente para este taller. Si te solicita un plan de pago, verifica que estas seleccionando el tier "Free".

---

## 7. Crear el entorno del taller e instalar dependencias

Este paso instala las librerias de Python que usaremos (Streamlit, OpenAI, pandas). Lo hacemos en un entorno aislado para no afectar al resto de tu ordenador.

### Con Anaconda (Opcion A)

Abre una terminal (o **Anaconda Prompt** en Windows) y ejecuta estos comandos uno a uno:

```
conda create -n mda13 python=3.12 -y
conda activate mda13
pip install -r requirements.txt
```

**Importante:** cada vez que abras una terminal nueva para trabajar en el taller, necesitas activar el entorno:

```
conda activate mda13
```

Sabras que esta activo cuando veas `(mda13)` al inicio de la linea.

### Con Python estandar (Opcion B)

```
python -m venv mda13_env
source mda13_env/bin/activate        # Mac/Linux
mda13_env\Scripts\activate           # Windows
pip install -r requirements.txt
```

(Si `requirements.txt` no esta disponible aun: `pip install streamlit openai pandas python-dotenv`)

---

## 8. Descargar el proyecto

Con git (recomendado):

```
git clone https://github.com/Kieleth/mda13-fitlife-workshop.git
cd mda13-fitlife-workshop
```

Si prefieres no usar git: el profesor te enviara un ZIP. Descomprimelo y abre la carpeta en VS Code.

---

## 9. Verificar que todo funciona

Con el entorno activado, navega a la carpeta del proyecto y ejecuta:

```
streamlit run test_app.py
```

Se abrira una pagina en el navegador con una serie de checks. **Si todos aparecen en verde, tu entorno esta listo.** Puedes cerrar con `Ctrl+C` en la terminal.

---

## 10. Leer el contexto del caso

En la carpeta del proyecto encontraras el archivo `CASO_FITLIFE.md` con la descripcion del caso de negocio que usaremos en el taller. Leelo antes de la primera sesion para familiarizarte con los datos y la pregunta que intentaremos responder.

---

## 11. Cuenta en Streamlit Community Cloud (opcional)

**Que es:** Streamlit Community Cloud es un servicio gratuito que permite publicar tu app para que cualquiera pueda acceder a ella desde un navegador, sin necesidad de servidores propios.

**Para que lo usamos:** Durante las tres primeras sesiones trabajaras en local. En la cuarta sesion es posible que despleguemos la aplicacion a la nube.

**Registro:** crea una cuenta en https://share.streamlit.io. Puedes registrarte directamente con tu cuenta de GitHub (recomendado). Si no la creas ahora, podras hacerlo antes de la cuarta sesion.

---

## Resumen

Lo que debes tener antes de la primera sesion:

- VS Code instalado
- Python funcionando (`python --version` muestra 3.11+)
- Extension Python instalada en VS Code
- Git instalado (`git --version` funciona)
- Cuenta en GitHub creada
- Extension GitHub Copilot instalada y vinculada a tu cuenta
- Entorno `mda13` creado y dependencias instaladas
- Proyecto descargado
- `streamlit run test_app.py` todo en verde
- Caso FitLife leido

Lo que NO necesitas hacer antes de venir:

- Configurar el interprete de Python en VS Code (lo haremos juntos)
- Crear una cuenta en un LLM ni obtener API keys (te las proporcionara el profesor)

---

## Problemas frecuentes

**"conda no se reconoce como comando"**
En Windows, usa **Anaconda Prompt** (se instala con Anaconda) en lugar de la terminal normal.

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
