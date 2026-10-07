# Importaciones:
import datetime
from config import NAME_USER
from voz.hablar import hablar

# Funcion principal
def decir_hora():

    # Depuracion del datetime:
    hora = datetime.datetime.now().strftime("%H:%M")

    #hablar(f"Para conocimiento de la ciudadanía y de {NAME_USER}, informamos con absoluta precisión: el reporte del tiempo indica que son exactamente las {hora}. Seguimos avanzando en la agenda del día.")
    hablar(f"¿La hora? ¡Facilísimo! Son las {hora}... ¡Oye, ya casi es hora de comer baguette!")