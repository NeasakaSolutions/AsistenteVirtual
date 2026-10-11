# Importaciones
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


# Función para la búsqueda en YouTube
def busqueda_youtube(busca):
    # Normalizar el texto
    busca = busca.lower().strip()

    # Eliminar el nombre del asistente y el comando
    busca = busca.replace("kasane", "")
    busca = busca.replace("busca en youtube", "")
    busca = busca.replace("buscar en youtube", "")

    # Limpiar espacios sobrantes
    busca = " ".join(busca.split())

    # Validar la búsqueda
    if not busca:
        try:
            mareo()
            hablar(
                f"¿Y qué quieres que ponga, {NAME_USER}? "
                "¡Teto-sama no puede adivinar tus gustos musicales!"
            )
        finally:
            desactivar_mareo()

        return

    # Activar las expresiones del modelo
    try:
        ojos_corazon()
    except Exception as error:
        print(f"Error al activar los ojos de corazón: {error}")

    try:
        activar_microfono()
    except Exception as error:
        print(f"Error al activar el micrófono: {error}")

    # Anunciar la búsqueda
    try:
        hablar(
            f"¡Luces, cámara y acción! Buscando '{busca}' "
            "en YouTube para el mejor público del mundo. "
            f"¡Dale play, {NAME_USER}!"
        )
    except Exception as error:
        print(f"Error al anunciar la búsqueda: {error}")

    finally:
        # Desactivar cada acción independientemente
        try:
            desactivar_ojos_corazon()
        except Exception as error:
            print(f"Error al desactivar los ojos de corazón: {error}")

        try:
            desactivar_microfono()
        except Exception as error:
            print(f"Error al desactivar el micrófono: {error}")

    # Abrir YouTube
    try:
        pywhatkit.playonyt(busca)

    except Exception as error:
        print(f"Error con la búsqueda en YouTube: {error}")

        try:
            mareo()
            hablar(
                "¡Aaaah, fallo técnico! El escenario colapsó "
                "y no pude abrir YouTube... ¡De seguro fue un "
                f"sabotaje! Inténtalo otra vez, {NAME_USER}."
            )
        finally:
            desactivar_mareo()