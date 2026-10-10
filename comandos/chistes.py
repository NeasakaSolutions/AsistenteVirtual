# Importaciones:
import pyjokes
from voz.hablar import hablar
from config import NAME_USER


# Funcion para que el asistente diga un chiste:
def chiste():

    try:
        chiste_generado = pyjokes.get_joke(language = "es", category= "neutral")

        hablar("Te advierto que mi sentido del humor es una amenaza para la humanidad, "
            f"{NAME_USER}. Ahí va este chiste horrendo... "
            f"{chiste_generado}"
            " ¡Ríete por compromiso o no te hablo en todo el día!")

    except Exception as error:

        # Debug:
        print(f"Error al obtener un chiste: {error}")

        hablar(f"¡Agh! Se me fue el remate, {NAME_USER}... "
               "¡No te burles! Hasta la grandiosa Teto-sama necesita reiniciar su cerebro de quimera de vez en cuando.")

        
    

