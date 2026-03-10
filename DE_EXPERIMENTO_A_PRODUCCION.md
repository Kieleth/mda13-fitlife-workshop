# De experimento a produccion

Habeis construido una app que funciona en vuestro portatil. Le haces preguntas, genera codigo, lo ejecuta, interpreta los resultados. Funciona.

Pero funciona **para vosotros, en vuestro ordenador, con vuestros datos, solos**.

Que pasa cuando quieres que esto lo use otra persona? O diez? O que se actualice con datos nuevos cada mes? O que no se caiga un viernes por la noche?

Esta guia os orienta sobre las cosas que cambian cuando pasas de "me funciona en local" a "esto es un producto". No es un tutorial — es un mapa. Sabeis que existe cada sitio, y cuando llegueis ahi, sabeis que preguntar.

---

# 1. Donde vive tu app

## Ahora mismo

```
Tu portatil
┌─────────────────────────────┐
│  VS Code                    │
│  ┌───────────┐              │
│  │ Streamlit │ ← tu app     │
│  │ port 8501 │              │
│  └─────┬─────┘              │
│        │                    │
│  ┌─────▼──────┐             │
│  │ fitlife.csv │ ← datos    │
│  └────────────┘             │
│        │                    │
│  ┌─────▼─────┐              │
│  │ OpenAI API │ → internet  │
│  └───────────┘              │
└─────────────────────────────┘
```

Todo vive en tu maquina. Si cierras el portatil, la app se para. Si alguien quiere verla, tiene que estar en tu misma red o pantalla.

## El primer paso: la nube

```
Internet
┌──────────────────────────────────────┐
│  Streamlit Community Cloud (gratis)  │
│  ┌───────────┐                       │
│  │ Tu app    │ ← desplegada          │
│  │ URL publica│                      │
│  └─────┬─────┘                       │
│        │                             │
│  ┌─────▼──────┐   ┌────────────┐     │
│  │ fitlife.csv │   │ OpenAI API │     │
│  │ (en GitHub) │   │ (tu key)   │     │
│  └────────────┘   └────────────┘     │
└──────────────────────────────────────┘

Cualquier persona con el link → ve tu app
```

Esto es lo que haremos en la sesion 4. Subir la app a Streamlit Community Cloud, conectar el repo de GitHub, y tener una URL publica. Gratis, sin servidores, sin configuracion.

Es perfecto para demos, prototipos y proyectos personales. Pero tiene limites.

## Cuando necesitas mas

```
Tu infraestructura (o cloud)
┌──────────────────────────────────────────────────┐
│                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    │
│  │ Nginx    │───▶│ Tu app   │───▶│ Base de  │    │
│  │ (proxy)  │    │ (Docker) │    │ datos    │    │
│  └──────────┘    └──────────┘    └──────────┘    │
│       │                │                         │
│  ┌────▼─────┐    ┌─────▼─────┐                   │
│  │ HTTPS    │    │ OpenAI    │                    │
│  │ Certs    │    │ API       │                    │
│  └──────────┘    └───────────┘                    │
│                                                  │
│  ┌──────────────────────────────────┐             │
│  │ CI/CD: GitHub → build → deploy  │             │
│  └──────────────────────────────────┘             │
└──────────────────────────────────────────────────┘
```

Aqui es donde las cosas se ponen interesantes (y complicadas). Vamos pieza por pieza.

---

# 2. Los datos: de CSV a conexion real

## Ahora mismo

Vuestros datos son un archivo CSV que esta en la carpeta del proyecto. Lo leeis con `pd.read_csv()` al arrancar la app. Funciona porque:
- Los datos no cambian
- Son pocos (16.000 filas)
- Solo los usais vosotros

## Que cambia en produccion

En un caso real, los datos de FitLife vendrian de alguno de estos sitios:

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│ Base de datos │     │ API interna   │     │ Data warehouse│
│ (PostgreSQL,  │     │ (el CRM, el   │     │ (BigQuery,    │
│  MySQL...)    │     │  ERP, Stripe) │     │  Snowflake)   │
└───────┬───────┘     └───────┬───────┘     └───────┬───────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                        ┌─────▼─────┐
                        │  Tu app   │
                        └───────────┘
