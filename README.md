# Kasane Teto — Asistente de Voz

Asistente virtual desarrollado en **Python**, inspirado en Kasane Teto.

El proyecto nace como una práctica para aprender y aplicar conceptos de programación mientras se construye, poco a poco, un asistente capaz de **escuchar comandos mediante el micrófono, interpretar las solicitudes del usuario y responder mediante voz**.

Además, el proyecto integra un avatar Live2D mediante VTube Studio, permitiendo controlar sus hotkeys y animar la boca mientras se reproduce la voz del asistente.

La idea es incorporar nuevas capacidades progresivamente, manteniendo el código organizado, modular y fácil de ampliar.

---

## Objetivos

Los principales objetivos del proyecto son:

- Reconocer comandos mediante la voz.
- Interpretar las solicitudes del usuario.
- Responder utilizando síntesis de voz.
- Utilizar una voz personalizada mediante **Fish Audio**.
- Consultar información como la hora.
- Incorporar comandos relacionados con música.
- Incorporar consultas del clima.
- Agregar funciones relacionadas con comida.
- Controlar algunas funciones del sistema.
- Controlar expresiones y acciones de un avatar mediante VTube Studio.
- Animar la boca del avatar durante la reproducción de voz.
- Mejorar progresivamente la interpretación del lenguaje natural.
- Mantener una arquitectura modular que permita agregar nuevos comandos fácilmente.

El proyecto se encuentra en desarrollo y sus funcionalidades irán creciendo con el tiempo.

---

## Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| **Python** | Lenguaje principal del proyecto. |
| **SpeechRecognition** | Reconocimiento de voz. |
| **PyAudio** | Acceso al micrófono para capturar audio. |
| **Fish Audio** | Generación de voz mediante inteligencia artificial. |
| **Fish Audio SDK** | Comunicación con la API de Fish Audio. |
| **Pygame** | Reproducción y control del audio generado. |
| **VTube Studio API** | Comunicación y control del avatar Live2D. |
| **WebSockets** | Comunicación con la API de VTube Studio. |
| **asyncio** | Ejecución de operaciones asíncronas. |
| **threading** | Ejecución del controlador de boca en un hilo independiente. |
| **python-dotenv** | Gestión de variables de entorno. |
| **Git** | Control de versiones del código fuente. |

---

## Estructura del proyecto

La estructura actual separa la entrada del programa, la voz, los comandos, la interpretación y las integraciones externas.

```text
AsistenteVirtual/
│
├── .env
├── .gitignore
├── README.md
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
│   └── avatar.py
│
├── core/
│   ├── __init__.py
│   └── interprete.py
│
└── integraciones/
    └── vtube_studio.py
```

Los archivos `__init__.py` pueden estar vacíos; permiten organizar los directorios como paquetes de Python.

A medida que se desarrollen nuevas funcionalidades, podrán agregarse módulos como `hora.py`, `musica.py`, `clima.py`, `comida.py` y `sistema.py` dentro de `comandos/`.

### `main.py`

Es el punto de entrada del programa.

Se encarga de:

- Preparar el avatar al iniciar.
- Ejecutar el saludo inicial.
- Mantener el ciclo principal de escucha y procesamiento.
- Finalizar el programa cuando el intérprete indique que debe salir.
- Liberar el controlador de boca al terminar la ejecución.

El objetivo es mantener este archivo sencillo y delegar las responsabilidades a los módulos correspondientes.

### `config.py`

Contiene las configuraciones generales del asistente.

Entre ellas se encuentran los parámetros de reconocimiento de voz, la conexión con VTube Studio y las credenciales necesarias para Fish Audio.

Por ejemplo, la configuración puede incluir:

```python
IDIOMA = "es-US"
TIEMPO_ESCUCHA = 5
PAUSE_THRESHOLD = 0.5

FISH_API_KEY = os.getenv("FISH_API_KEY")
FISH_VOICE_ID = os.getenv("FISH_VOICE_ID")
FISH_MODEL = "s2.1-pro-free"
```

Los valores definitivos deben corresponder a los nombres que utiliza el `config.py` actual del proyecto.

