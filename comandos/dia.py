# Importaciones:
import datetime
from voz.hablar import hablar
from config import NAME_USER
from comandos.avatar import (
    ojos_estrella,
    desactivar_ojos_estrella
)

# Lista para los meses en espaniol:
meses = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]

# Funcion para dar el dia:
def decir_dia():

    # Depuracion del datetime:
    ahora = datetime.datetime.now()
    dia = ahora.day
    mes = meses[ahora.month - 1]
    anio = ahora.year

    # Acciones del modelo:
    ojos_estrella()

    hablar(f"¿En qué planeta vives {NAME_USER}, que no sabes el día?"
           f" Te lo perdono solo porque soy buena: hoy estamos a {dia} de"
            f" {mes} del año {anio}. ¡Anotado en tu calendario!")

    # Acciones del modelo:
    desactivar_ojos_estrella()
