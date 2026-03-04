# Git Companion — De cero a manejarte

Esta guia tiene dos partes. La primera empieza desde cero absoluto. La segunda te lleva un paso mas alla. No hace falta hacer las dos de golpe.

---

# PARTE A — Tu primer repositorio

## Que es Git (sin rodeos)

Cuando trabajas en un documento y quieres poder volver atras, haces copias:

```
informe_final.docx
informe_final_v2.docx
informe_final_DEFINITIVO.docx
informe_final_DEFINITIVO_bueno.docx
```

Git hace lo mismo pero de forma inteligente. En vez de copiar archivos enteros, Git guarda **los cambios** que haces. Cada vez que le dices "guardame esto", Git toma una foto del estado actual de todos tus archivos. Esa foto se llama **commit**.

La diferencia con hacer copias manuales:
- No tienes 20 versiones del mismo archivo
- Puedes ver exactamente que cambiaste y cuando
- Puedes volver a cualquier punto anterior con un clic
- Funciona con todos los archivos de un proyecto a la vez, no uno por uno

---

## Paso 1: Crea una carpeta y activa Git

Abre la terminal en VS Code y escribe:

```bash
mkdir mi-proyecto
cd mi-proyecto
git init
```

`mkdir` crea una carpeta. `cd` entra en ella. `git init` le dice a Git: "vigila esta carpeta."

No vas a ver nada especial. Git trabaja en silencio. Pero ahora todo lo que pase en esta carpeta queda registrado.

---

## Paso 2: Crea un archivo y ve que pasa

Crea un archivo. Puedes hacerlo desde VS Code (File > New File) o desde la terminal:

```bash
echo "Hola, este es mi primer archivo" > notas.txt
```

Ahora preguntale a Git que ve:

```bash
git status
```

Git te dice algo como:

```
Untracked files:
    notas.txt
```

**Untracked** significa "veo este archivo, pero no lo estoy siguiendo todavia." Git sabe que `notas.txt` existe, pero no le has dicho que lo vigile.

---

## Paso 3: Dile a Git que vigile el archivo (staging)

```bash
git add notas.txt
```

Ahora `git status` dice:

```
Changes to be committed:
    new file: notas.txt
```

Has pasado el archivo a la **zona de preparacion** (staging area). Es como poner cosas en una caja antes de sellarla. Todavia no has guardado nada — solo has dicho "esto va a ir en la proxima foto."

**Por que no guarda directamente?** Porque a veces cambias 5 archivos pero solo quieres guardar 3. El staging te deja elegir que entra en cada foto.

---

## Paso 4: Guarda la foto (commit)

```bash
git commit -m "Primer archivo del proyecto"
```

Hecho. Git ha tomado una foto de tu proyecto. El texto entre comillas es el **mensaje del commit** — una nota para tu yo del futuro que explica que hiciste.

Comprueba:

```bash
git log
```

Veras algo como:

```
commit a1b2c3d4... (HEAD -> main)
Author: Tu Nombre <tu@email.com>
Date:   Wed Mar 4 2026

    Primer archivo del proyecto
```

Esa es tu primera foto. Puedes volver a ella en cualquier momento.

---

## Paso 5: Haz cambios y observa

Edita `notas.txt` — anade una linea, cambia algo, lo que quieras. Luego:

```bash
git status
```

```
Changes not staged for commit:
    modified: notas.txt
```

Git sabe que el archivo cambio. Si quieres ver exactamente que cambiaste:

```bash
git diff
```

Veras las lineas antiguas (en rojo, con `-`) y las nuevas (en verde, con `+`). Esto es lo que hace Git especial: no solo sabe QUE cambio un archivo — sabe exactamente QUE lineas cambiaron.

Para guardar estos cambios:

```bash
git add notas.txt
git commit -m "Anadida segunda linea a notas"
```

Ahora tienes dos fotos. Puedes ver las dos con `git log`.

---

## Paso 6: Varios archivos a la vez

Crea dos archivos mas:

```bash
echo "Lista de tareas" > tareas.txt
echo "Ideas para el proyecto" > ideas.txt
```

```bash
git status
```

```
Untracked files:
    ideas.txt
    tareas.txt
```

