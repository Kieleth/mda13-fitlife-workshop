# Git y GitHub en 5 minutos

No necesitas ser experto en Git para este taller. Esta página te da las ideas clave para que entiendas qué está pasando cuando usas estos comandos.

---

## El problema que resuelve Git

Imagina que estás escribiendo un documento importante. En algún momento haces esto:

```
informe_final.docx
informe_final_v2.docx
informe_final_v2_BUENO.docx
informe_final_v2_BUENO_corregido.docx
```

Es un desastre, pero lo haces porque necesitas poder volver atrás si algo sale mal.

**Git resuelve exactamente esto.** En lugar de copiar archivos, Git guarda "fotos" de tu proyecto en distintos momentos. Cada foto se llama un **commit**. Puedes volver a cualquier foto anterior cuando quieras. Ya no necesitas copias con nombres raros.

---

## Las 3 ideas fundamentales

### 1. Commit = guardar un punto en el tiempo

Cuando llegas a un estado de tu código que funciona (o que quieres recordar), haces un commit. Es como decirle a Git: "hazte una foto de todo tal como está ahora". Cada commit lleva un mensaje corto que describe qué cambiaste:

```
"Añadido el gráfico de ingresos por mes"
"Corregido el filtro de centros"
```

Si después rompes algo, puedes volver a cualquier commit anterior.

### 2. Branch = experimentar sin miedo

Una **rama** (branch) es una línea paralela de trabajo. Imagina que tu proyecto funciona bien y quieres probar algo arriesgado. En lugar de tocar tu versión buena, creas una rama:

```
main (tu versión estable)
  \
   nueva-idea (aquí experimentas)
```

Si el experimento sale bien, lo unes a `main`. Si sale mal, borras la rama y tu versión buena sigue intacta. Es como tener un borrador aparte donde puedes hacer lo que quieras sin consecuencias.

### 3. Repositorio = la carpeta de tu proyecto + todo su historial

Un **repositorio** (o "repo") es simplemente una carpeta de archivos que tiene Git activado. Eso significa que Git está registrando los cambios. La carpeta del taller (`mda13-fitlife-workshop`) es un repositorio.

---

## Git vs GitHub

Son cosas distintas:

- **Git** es la herramienta que se instala en tu ordenador. Funciona sin internet. Es lo que guarda las fotos (commits), crea ramas, etc.

- **GitHub** es una web (github.com) donde puedes subir tu repositorio para que exista "en la nube". Sirve para:
  - **Compartir**: otros pueden ver y descargar tu código.
  - **Colaborar**: varias personas pueden trabajar en el mismo proyecto.
  - **Respaldo**: si tu ordenador muere, tu código sigue en GitHub.

Cuando haces `git clone`, estás descargando a tu ordenador una copia de un repositorio que está en GitHub.

---

## Qué es un repositorio público

El repositorio de este taller es **público**. Eso significa que cualquier persona en internet puede verlo y descargarlo. Esto es lo normal para material educativo y para la gran mayoría del software de código abierto.

Público NO significa que cualquiera pueda modificarlo. Solo el propietario (el profesor) puede hacer cambios en el repositorio original. Tú tienes una copia local en tu ordenador donde puedes hacer lo que quieras sin afectar al original.

---

## Los únicos comandos que necesitas

Para este taller, solo vas a usar esto:

| Comando | Qué hace |
|---|---|
| `git clone <url>` | Descarga el proyecto de GitHub a tu ordenador (solo la primera vez) |
| `git status` | Te dice qué archivos has cambiado desde el último commit |
| `git add .` | Prepara todos los cambios para el próximo commit |
| `git commit -m "mensaje"` | Guarda una foto del estado actual con un mensaje descriptivo |

Eso es todo. Si en algún momento quieres ir más allá, hay miles de recursos, pero con estos cuatro comandos tienes de sobra para el taller.

---

## Resumen en una frase

Git te permite guardar versiones de tu trabajo, experimentar sin miedo y volver atrás si algo sale mal. GitHub es donde se comparte ese trabajo con el mundo.
