# Importaciones:
import datetime
from voz.hablar import hablar

# Funcion principal
def decir_hora():

    # Depuracion del datetime:
    hora = datetime.datetime.now().strftime("%H:%M")

    hablar(f"¿La hora? ¡Facilísimo! Son las {hora}... ¡Oye, ya casi es hora de comer baguette!")