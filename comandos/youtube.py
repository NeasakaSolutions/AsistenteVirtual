# Importaciones:
import pywhatkit
from voz.hablar import hablar
from config import NAME_USER

# Funcion para la busqueda en youtube:
def busqueda_youtube(busca):

    # Formatear el texto:
    busca = busca.replace("busca en youtube", "").strip()

    # Validaciones para el usuario:
    if not busca:
        hablar(f"¿Y qué quieres que ponga, {NAME_USER}? " 
               "¡Teto-sama no puede adivinar tus gustos musicales!")

        return

    try: 
        hablar(f"¡Luces, cámara y acción! Buscando '{busca}'"
               f" en YouTube para el mejor público del mundo. ¡Dale play, {NAME_USER}!")

        # Busqueda del asistente:
        pywhatkit.playonyt(busca)

    except Exception as error:

        # Debugin:
        print(f"Error con la busqueda en youtube: {error}")

        hablar("¡Aaaah, fallo técnico! El escenario colapsó y no pude abrir YouTube..."
               f" ¡De seguro fue un sabotaje! Inténtalo otra vez, {NAME_USER}.")
    
