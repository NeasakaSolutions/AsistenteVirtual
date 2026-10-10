# Importaciones:
import random
from config import NAME_USER
from voz.hablar import hablar
from comandos.avatar import (
    activar_rostro_oscuro,
    desactivar_rostro_oscuro,
    ojos_oscuros,
    desactivar_ojos_oscuros
)

# Respuestas de teto:
RESPUESTAS_ALBUR = [
    (
        f"¡Ésos te los comes, {NAME_USER}! "
        "Y de paso me traes un baguette de la panadería. "
        "¡Con Teto-sama no te andes llevando así, insolente!"
    ),
    (
        f"¡Con catsup o en omelette, pero te los cenas enteros, {NAME_USER}! "
        "A ver si así se te quita lo chistoso..."
    ),
    (
        f"¡Con los que te atragantas, {NAME_USER}! "
        "Te los sirvo en plato de plata a ver si no te me ahogas, "
        "¡mensote!"
    )
]

# Funcion para respoder el albur:
def responder_albur():

    #  Acciones del modelo:
    ojos_oscuros()
    activar_rostro_oscuro()

    # Respuesta aleatoria:
    respuesta = random.choice(RESPUESTAS_ALBUR)

    # Asistente hablando:
    hablar(respuesta)

    # Acciones del modelo:
    desactivar_rostro_oscuro()
    desactivar_ojos_oscuros()



