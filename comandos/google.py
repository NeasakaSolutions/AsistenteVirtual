# Importaciones
import pywhatkit

from voz.hablar import hablar
from config import NAME_USER

from comandos.avatar import (
    ojos_estrella,
    desactivar_ojos_estrella,
    activar_audifonos,
    desactivar_audifonos,
    mareo,
    desactivar_mareo,
)


def limitar_texto(texto, max_caracteres=400):
    if len(texto) <= max_caracteres:
        return texto

    return texto[:max_caracteres].rsplit(" ", 1)[0] + "..."


def busqueda_google(busca):
    # Normalizar el texto
    busca = busca.lower().strip()

    # Eliminar variantes del nombre del asistente
    busca = busca.replace("kasane teto", "")
    busca = busca.replace("kasane", "")
    busca = busca.replace("casane", "")
    busca = busca.replace("casani", "")
    busca = busca.replace("kasani", "")

    # Eliminar el comando de búsqueda
    busca = busca.replace("busca en google", "")
    busca = busca.replace("buscar en google", "")

    # Limpiar espacios sobrantes
    busca = " ".join(busca.split())

    if not busca:
        try:
            mareo()
            hablar(
                f"¿Qué quieres que busque, {NAME_USER}? "
                "¡Mis poderes no leen la mente!"
            )
        finally:
            desactivar_mareo()

        return

    # Activar las acciones del modelo
    try:
        ojos_estrella()
        activar_audifonos()

        hablar(
            f"¡Aquí tienes, {NAME_USER}! "
            f"Teto-sama encontró justo lo que buscabas sobre "
            f"'{busca}'. ¡Soy la mejor buscando en internet!"
        )

    except Exception as error:
        print(f"Error al anunciar la búsqueda: {error}")

    finally:
        try:
            desactivar_ojos_estrella()
        except Exception as error:
            print(f"Error al desactivar los ojos de estrella: {error}")

        try:
            desactivar_audifonos()
        except Exception as error:
            print(f"Error al desactivar los audífonos: {error}")

    # Buscar en Google
    try:
        pywhatkit.search(busca)

    except Exception as error:
        print(f"Error con la búsqueda en Google: {error}")

        try:
            mareo()
            hablar(
                "¡Ocurrió un error al buscar en Google! "
                "Revisa tu conexión e inténtalo de nuevo."
            )
        finally:
            desactivar_mareo()