La API key, el identificador de voz y el token de VTube Studio se gestionan mediante variables de entorno, evitando incluir credenciales directamente en el código fuente.

---

## Módulo `voz`

Contiene la lógica relacionada con la interacción mediante voz.

### `voz/escuchar.py`

Se encarga de:

- Activar el micrófono.
- Capturar el audio del usuario.
- Convertir el audio a texto.
- Manejar errores durante el reconocimiento.

Su función principal es:

```python
escuchar()
```

El texto reconocido se envía posteriormente al intérprete de comandos.

### `voz/hablar.py`

Se encarga de generar y reproducir las respuestas habladas utilizando **Fish Audio**.

Su función principal es:

```python
hablar(texto)
```

Por ejemplo:

```python
hablar("¡Oha-teto! ¿En qué puedo ayudarte?")
```

El flujo de generación de voz es:

```text
Texto de respuesta
       ↓
   Fish Audio
       ↓
   Audio generado
       ↓
 Guardado temporal
       ↓
     Pygame
       ↓
 Voz de Kasane Teto
```

La voz se configura mediante `FISH_VOICE_ID`, mientras que `FISH_API_KEY` permite autenticar las solicitudes a Fish Audio.

El audio generado se guarda temporalmente para su reproducción y se elimina al terminar el proceso de voz.

#### Integración con el movimiento de boca

`hablar()` también coordina la animación de la boca del avatar:

1. Genera el audio mediante Fish Audio.
2. Guarda el audio temporalmente.
3. Carga el archivo en Pygame.
4. Activa el movimiento de boca.
5. Reproduce la voz.
6. Espera hasta que termina la reproducción.
7. Detiene el movimiento y cierra la boca.
8. Elimina el archivo temporal.

Los comandos solo necesitan llamar a `hablar(texto)`. No deben implementar individualmente el movimiento de boca.

Esto permite mantener separada la lógica de voz y evita duplicar código en cada comando.

**Limitación actual:** la animación de boca utiliza una oscilación periódica de apertura y cierre durante la reproducción. Está sincronizada con la duración de la voz, pero todavía no realiza sincronización labial precisa por fonemas o sílabas.

---

## Integración con VTube Studio

El módulo `integraciones/vtube_studio.py` contiene la comunicación con VTube Studio mediante su API pública y WebSockets.

Sus responsabilidades incluyen:

- Conectar y autenticar al asistente.
- Consultar las hotkeys disponibles del modelo actual.
- Activar hotkeys configuradas en VTube Studio.
- Controlar el movimiento de boca durante la reproducción de voz.
- Cerrar la conexión al finalizar el programa.

### Control de hotkeys

Las hotkeys permiten activar acciones del avatar, como cambios de expresión, ropa u otros efectos configurados en el modelo.

Las funciones principales utilizadas para esta tarea son:

```python
activar_hotkey(hotkey_id)
listar_hotkeys()
```

El módulo `comandos/avatar.py` utiliza estas capacidades para ejecutar acciones relacionadas con el avatar.

### Control de boca

El movimiento de boca se gestiona mediante funciones específicas:

```python
iniciar_movimiento_boca()
detener_movimiento_boca()
cerrar_control_boca()
```

Su propósito es:

- Iniciar la animación cuando comienza la reproducción de voz.
- Detenerla cuando termina la reproducción.
- Mantener el controlador disponible entre frases consecutivas.
- Liberar la conexión cuando el asistente finaliza.

La conexión persistente busca reducir las reconexiones y la latencia entre respuestas. Su funcionamiento debe verificarse con las pruebas de integración del proyecto.

El control utiliza el parámetro de seguimiento `MouthOpen` de VTube Studio, no el parámetro interno de Live2D `ParamMouthOpenY`.

---

## Módulo `comandos`

Este módulo contiene las capacidades individuales del asistente. La idea es que cada funcionalidad tenga su propia responsabilidad y pueda ampliarse sin convertir `main.py` en un archivo demasiado grande.

### `comandos/avatar.py`

Contiene acciones relacionadas con la preparación y el control del avatar.

Actualmente incluye funciones para:

