#  Meowchele — Asistente de Voz

Meowchele es un asistente de voz desarrollado en **Python**.

El proyecto nace como una práctica para aprender y aplicar conceptos de programación mientras se construye, poco a poco, un asistente capaz de **escuchar comandos mediante el micrófono, interpretar las solicitudes del usuario y responder mediante voz**.

La idea es ir agregando nuevas capacidades progresivamente, manteniendo el proyecto organizado y fácil de ampliar.

---

##  Objetivos

Los principales objetivos del proyecto son:

*  Reconocer comandos mediante la voz.
*  Interpretar las solicitudes del usuario.
*  Responder utilizando síntesis de voz.
*  Consultar información como la hora.
*  Incorporar comandos relacionados con música.
*  Incorporar consultas del clima.
*  Agregar funciones relacionadas con comida.
*  Controlar algunas funciones del sistema.
*  Mantener una arquitectura modular que permita agregar nuevos comandos fácilmente.

El proyecto se encuentra en desarrollo y sus funcionalidades irán creciendo con el tiempo.

---

## Tecnologías

Actualmente se utilizan:

* **Python**
* **SpeechRecognition** — reconocimiento de voz.
* **PyAudio** — acceso al micrófono.
* **pyttsx3** — síntesis de voz.

---

## Estructura del proyecto

```text
meowchele/
│
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

La intención es mantener este archivo lo más sencillo posible.

---

### `config.py`

Contiene las configuraciones generales del asistente.

Por ejemplo:

```python
IDIOMA = "es-US"
VELOCIDAD_VOZ = 200
TIEMPO_ESCUCHA = 5
PAUSE_THRESHOLD = 0.5
```

De esta manera, las configuraciones pueden modificarse desde un solo lugar.

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

---

### `voz/hablar.py`

Se encarga de la síntesis de voz utilizando `pyttsx3`.

Su función principal es:

```python
hablar(texto)
```

Por ejemplo:

```python
hablar("Hola, soy Meowchele.")
```

La configuración del motor de voz se realiza una sola vez para evitar inicializarlo cada vez que el asistente habla.

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
                ┌───────────────┐
                │   escuchar()  │
                └───────┬───────┘
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
                   Respuesta
```

---

## Futuro del proyecto

La arquitectura está pensada para poder agregar nuevas funcionalidades sin convertir `main.py` en un archivo demasiado grande.

Algunas funcionalidades que podrían incorporarse posteriormente:

*  Reproducción y control de música.
*  Consulta del clima.
*  Búsquedas en Internet.
*  Control de YouTube.
*  Integración con servicios de música.
*  Consultas a Wikipedia.
*  Apertura y control de aplicaciones.
*  Control del volumen.
*  Gestión de archivos.
*  Recordatorios.
*  Conversaciones más naturales.
*  Mejor interpretación de lenguaje natural.

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

 **En desarrollo**

Meowchele se encuentra en una etapa inicial de desarrollo. La arquitectura actual está enfocada en crear una base organizada sobre la cual puedan incorporarse nuevas funcionalidades progresivamente.

> 🐾 *Pequeños comandos, grandes maullidos.*
