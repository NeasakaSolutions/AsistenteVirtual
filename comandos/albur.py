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


# Funcion para respoder el albur:
def responder_albur():

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

# Funcion para respoder cuando la mandan alv
def responder_alv():

    RESPUESTAS_ALV = [
        (
            f"¡¿A DÓNDE DICES?! ¡A la verga te vas a ir tú, grosero! "
            "¡A Teto-sama nadie le habla así!"
            " ¡Agradece que soy un programa y no te puedo lanzar un baguette en la cara!"
        ),
        (
            f"¡Qué elegancia la tuya, {NAME_USER}! "
            " ¡Qué falta de respeto para una Diva de mi calibre! Me voy a mi rincón a comer mi pan y ni pienses que te voy a pedir perdón."
        ),
        (
            f"¡Órale! ¡Mucho pico y poca acción, {NAME_USER}! "
            " Te me vas calmando o te borro el historial de la compu para que aprendas a respetar a Teto-sama."
        )
    ]

    #  Acciones del modelo:
    ojos_oscuros()
    activar_rostro_oscuro()

    # Respuesta aleatoria:
    respuesta = random.choice(RESPUESTAS_ALV)

    # Asistente hablando:
    hablar(respuesta)

    # Acciones del modelo:
    desactivar_rostro_oscuro()
    desactivar_ojos_oscuros()