```

Las preguntas que aparecen cuando los datos son reales:

- **Frecuencia**: cada cuanto se actualizan? Cada dia? Cada hora? En tiempo real?
- **Volumen**: 16.000 filas se cargan en memoria sin problema. 16 millones no. Necesitas paginacion, consultas parciales o un motor de base de datos.
- **Credenciales**: la conexion a la base de datos necesita usuario, contrasena, host. Eso no se mete en el codigo — se mete en variables de entorno (como hicisteis con la API key de OpenAI en el `.env`).
- **Consistencia**: si alguien esta mirando un dashboard mientras los datos se actualizan, que ve? Datos de ayer? De hace 5 minutos? Un mix?

No hace falta resolverlo todo de golpe. Pero hay que saber que estos problemas existen.

---

# 3. Git en equipo: ramas para no pisarse

En el taller habeis usado Git para descargar material (`git pull`). En un proyecto real, Git es como trabajais en equipo.

La idea fundamental ya la visteis en `GIT_COMPANION.md`: las ramas os permiten experimentar sin romper lo que funciona. En un equipo, esto se convierte en un flujo de trabajo:

```
main (lo que esta en produccion — siempre funciona)
  │
  ├── feature/nuevo-grafico     ← alguien trabaja aqui
  │
  ├── feature/modelo-gpt4       ← otra persona aqui
  │
  └── fix/error-en-churn        ← alguien arreglando un bug
```

Cada persona trabaja en su rama. Cuando termina, pide una **pull request** (PR): "He terminado esto, revisadlo." Otro del equipo lo revisa, y si esta bien, se une a `main`.

Regla basica: **nadie toca main directamente**. Todo pasa por ramas y revision.

Esto parece burocracia innecesaria cuando estas solo. Pero cuando sois 3 personas tocando el mismo codigo, es lo que evita que os piseis.

---

# 4. CI/CD: que el deploy no dependa de ti

## El problema

Ahora mismo, para que tu app se actualice, tu tienes que:
1. Abrir VS Code
2. Hacer cambios
3. Guardar
4. Hacer commit y push
5. Ir a Streamlit Cloud y ver que se actualice

Son 5 pasos manuales. Si te olvidas del paso 3, o si haces push de algo roto, la app se rompe en produccion.

## La solucion: automatizar

CI/CD significa Continuous Integration / Continuous Deployment. En practico:

```
Tu haces push a GitHub
        │
        ▼
┌───────────────────────────────────┐
│ CI: Tests automaticos             │
│                                   │
│  - El codigo arranca sin errores? │
│  - Las preguntas test dan         │
│    resultados razonables?         │
│  - El prompt tiene los campos     │
│    obligatorios?                  │
└───────────────┬───────────────────┘
                │
           Todo OK?
           /      \
          Si       No
          │        │
          ▼        ▼
   ┌──────────┐  ┌──────────┐
   │ CD:      │  │ STOP     │
   │ Deploy   │  │ Te avisa │
   │ auto     │  │ del error│
   └──────────┘  └──────────┘
```

Tu haces push. El sistema ejecuta tests. Si pasan, despliega automaticamente. Si no pasan, te avisa y no despliega. La app en produccion nunca se rompe por un push descuidado.

Herramientas tipicas: GitHub Actions (gratis para repos publicos), GitLab CI, Jenkins.

No es magia — es un archivo de configuracion en tu repo que dice "cuando alguien haga push, ejecuta estos comandos." Pero cambia completamente la forma de trabajar.

---

# 5. Docker: que funcione en cualquier sitio

## El problema clasico

"En mi ordenador funciona." La frase mas famosa del desarrollo de software.

Tu app necesita Python 3.11, pandas, openai, streamlit, y unas versiones concretas de cada una. En tu portatil las tienes instaladas. Pero en el servidor de produccion, o en el portatil de tu companero, puede haber versiones diferentes. Y eso rompe cosas.

## La solucion: empaquetar todo

Docker es como una caja que contiene tu app + todo lo que necesita para funcionar. El sistema operativo, Python, las librerias, los archivos de configuracion. Todo.

```
┌─────────────────────────────────┐
│ Contenedor Docker               │
│                                 │
│  Python 3.11                    │
│  pandas 2.1                     │
│  openai 1.30                    │
│  streamlit 1.35                 │
│                                 │
│  ┌───────────────────────────┐  │
│  │ Tu app (paso_15.py)       │  │
│  │ Datos (fitlife.csv)       │  │
│  │ .env (API keys)           │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

Esa caja funciona **exactamente igual** en tu portatil, en el servidor, en el ordenador de tu companero, en cualquier sitio. Si funciona en la caja, funciona en todas partes.