- Eliminar toggles activos.
- Quitar la marca de agua.
- Cambiar la ropa.
- Activar la hotkey de baguette.
- Ejecutar otras acciones configuradas para el modelo.

Las acciones disponibles dependen de las hotkeys y configuraciones del modelo de VTube Studio.

### Módulos previstos

Los siguientes módulos representan funcionalidades que se pueden incorporar progresivamente. No significa que todos estén implementados actualmente.

| Módulo | Responsabilidad prevista |
|---|---|
| `comandos/hora.py` | Consultar y anunciar la hora. |
| `comandos/musica.py` | Reproducir y controlar música. |
| `comandos/clima.py` | Consultar información meteorológica. |
| `comandos/comida.py` | Buscar o recomendar comida. |
| `comandos/sistema.py` | Controlar funciones del sistema y salir del asistente. |

Cuando se agreguen, cada comando podrá llamar a `hablar()` para responder mediante voz sin tener que implementar de nuevo la integración con Fish Audio y VTube Studio.

---

## Módulo `core`

### `core/interprete.py`

Contiene la lógica que conecta las instrucciones del usuario con las funciones disponibles.

Su responsabilidad principal es determinar qué comando corresponde al texto recibido y ejecutar la acción adecuada.

Por ejemplo:

```text
Usuario:
"¿Qué hora es?"
       ↓
  escuchar()
       ↓
Texto reconocido
       ↓
ejecutar_comando(texto)
       ↓
   Comando de hora
       ↓
   hablar(texto)
       ↓
Respuesta hablada
```

Actualmente, la interpretación se basa en las reglas y palabras clave definidas en el código.

En el futuro se busca mejorar la interpretación del lenguaje natural para reconocer solicitudes formuladas de distintas maneras.

---

## Flujo general del asistente

```text
                 ┌──────────────┐
                 │    main.py   │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │  escuchar()  │
                 └──────┬───────┘
                        ↓
                Texto reconocido
                        ↓
              ┌───────────────────┐
              │ ejecutar_comando()│
              └─────────┬─────────┘
                        ↓
                Comando seleccionado
                        ↓
                  hablar(texto)
                        ↓
                  ┌───────────┐
                  │ Fish Audio│
                  └─────┬─────┘
                        ↓
                  Audio generado
                        ↓
                    Pygame
                        ↓
               Voz de Kasane Teto
                        ↕
                VTube Studio API
                        ↓
              Movimiento de boca
```

Este diseño mantiene las responsabilidades separadas: el intérprete decide qué hacer, el módulo de voz se ocupa de hablar y la integración con VTube Studio controla el avatar.

---

## Variables de entorno y seguridad

El proyecto utiliza un archivo `.env` para almacenar credenciales y otros valores que no deben incluirse directamente en el código fuente.

Ejemplo:

```dotenv
FISH_API_KEY=tu_clave_de_fish_audio
FISH_VOICE_ID=tu_identificador_de_voz
FISH_MODEL=s2.1-pro-free
VTS_AUTH_TOKEN=tu_token_de_vtube_studio
```

Los valores anteriores son ejemplos. Deben sustituirse por las credenciales y los identificadores correspondientes a tu configuración.

La URL de conexión con VTube Studio y otras opciones también pueden configurarse en `config.py`.

**Nunca publiques las claves API ni el token de VTube Studio en un repositorio público.**

### Archivo `.gitignore`

Para evitar subir credenciales y archivos generados automáticamente, el archivo `.gitignore` debe incluir al menos:

```gitignore
# Variables de entorno y secretos
.env
.env.*

# Excepción opcional para una plantilla sin secretos
!.env.example

# Caché de Python
__pycache__/
*.py[cod]

# Entornos virtuales
entorno/
.venv/
venv/

# Archivos locales de editores
.vscode/
.idea/
```

Si utilizas una plantilla `.env.example`, debe contener únicamente nombres de variables y valores de ejemplo, nunca credenciales reales.

Los directorios `__pycache__` y los archivos `.pyc` son generados automáticamente por Python. No es necesario incluirlos en el repositorio.

---

## Instalación

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

Desde la carpeta raíz, en Windows con PowerShell:

```powershell
python -m venv entorno
.\entorno\Scripts\Activate.ps1
```