Puedes anadir los dos a la vez:

```bash
git add .
```

El punto (`.`) significa "todo lo que hay en esta carpeta." Es un atajo para no escribir cada archivo por separado.

```bash
git commit -m "Anadidos archivos de tareas e ideas"
```

Ahora tu historial tiene 3 fotos:
1. El archivo inicial
2. La edicion
3. Los dos archivos nuevos

---

## Paso 7: Vuelve atras (sin miedo)

Imagina que editas `notas.txt` y lo dejas peor de como estaba. Antes de hacer commit, puedes deshacerlo:

```bash
git checkout -- notas.txt
```

Eso restaura el archivo al estado del ultimo commit. Los cambios que hiciste desaparecen. Es como pulsar Ctrl+Z pero para toda la sesion de edicion.

**Importante:** esto solo funciona ANTES de hacer commit. Una vez que haces commit, el cambio queda en la foto. Pero puedes volver a fotos anteriores (eso lo vemos en la parte B).

---

## Resumen de la Parte A

Has aprendido el flujo basico de Git:

```
Editar archivos
    ↓
git status         (ver que cambio)
    ↓
git diff           (ver los cambios exactos)
    ↓
git add .          (preparar los cambios)
    ↓
git commit -m ""   (guardar la foto)
    ↓
git log            (ver el historial de fotos)
```

Con estos comandos puedes trabajar en cualquier proyecto y tener siempre un historial de todo lo que has hecho. Si algo se rompe, puedes investigar que cambio y cuando.

---

---

# PARTE B — Ramas y trabajo en paralelo

## La idea de las ramas

Hasta ahora has trabajado en una sola linea: haces cambios, los guardas, sigues. Esa linea se llama `main` (la rama principal).

Pero a veces quieres probar algo sin arriesgar lo que ya funciona. Por ejemplo:

- "Quiero cambiar el diseno de la app, pero no se si quedara bien"
- "Quiero probar otro modelo de LLM, pero si no funciona quiero volver"
- "Quiero reorganizar todo el codigo, pero si la lio necesito poder deshacer"

Para eso existen las **ramas**. Una rama es una copia de tu proyecto donde puedes experimentar libremente. Si el experimento sale bien, lo unes a `main`. Si sale mal, la borras y ya esta.

Imagina un camino que se bifurca:

```
main:          A --- B --- C
                          \
experimento:               D --- E
```

`A`, `B`, `C` son commits en main. En el punto `C` creas una rama y haces los commits `D` y `E` ahi. `main` sigue en `C`, intacto. Si `D` y `E` salen bien, los unes a `main`. Si no, los descartas.

---

## Paso 1: Crea una rama

Desde tu proyecto (el de la Parte A o cualquier otro):

```bash
git branch experimento
```

Esto crea la rama pero no te mueve a ella. Para moverte:

```bash
git checkout experimento
```

O, en un solo paso (crear + moverte):

```bash
git checkout -b experimento
```

Para comprobar en que rama estas:

```bash
git branch
```

Veras algo como:

```
* experimento
  main
```

El asterisco indica donde estas.

---

## Paso 2: Trabaja en la rama

Ahora estas en la rama `experimento`. Todo lo que hagas aqui NO afecta a `main`.

Haz algun cambio:

```bash
echo "Esta es una idea experimental" > experimento.txt
git add .
git commit -m "Probando una idea nueva"
```

Edita tambien un archivo existente:

```bash
echo "Linea anadida desde la rama experimento" >> notas.txt
git add .
git commit -m "Modificado notas desde experimento"
```

---

## Paso 3: Vuelve a main y mira

```bash
git checkout main
```

Ahora mira tus archivos:
- `experimento.txt` **no existe** — solo vive en la rama `experimento`
- `notas.txt` **no tiene la linea que anadiste** — esa linea esta en la otra rama

Esto es lo mas importante de las ramas: **son mundos paralelos**. Lo que haces en uno no existe en el otro hasta que decides unirlos.

---

## Paso 4: Une la rama a main (merge)

Tu experimento funciono. Quieres incorporar esos cambios a `main`.

Primero, asegurate de estar en `main`:

