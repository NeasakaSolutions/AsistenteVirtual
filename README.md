# Meowchele — Asistente de Voz

Meowchele es un asistente de voz desarrollado en **Python**.

El proyecto nace como una práctica para aprender y aplicar conceptos de programación mientras se construye, poco a poco, un asistente capaz de **escuchar comandos mediante el micrófono, interpretar las solicitudes del usuario y responder mediante voz**.

La idea es ir agregando nuevas capacidades progresivamente, manteniendo el proyecto organizado y fácil de ampliar.

---

## Objetivos

Los principales objetivos del proyecto son:

* Reconocer comandos mediante la voz.
* Interpretar las solicitudes del usuario.
* Responder utilizando síntesis de voz.
* Utilizar una voz personalizada mediante **Fish Audio**.
* Consultar información como la hora.
* Incorporar comandos relacionados con música.
* Incorporar consultas del clima.
* Agregar funciones relacionadas con comida.
* Controlar algunas funciones del sistema.
* Mantener una arquitectura modular que permita agregar nuevos comandos fácilmente.
* Mejorar progresivamente la interpretación del lenguaje natural.

El proyecto se encuentra en desarrollo y sus funcionalidades irán creciendo con el tiempo.

---

## Tecnologías

Actualmente se utilizan:

* **Python** — lenguaje principal del proyecto.
* **SpeechRecognition** — reconocimiento de voz.
* **PyAudio** — acceso al micrófono.
* **Fish Audio** — generación de voz mediante inteligencia artificial.
* **Fish Audio SDK** — comunicación con la API de Fish Audio.
* **Pygame** — reproducción del audio generado.
* **python-dotenv** — gestión de variables de entorno.

---

## Estructura del proyecto

```text
meowchele/
│
├── .env
├── .gitignore
├── main.py
├── config.py
│
├── voz/
│   ├── __init__.py
│   ├── escuchar.py
│   └── hablar.py
│
├── comandos/
│   ├── __init__.py
│   ├── hora.py
│   ├── musica.py
│   ├── clima.py
│   ├── comida.py
│   └── sistema.py
│
└── core/
    ├── __init__.py
    └── interprete.py
```

### `main.py`

Es el **punto de entrada** del programa.

Se encarga de iniciar el asistente y mantener el ciclo principal:

```text
Escuchar → Interpretar → Ejecutar → Escuchar nuevamente
```

La intención es mantener este archivo lo más sencillo posible y delegar las responsabilidades a los diferentes módulos.

---

### `config.py`

Contiene las configuraciones generales del asistente.

Entre ellas se encuentran las configuraciones relacionadas con el reconocimiento de voz y Fish Audio.

Por ejemplo:

```python
IDIOMA = "es-US"
TIEMPO_ESCUCHA = 5
PAUSE_THRESHOLD = 0.5

FISH_API_KEY = os.getenv("FISH_API_KEY")
FISH_VOICE_ID = os.getenv("FISH_VOICE_ID")
FISH_MODEL = "s2.1-pro-free"
```

La API key y el identificador de la voz se almacenan mediante variables de entorno para evitar incluir información sensible directamente en el código.

---

## Módulo `voz`

Este módulo contiene todo lo relacionado con la interacción mediante voz.

### `voz/escuchar.py`

Se encarga de:

* Activar el micrófono.
* Capturar el audio.
* Convertir el audio a texto.
* Manejar errores del reconocimiento.

Su función principal es:

```python
escuchar()
```

El texto reconocido posteriormente es enviado al intérprete de comandos.

---

### `voz/hablar.py`

Se encarga de generar y reproducir la voz de Meowchele utilizando **Fish Audio**.

Su función principal es:

```python
hablar(texto)
```

Por ejemplo:

```python
hablar("Hola, soy Meowchele.")
```

El funcionamiento general es:

```text
Texto
  ↓
Fish Audio
  ↓
Audio generado
  ↓
Pygame
  ↓
 Voz de Kasane Teto
```

La voz utilizada por el asistente se identifica mediante `FISH_VOICE_ID` y la comunicación con Fish Audio utiliza una API key almacenada en `.env`.

La implementación de la voz está aislada dentro de este módulo para que el resto del proyecto pueda utilizar simplemente:

```python
hablar("Hola")
```

sin necesitar conocer cómo se genera o reproduce el audio.

---

## Variables de entorno

El proyecto utiliza un archivo `.env` para almacenar información que no debe incluirse directamente en el código fuente.

Ejemplo:

```env
FISH_API_KEY=TU_API_KEY
FISH_VOICE_ID=TU_VOICE_ID
```

El archivo `.env` **no debe subirse al repositorio**.

