# Importaciones:
import pyjokes
import random
from comandos.lista_chistes import chistes_malos
from voz.hablar import hablar
from config import NAME_USER
from comandos.avatar import (
    ojos_entrecerrados,
    desactivar_ojos_entrecerrados,
    mareo,
    desactivar_mareo,
    activar_rostro_oscuro,
    desactivar_rostro_oscuro
)


# Funcion para que el asistente diga un chiste:
def chiste(usuario = None):

    nombre = usuario or NAME_USER

    try:
        #chiste_generado = pyjokes.get_joke(language = "es", category= "neutral")
        chiste_generado = random.choice(chistes_malos)

        # Acciones del modelo:
        ojos_entrecerrados()

        hablar("Te advierto que mi sentido del humor es una amenaza para la humanidad, "
            f"{nombre}. Ahí va este chiste horrendo... "
            f"{chiste_generado}"
            " ¡Ríete por compromiso o no te hablo en todo el día!")

        # Acciones del modelo:
        desactivar_ojos_entrecerrados()

    except Exception as error:

        # Debug:
        print(f"Error al obtener un chiste: {error}")

        # Acciones del modelo:
        mareo()
        activar_rostro_oscuro()

        hablar(f"¡Agh! Se me fue el remate, {nombre}... "
               "¡No te burles! Hasta la grandiosa Teto-sama necesita reiniciar su cerebro de quimera de vez en cuando.")

        # Acciones del modelo:
        desactivar_mareo()
        desactivar_rostro_oscuro()
        
    