Instala las dependencias utilizadas por los módulos del proyecto:

```powershell
pip install SpeechRecognition PyAudio fishaudio pygame websockets python-dotenv
```

La instalación de PyAudio puede requerir pasos adicionales según la versión de Python y el entorno de Windows.

Si posteriormente se incorporan nuevas bibliotecas, conviene agregarlas a un archivo `requirements.txt` para facilitar la instalación del proyecto en otros equipos.

Para generar ese archivo desde el entorno virtual activo:

```powershell
pip freeze > requirements.txt
```

---

## Ejecución

Antes de iniciar el asistente:

1. Activa el entorno virtual.
2. Comprueba que el archivo `.env` tenga las variables necesarias.
3. Inicia VTube Studio.
4. Carga el modelo Live2D que deseas utilizar.
5. Verifica que la API de VTube Studio esté disponible y que el token sea válido.
6. Ejecuta el programa:

```powershell
python main.py
```

El asistente preparará el avatar, reproducirá el saludo inicial y comenzará el ciclo de escucha y ejecución de comandos.

Para terminar, utiliza el comando de salida definido en el intérprete o presiona `Ctrl+C`. El programa debe liberar el controlador de boca al finalizar.

---

## Git y control de versiones

Git permite mantener un historial de los cambios y experimentar con nuevas funcionalidades sin poner en riesgo la versión estable.

Una organización posible es:

- `main`: versión estable del asistente.
- `develop`: integración de funcionalidades en desarrollo, si decides utilizar esta rama.
- `feature/nombre`: ramas para implementar nuevas características.
- `fix/nombre`: ramas para corregir errores.

Por ejemplo, una futura mejora de sincronización labial podría desarrollarse en una rama como `feature/lip-sync`, probarse y después integrarse en la rama correspondiente.

Los nombres de las ramas son una propuesta de organización; puedes adaptarlos a tu flujo de trabajo.

---

## Próximas mejoras

La arquitectura está pensada para ampliar las capacidades del asistente sin concentrar toda la lógica en un solo archivo.

Entre las funcionalidades previstas se encuentran:

- Incorporar más comandos de voz.
- Mejorar la interpretación del lenguaje natural.
- Consultar la fecha y otros datos útiles.
- Reproducir y controlar música.
- Consultar el clima.
- Buscar información en Internet y Wikipedia.
- Controlar YouTube y otros servicios de música.
- Abrir aplicaciones.
- Controlar el volumen del sistema.
- Gestionar archivos.
- Incorporar recordatorios.
- Mejorar el manejo de errores y las reconexiones.
- Reducir la latencia entre la solicitud y la respuesta.
- Implementar una sincronización labial más precisa.
- Añadir respuestas y expresiones más dinámicas del avatar.
- Mejorar las pruebas de los módulos y las integraciones.

La intención es que cada nueva capacidad tenga su propio módulo y que las funcionalidades compartidas, como hablar o controlar el avatar, se mantengan centralizadas.

---

## Estado del proyecto

**En desarrollo.**

El proyecto ya cuenta con una base modular y con las siguientes capacidades implementadas o integradas:

- Reconocimiento de voz mediante el micrófono.
- Interpretación básica de comandos.
- Síntesis de voz mediante Fish Audio.
- Configuración de una voz personalizada.
- Reproducción del audio generado mediante Pygame.
- Gestión de credenciales mediante variables de entorno.
- Conexión con VTube Studio.
- Activación de hotkeys del avatar.
- Movimiento de boca durante la reproducción de voz.
- Separación de responsabilidades entre voz, comandos, intérprete e integraciones.

Algunas funcionalidades adicionales, como los comandos de música, clima, comida y una sincronización labial más precisa, permanecen como objetivos de desarrollo.

## Objetivo final

Construir un asistente virtual modular en Python inspirado en **Kasane Teto**, capaz de escuchar, interpretar y responder a instrucciones mediante voz, mientras interactúa con un avatar Live2D.

El proyecto sirve como una oportunidad para aprender y mejorar progresivamente la programación en Python, la gestión de audio, el consumo de API, la concurrencia y el diseño de aplicaciones mantenibles.
