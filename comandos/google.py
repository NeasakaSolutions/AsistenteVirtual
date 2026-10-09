# Importaciones:
import pywhatkit
from voz.hablar import hablar
from config import NAME_USER

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
        hablar(
            f"¿Y qué se supone que debo buscar, {NAME_USER}? " 
            "¡Mis poderes de Teto-sama no leen la mente!"
        )

        return

    try:

        # Respuesta del asistente:
        hablar(f"¿Eh? Busqué por todos lados y no encontré nada sobre '{busca}'. "
                    f"¡Seguro ni existe o lo dijiste mal, {NAME_USER}!")

        # Realizar busqueda:
        pywhatkit.search(busca)

    except Exception as error:

        # Debugin:
        print(f"Error con la busqueda en google: {error}")

        hablar("¡Oye, ocurrió un error rarísimo! Algo falló en la búsqueda... "
            "¡Seguro fue culpa de Miku o de mi conexión!")