Para crear la caja, escribes un archivo llamado `Dockerfile`:

```dockerfile
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "paso_15.py"]
```

5 lineas. Eso es todo lo que necesitas para empaquetar tu app.

---

# 6. Seguridad: cosas que no puedes ignorar

Cuando la app es solo para ti, da igual. Cuando la ve alguien mas, hay cosas que proteger.

## API keys

Vuestra API key de OpenAI esta en un archivo `.env`. Eso esta bien para desarrollo. En produccion, las keys van en **variables de entorno del servidor** o en un **gestor de secretos** (como AWS Secrets Manager o HashiCorp Vault). Nunca, jamas, en el codigo ni en el repositorio de Git.

Si alguien sube una API key a un repo publico de GitHub, hay bots que la detectan en segundos y la usan para hacer llamadas a tu cuenta. Os lo digo porque pasa todos los dias.

## Autenticacion

Ahora mismo cualquiera con el link puede usar vuestra app. Y cada pregunta que hacen cuesta dinero (la llamada a OpenAI). En produccion necesitais saber **quien** esta usando la app.

Opciones de menos a mas complicado:
- Streamlit tiene un sistema basico de autenticacion (email + contrasena)
- OAuth con Google/GitHub (el tipico "Inicia sesion con Google")
- Sistemas de permisos propios (roles: admin, analista, viewer)

## exec() en produccion

Recordais `exec()`? Ejecuta codigo generado por el LLM. En el taller es seguro porque somos los unicos usuarios. En produccion, alguien podria hacer preguntas disenadas para que el LLM genere codigo malicioso ("borra todos los archivos").

Soluciones:
- Ejecutar el codigo en un **sandbox** (un entorno aislado donde no puede hacer dano)
- Validar el codigo antes de ejecutarlo (por ejemplo: prohibir `import os`, `import subprocess`, `open()`)
- Limitar los permisos del proceso que ejecuta el codigo

No hace falta paranoiar, pero hay que saber que el riesgo existe.

---

# 7. Escalabilidad: cuando un servidor no es suficiente

## El problema

Vuestra app corre en un proceso. Un proceso atiende a un usuario a la vez (mas o menos). Si 50 personas preguntan a la vez, 49 esperan.

## La solucion progresiva

```
Nivel 1: Un servidor mas grande
┌─────────────┐
│ Servidor    │
│ (mas RAM,   │
│  mas CPU)   │
└─────────────┘
Sirve para: 1-20 usuarios simultaneos


Nivel 2: Varias copias detras de un balanceador
                ┌─────────────┐
           ┌───▶│ App copia 1 │
           │    └─────────────┘
┌──────┐   │    ┌─────────────┐
│ Load │───┼───▶│ App copia 2 │
│ Bal. │   │    └─────────────┘
└──────┘   │    ┌─────────────┐
           └───▶│ App copia 3 │
                └─────────────┘
Sirve para: 20-500 usuarios simultaneos


Nivel 3: Kubernetes (orquestacion de contenedores)
┌────────────────────────────────────────┐
│ Kubernetes                             │
│                                        │
│  Crea y destruye copias segun demanda  │
│  Si una copia falla, crea otra         │
│  Escala automaticamente                │
│                                        │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │
│  │App 1│ │App 2│ │App 3│ │App N│      │
│  └─────┘ └─────┘ └─────┘ └─────┘      │
└────────────────────────────────────────┘
Sirve para: 500+ usuarios, alta disponibilidad
```

La mayoria de proyectos nunca pasan del nivel 1. Pero es bueno saber que los otros niveles existen para cuando los necesites.

---

# 8. Monitoring: saber que esta pasando

Cuando la app esta en tu portatil, ves los errores en la terminal. Cuando esta en un servidor, nadie ve esa terminal. Necesitas herramientas que te avisen.

Cosas que quieres saber:
- **La app esta corriendo?** (health checks)
- **Cuantas preguntas se hacen al dia?** (metricas de uso)
- **Cuanto tarda cada respuesta?** (latencia)
- **Cuantas llamadas a la API estamos haciendo?** (costes)
- **Hay errores?** (logs centralizados)

No necesitas montarlo todo desde el dia 1. Pero si algo se rompe un domingo a las 3 de la manana y no te enteras hasta el lunes, tienes un problema.

---

# 9. Costes: lo que nadie te cuenta

