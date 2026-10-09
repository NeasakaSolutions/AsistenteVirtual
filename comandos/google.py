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

    # Respuesta del asistente:
    hablar(f"¡Sacando los binoculares de Teto-sama! Buscando '{busca}'"
           f"en Google... ¡A ver qué sorpresas encontramos, {NAME_USER}!")

    # Realizar busqueda:
    pywhatkit.search(busca)


