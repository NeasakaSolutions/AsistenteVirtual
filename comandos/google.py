# Importaciones:
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

# Funcion para que no arroje tantos caracteres
def limitar_texto(texto, max_caracteres=400):
    # Limita la respuesta para evitar que el asistente hable demasiado.
    if len(texto) <= max_caracteres:
        return texto

    return texto[:max_caracteres].rsplit(" ", 1)[0] + "..."

# Funcion paralabusqueda en google:
def busqueda_google(busca):

    # Formatear el texto:
    busca = busca.replace("busca en google", "").strip()

    # Comprobar que el usuario especifico la busqueda:
    if not busca:

        # Acciones del modelo:
        mareo()

        hablar(
            f"¿Y qué se supone que debo buscar, {NAME_USER}? " 
            "¡Mis poderes de Teto-sama no leen la mente!"
        )

        # Acciones del modelo:
        desactivar_mareo()

        return

    try:

        # Acciones del modelo:
        ojos_estrella()
        activar_audifonos()

        # Respuesta del asistente:
        hablar(f"¡Aquí tienes, {NAME_USER}! Teto-sama encontró justo lo que buscabas sobre '{busca}'. "
               "¡Agradece que soy la mejor buscando en internet!")

        # Realizar busqueda:
        pywhatkit.search(busca)

        # Acciones modelo:
        desactivar_ojos_estrella()
        desactivar_audifonos()

    except Exception as error:

        # Debugin:
        print(f"Error con la busqueda en google: {error}")

        # Acciones del modelo:
        mareo()

        hablar("¡Oye, ocurrió un error rarísimo! Algo falló en la búsqueda... "
            "¡Seguro fue culpa de Miku o de mi conexión!")

        # Acciones del modelo:
        desactivar_mareo()