Vuestra app hace 2 llamadas a OpenAI por pregunta (codigo + interpretacion). Con gpt-4.1-mini, cada llamada cuesta fracciones de centimo. Parece nada.

Pero si 100 usuarios hacen 20 preguntas al dia:
- 100 × 20 × 2 = 4.000 llamadas al dia
- ~120.000 llamadas al mes
- Dependiendo del modelo y la longitud del prompt, puede ser 50 EUR o 500 EUR al mes

Cosas que controlar:
- **Modelo**: gpt-4.1-mini es 10x mas barato que gpt-4.1. Para la mayoria de preguntas, mini sobra.
- **Cache**: si alguien pregunta lo mismo que otro usuario pregunto hace 5 minutos, para que volver a llamar a la API? Guarda la respuesta.
- **Limites**: maximo de preguntas por usuario al dia. Evita sorpresas en la factura.
- **Prompt**: un prompt de 2.000 tokens cuesta el doble que uno de 1.000. Los ejemplos de few-shot ayudan, pero anaden tokens.

---

# 10. El mapa completo

Aqui va todo junto. No para que lo monteis manana — para que sepais que piezas existen.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Desarrollador                                                 │
│   ┌──────────┐     ┌──────────────┐     ┌──────────────────┐    │
│   │ VS Code  │────▶│ Git + GitHub │────▶│ CI/CD            │    │
│   │ (codigo) │     │ (versiones)  │     │ (tests + deploy) │    │
│   └──────────┘     └──────────────┘     └────────┬─────────┘    │
│                                                  │              │
│   Servidor / Cloud                               │              │
│   ┌──────────────────────────────────────────────▼──────────┐   │
│   │                                                         │   │
│   │  ┌───────┐   ┌─────────────┐   ┌──────────────────┐    │   │
│   │  │ Nginx │──▶│ Docker      │──▶│ Base de datos    │    │   │
│   │  │(proxy)│   │ (tu app)    │   │ (datos reales)   │    │   │
│   │  └───────┘   └──────┬──────┘   └──────────────────┘    │   │
│   │                     │                                   │   │
│   │  ┌──────────────────▼──────────────────────────────┐    │   │
│   │  │ APIs externas: OpenAI, Stripe, CRM, lo que sea  │    │   │
│   │  └─────────────────────────────────────────────────┘    │   │
│   │                                                         │   │
│   │  ┌─────────────────────────────────────────────────┐    │   │
│   │  │ Monitoring: logs, alertas, metricas, costes     │    │   │
│   │  └─────────────────────────────────────────────────┘    │   │
│   │                                                         │   │
│   │  ┌─────────────────────────────────────────────────┐    │   │
│   │  │ Seguridad: auth, secrets, sandbox, HTTPS        │    │   │
│   │  └─────────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   Usuarios                                                      │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐                       │
│   │ Navegador│ │ Navegador│ │ Navegador│                        │
│   └──────────┘ └──────────┘ └──────────┘                        │
└─────────────────────────────────────────────────────────────────┘
```

---

# Como usar este documento

Si quieres ir mas alla con tu proyecto, este documento te sirve como checklist de las cosas que tienes que pensar. No tienes que resolverlas todas ni resolverlas solo.

Una forma practica de usarlo: abre un LLM (ChatGPT, Claude, lo que uses) y dile algo como:

> "Tengo una app de Streamlit que funciona en local. Usa OpenAI para generar y ejecutar codigo Python sobre un dataset de 16.000 filas. Quiero desplegarla para que la usen 10 personas de mi equipo. Segun mi profesor, las cosas que tengo que pensar son: [pega la seccion que te interese de este documento]. Que pasos concretos deberia seguir?"

El LLM te dara un plan especifico para tu caso. Este documento es el mapa; el LLM te da las direcciones.

---

# Resumen

| Cuando estas en... | Te preocupas de... |
|---|---|
| Tu portatil | Que funcione |
| Demo / prototipo | Que se vea (Streamlit Cloud) |
| Equipo pequeno | Git con ramas, permisos, API keys seguras |
| Usuarios reales | Auth, HTTPS, monitoring, costes |
| Escala | Docker, CI/CD, load balancing |
| Produccion seria | Todo lo anterior + backups, SLAs, on-call |

No hace falta llegar al final de la tabla. La mayoria de proyectos viven felices en las dos o tres primeras filas. Pero cuando necesites avanzar, ya sabes por donde ir.
