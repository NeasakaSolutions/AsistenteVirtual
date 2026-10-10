# Importaciones:
import pyjokes
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
def chiste():

    try:
        chiste_generado = pyjokes.get_joke(language = "es", category= "neutral")

        # Acciones del modelo:
        ojos_entrecerrados()

        hablar("Te advierto que mi sentido del humor es una amenaza para la humanidad, "
            f"{NAME_USER}. Ahí va este chiste horrendo... "
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

        hablar(f"¡Agh! Se me fue el remate, {NAME_USER}... "
               "¡No te burles! Hasta la grandiosa Teto-sama necesita reiniciar su cerebro de quimera de vez en cuando.")

        # Acciones del modelo:
        desactivar_mareo()
        desactivar_rostro_oscuro()
        
    

