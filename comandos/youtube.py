# Importaciones:
import pywhatkit
from voz.hablar import hablar
from config import NAME_USER
from comandos.avatar import (
    ojos_corazon,
    desactivar_ojos_corazon,
    activar_microfono,
    desactivar_microfono,
    mareo,
    desactivar_mareo,
)

# Funcion para la busqueda en youtube:
def busqueda_youtube(busca):

    # Formatear el texto:
    busca = busca.replace("busca en youtube", "").strip()

    # Validaciones para el usuario:
    if not busca:

        # Acciones del modelo:
        mareo()

        hablar(f"¿Y qué quieres que ponga, {NAME_USER}? " 
               "¡Teto-sama no puede adivinar tus gustos musicales!")

        # Acciones del modelo:
        desactivar_mareo()

        return

    try: 

        # Acciones del modelo:
        ojos_corazon()
        activar_microfono()

        hablar(f"¡Luces, cámara y acción! Buscando '{busca}'"
               f" en YouTube para el mejor público del mundo. ¡Dale play, {NAME_USER}!")

        # Acciones del modelo:
        desactivar_ojos_corazon()
        desactivar_microfono()

        # Busqueda del asistente:
        pywhatkit.playonyt(busca)

    except Exception as error:

        # Debugin:
        print(f"Error con la busqueda en youtube: {error}")

        # Acciones del modelo:
        mareo()

        hablar("¡Aaaah, fallo técnico! El escenario colapsó y no pude abrir YouTube..."
               f" ¡De seguro fue un sabotaje! Inténtalo otra vez, {NAME_USER}.")

        # Acciones del modelo:
        desactivar_mareo()
    