Por este motivo, `.gitignore` debe incluir:

```gitignore
.env
__pycache__/
*.pyc
```

Los directorios `__pycache__` y los archivos `.pyc` son archivos generados automáticamente por Python y no forman parte del código fuente del proyecto.

---

## Módulo `comandos`

Aquí se encuentran las **capacidades individuales de Meowchele**.

Cada archivo representa una categoría o funcionalidad específica.

### `comandos/hora.py`

Contiene las funciones relacionadas con la hora.

```python
decir_hora()
```

---

### `comandos/musica.py`

Contendrá las funciones relacionadas con la reproducción y control de música.

Actualmente se encuentra en desarrollo.

---

### `comandos/clima.py`

Contendrá las funciones relacionadas con consultas meteorológicas.

Actualmente se encuentra en desarrollo.

---

### `comandos/comida.py`

Contendrá las funciones relacionadas con búsqueda o recomendaciones de comida.

Actualmente se encuentra en desarrollo.

---

### `comandos/sistema.py`

Contiene comandos relacionados con el funcionamiento del propio asistente o del sistema.

Por ejemplo:

```python
salir()
```

---

## Módulo `core`

Contiene la lógica principal que conecta lo que dice el usuario con los comandos disponibles.

### `core/interprete.py`

Su responsabilidad es determinar **qué comando corresponde al texto recibido**.

Por ejemplo:

```text
Usuario:

"¿Qué hora es?"

        ↓

interpreter

        ↓

decir_hora()

        ↓

Meowchele:

"Son las 8:30."
```

Actualmente el intérprete utiliza palabras clave para identificar los comandos.

A futuro se busca mejorar esta parte para permitir una interpretación más natural de las solicitudes.

---

## Flujo del asistente

El funcionamiento general del programa es:

```text
                  ┌─────────────┐
                  │   main.py   │
                  └──────┬──────┘
                         │
                         ▼
                ┌────────────────┐
                │    escuchar()  │
                └───────┬────────┘
                        │
                        ▼
                 Texto del usuario
                        │
                        ▼
              ┌──────────────────┐
              │ ejecutar_comando │
              └────────┬─────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       hora.py      musica.py    clima.py
          │            │            │
          └────────────┼────────────┘
                       ▼
                   hablar()
                       │
                       ▼
                 Fish Audio
                       │
                       ▼
                Voz de Meowchele
```

---

## Futuro del proyecto

La arquitectura está pensada para poder agregar nuevas funcionalidades sin convertir `main.py` en un archivo demasiado grande.

Algunas funcionalidades que podrían incorporarse posteriormente:

* Reproducción y control de música.
* Consulta del clima.
* Búsquedas en Internet.
* Control de YouTube.
* Integración con servicios de música.
* Consultas a Wikipedia.
* Apertura y control de aplicaciones.
* Control del volumen.
* Gestión de archivos.
* Recordatorios.
* Conversaciones más naturales.
* Mejor interpretación del lenguaje natural.
* Respuestas más expresivas mediante las capacidades de Fish Audio.
* Streaming de audio para reducir la latencia de respuesta.

La estructura podría crecer de esta forma:

```text
comandos/
├── hora.py
├── fecha.py
├── musica.py
├── youtube.py
├── spotify.py
├── clima.py
├── comida.py
├── wikipedia.py
├── navegador.py
├── volumen.py
├── archivos.py
├── recordatorios.py
└── sistema.py
```

La intención es que **cada nueva capacidad tenga su propio módulo**, manteniendo las responsabilidades separadas.

---

## Ejecución

Para iniciar Meowchele:

```bash
python main.py
```

Una vez iniciado, el asistente comenzará a escuchar mediante el micrófono.

Por ejemplo:

```text
Meowchele:

¡Meowchele-san! ¡Bienvenido! ¿Qué necesitas?

Usuario:

¿Qué hora es?

Meowchele:

Son las 8:30.
```

Para terminar el programa:

```text
Usuario:

Salir

Meowchele:

Allí nos vidrios Meowchele-san.
```

---

##  Estado del proyecto

** En desarrollo**

Meowchele se encuentra en una etapa inicial de desarrollo. La arquitectura actual está enfocada en crear una base organizada sobre la cual puedan incorporarse nuevas funcionalidades progresivamente.

Actualmente el proyecto ya cuenta con:

*  Reconocimiento de voz mediante micrófono.
*  Interpretación básica mediante palabras clave.
*  Consulta de la hora.
*  Síntesis de voz mediante Fish Audio.
*  Voz personalizada mediante un `reference_id`.
*  Gestión de credenciales mediante variables de entorno.
*  Arquitectura modular para agregar nuevos comandos.