```bash
git checkout main
```

Luego, une la otra rama:

```bash
git merge experimento
```

Si todo va bien, veras algo como:

```
Updating c3d4e5f..a1b2c3d
Fast-forward
 experimento.txt | 1 +
 notas.txt       | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 experimento.txt
```

Ahora `main` tiene todos los cambios de `experimento`. Ya no necesitas la rama:

```bash
git branch -d experimento
```

---

## Paso 5: Cuando las ramas chocan (conflictos)

A veces dos ramas modifican la misma linea del mismo archivo. Git no sabe cual de las dos versiones elegir. Eso se llama un **conflicto**.

Vamos a provocar uno a proposito para que pierdas el miedo.

### Crea el escenario

```bash
# Asegurate de estar en main
git checkout main

# Edita notas.txt: cambia la primera linea
# (abre el archivo y escribe "Version de main" en la primera linea)
git add .
git commit -m "Editado notas en main"

# Crea una rama y edita la MISMA linea
git checkout -b otra-idea

# Cambia la primera linea a "Version de otra-idea"
git add .
git commit -m "Editado notas en otra-idea"

# Vuelve a main e intenta unir
git checkout main
git merge otra-idea
```

### Git te avisa del conflicto

```
CONFLICT (content): Merge conflict in notas.txt
Automatic merge failed; fix conflicts and then commit the result.
```

No pasa nada. No se ha roto nada. Git simplemente te dice: "Hay dos versiones de la misma linea y no se cual quieres. Decidelo tu."

### Como se ve un conflicto

Abre `notas.txt`. Veras algo asi:

```
<<<<<<< HEAD
Version de main
=======
Version de otra-idea
>>>>>>> otra-idea
```

Las marcas son de Git:
- Lo que hay entre `<<<<<<< HEAD` y `=======` es la version de `main` (donde estas ahora)
- Lo que hay entre `=======` y `>>>>>>> otra-idea` es la version de la otra rama

### Resuelve el conflicto

Tu decides que quedarte. Tienes tres opciones:

**Opcion A: Qudate con la version de main.**
Borra todo lo de la otra rama y las marcas de Git. El archivo queda:
```
Version de main
```

**Opcion B: Quedate con la version de la otra rama.**
Borra todo lo de main y las marcas. El archivo queda:
```
Version de otra-idea
```

**Opcion C: Combina las dos.**
Escribe lo que quieras. El archivo queda:
```
Version combinada de main y otra-idea
```

Lo importante: **borra las lineas con `<<<<<<<`, `=======`, y `>>>>>>>`**. Esas son marcas de Git, no contenido real.

### Guarda la resolucion

```bash
git add notas.txt
git commit -m "Resuelto conflicto en notas"
```

Hecho. El conflicto esta resuelto. La rama esta unida.

---

## Casos reales: cuando usar ramas

### Caso 1: Probar un modelo diferente

```bash
git checkout -b probar-gpt4
# Cambias el modelo en tu app de gpt-4.1-mini a gpt-4.1
# Pruebas varias preguntas, comparas resultados
# Si va mejor:
git checkout main
git merge probar-gpt4
# Si va peor:
git checkout main
git branch -D probar-gpt4    # la D mayuscula fuerza el borrado
```

### Caso 2: Cambiar el prompt sin romper lo que funciona

```bash
git checkout -b nuevo-prompt
# Experimentas con el prompt del sistema
# Pruebas, ajustas, pruebas mas
# Cuando estas contento:
git checkout main
git merge nuevo-prompt
```

### Caso 3: Descargar actualizaciones del taller sin perder tus cambios

```bash
# Guarda tus cambios actuales
git add .
git commit -m "Mi trabajo hasta ahora"

# Descarga las actualizaciones
git pull
```

Si hay conflictos (porque tu cambiaste un archivo que el profesor tambien cambio), Git te avisa y los resuelves como vimos arriba.

---

## Referencia rapida

### Comandos del dia a dia

| Comando | Que hace |
|---|---|
| `git status` | Ver que ha cambiado |
| `git diff` | Ver las lineas exactas que cambiaron |
| `git add .` | Preparar todos los cambios |
| `git add archivo.py` | Preparar solo un archivo |
| `git commit -m "mensaje"` | Guardar una foto |
| `git log` | Ver el historial de fotos |
| `git log --oneline` | Historial compacto (una linea por commit) |

