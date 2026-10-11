# Importaciones
import wikipedia

from voz.hablar import hablar
from config import NAME_USER

from comandos.avatar import (
    activar_rostro_oscuro,
    desactivar_rostro_oscuro,
    mareo,
    desactivar_mareo,
)


# Configuración de Wikipedia
wikipedia.set_lang("es")
wikipedia.set_user_agent(
    "Kasane_Teto/1.0 (Asistente de voz educativo)"
)


def limitar_texto(texto, max_caracteres=400):
    if len(texto) <= max_caracteres:
        return texto

    return texto[:max_caracteres].rsplit(" ", 1)[0] + "..."


def busqueda_wikipedia(busca):
    # Normalizar el texto
    busca = busca.lower().strip()

    # Eliminar variantes del nombre del asistente
    busca = busca.replace("kasane teto", "")
    busca = busca.replace("kasane", "")
    busca = busca.replace("casane", "")
    busca = busca.replace("casani", "")
    busca = busca.replace("kasani", "")

    # Eliminar el comando de búsqueda
    busca = busca.replace("busca en wikipedia", "")
    busca = busca.replace("buscar en wikipedia", "")

    # Limpiar espacios sobrantes
    busca = " ".join(busca.split())

    if not busca:
        try:
            mareo()
            activar_rostro_oscuro()

            hablar(
                f"¿Qué quieres que busque en Wikipedia, {NAME_USER}? "
                "¡No puedo leer tu mente todavía!"
            )
        finally:
            desactivar_mareo()
            desactivar_rostro_oscuro()

        return

    try:
        resultado = wikipedia.summary(busca, sentences=2)
        resultado = limitar_texto(resultado)

        hablar(
            f"¡Atención, {NAME_USER}! Según Wikipedia: "
            f"'{resultado}'. "
            "¡Aprende algo de la grandiosa Teto-sama!"
        )

    except wikipedia.exceptions.DisambiguationError:
        try:
            mareo()
            activar_rostro_oscuro()

            hablar(
                f"¡Ayyy, {NAME_USER}! Encontré demasiados "
                f"resultados sobre '{busca}'. "
                "Sé más específico con lo que buscas."
            )
        finally:
            desactivar_mareo()
            desactivar_rostro_oscuro()

    except wikipedia.exceptions.PageError:
        try:
            mareo()
            activar_rostro_oscuro()

            hablar(
                f"No encontré información sobre '{busca}'. "
                f"Comprueba el término, {NAME_USER}, "
                "e inténtalo otra vez."
            )
        finally:
            desactivar_mareo()
            desactivar_rostro_oscuro()

    except wikipedia.exceptions.HTTPTimeoutError:
        try:
            mareo()
            activar_rostro_oscuro()

            hablar(
                "¡Wikipedia está tardando demasiado en responder! "
                "Inténtalo otra vez en un momento."
            )
        finally:
            desactivar_mareo()
            desactivar_rostro_oscuro()

    except Exception as error:
        print(f"Error con Wikipedia: {error}")

        try:
            mareo()
            activar_rostro_oscuro()

            hablar(
                "¡Ocurrió un error durante la búsqueda! "
                "Revisa tu conexión e inténtalo de nuevo."
            )
        finally:
            desactivar_mareo()
            desactivar_rostro_oscuro()