### Comandos de ramas

| Comando | Que hace |
|---|---|
| `git branch` | Ver en que rama estas |
| `git branch nombre` | Crear una rama |
| `git checkout nombre` | Moverte a una rama |
| `git checkout -b nombre` | Crear una rama y moverte a ella |
| `git merge nombre` | Unir una rama a la actual |
| `git branch -d nombre` | Borrar una rama (ya unida) |
| `git branch -D nombre` | Borrar una rama (sin unir, forzado) |

### Cuando algo va mal

| Situacion | Que hacer |
|---|---|
| "He cambiado un archivo y quiero deshacerlo" | `git checkout -- archivo.txt` |
| "He hecho `git add` pero no quiero incluir ese archivo" | `git reset archivo.txt` |
| "Hay un conflicto y no se que hacer" | Abre el archivo, busca `<<<<<<<`, decide que version quieres, borra las marcas, `git add` y `git commit` |
| "Todo esta roto y quiero volver al ultimo commit" | `git checkout -- .` (deshace TODOS los cambios no commiteados) |
| "Quiero ver como estaba un archivo en un commit anterior" | `git show HEAD~1:archivo.txt` (1 commit atras, 2 para dos, etc.) |

---

## Resumen en una frase

Git guarda fotos de tu proyecto (commits). Las ramas te dejan experimentar sin romper nada. Los conflictos se resuelven eligiendo que version quieres. Con 10 comandos te manejas en el 99% de las situaciones.

---

---

# PARTE C — Rescate: cuando git pull sale mal

Cada sesion os pedire que hagais `git pull` para descargar material nuevo. A veces eso choca con cambios que habeis hecho en vuestros archivos. Aqui teneis las recetas para salir de cualquier lio.

---

## Si todavia no habeis hecho git pull

Antes de nada, vamos a guardar vuestro trabajo en un sitio seguro y luego descargar lo nuevo. Copiad estas 3 lineas en la terminal, una por una:

```
git checkout -b mi-trabajo
```

```
git add -A && git commit -m "guardado mi trabajo" --allow-empty
```

```
git checkout main && git fetch origin && git reset --hard origin/main
```

Que acaba de pasar:
- La primera linea crea una rama llamada `mi-trabajo` con todo lo que teneis ahora. Vuestros archivos no se pierden — estan ahi.
- La segunda guarda todo en esa rama.
- La tercera vuelve a `main` y lo deja exactamente igual que lo que hay en GitHub. Limpio, sin conflictos, sin dramas.

Si os dice `branch 'mi-trabajo' already exists`, usad otro nombre: `mi-trabajo-2`, `mi-trabajo-sesion3`, lo que sea.

---

## Si ya habeis hecho git pull y estais en medio de un conflicto

Sabeis que estais en un conflicto si Git os ha dicho `CONFLICT`, o si al abrir un archivo veis lineas raras con `<<<<<<<` y `>>>>>>>`, o si `git status` dice `Unmerged paths`.

Primero, cancelad el merge que se ha quedado a medias:

```
git merge --abort
```

Eso os devuelve al estado de antes del pull. Ahora ya podeis hacer el proceso normal:

```
git checkout -b mi-trabajo
```

```
git add -A && git commit -m "guardado mi trabajo" --allow-empty
```

```
git checkout main && git fetch origin && git reset --hard origin/main
```

---

## Si nada funciona

Opcion nuclear. Funciona siempre. Renombrad vuestra carpeta y descargad el proyecto de cero:

```
cd ..
```

```
mv mda13-fitlife-workshop mda13-backup
```

```
git clone https://github.com/Kieleth/mda13-fitlife-workshop.git
```

```
cd mda13-fitlife-workshop
```

Vuestro trabajo anterior esta en la carpeta `mda13-backup`. La nueva carpeta es una copia limpia de GitHub.

Despues de esto, recordad activar el entorno:

```
conda activate mda13
```

Y verificar que todo funciona:

```
streamlit run test_app.py
```
