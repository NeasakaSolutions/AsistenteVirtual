# Importaciones:
import random
from voz.hablar import hablar
from comandos.avatar import (
    activar_rostro_oscuro,
    desactivar_rostro_oscuro,
    ojos_oscuros,
    desactivar_ojos_oscuros
)

# Respuestas de teto:
RESPUESTAS_INSULTO_KOTORI = [
    (
        f"¡Ayyy, pero si es Kotori! El grandioso motociclista de Morelos... "
        "¡Bájale a tu ruidajo de motor que no me dejas concentrarme en comer mi baguette! "
        "A ver si te pones casco en la cabeza antes de andar dando vueltas por allá, ¡inconsciente!"
    ),
    (
        f"¡Mírenlo al Kotori, sintiéndose el rey de las curvas de Morelos en su motito! "
        " Te crees bien rudo, pero apuesto a que mis coletas de taladro son mil veces más aerodinámicas que tu casco. "
        "¡Llegaste haciendo un escándalo tremendo!"
    ),
    (
        f"¡Oye, Kotori! Con el calorón que hace allá en Morelos, "
        "¡tú pegado al motor de esa moto vas a terminar más horneado que un pan viejo!"
        " Haznos un favor a todos y apaga ese escape ruidoso, ¡que Teto-sama necesita silencio para su ensayo!"
    )
]


# Funcion principal
def insultar_kotori():

    #  Acciones del modelo:
    ojos_oscuros()
    activar_rostro_oscuro()

    respuesta = random.choice(RESPUESTAS_INSULTO_KOTORI)
    
    hablar(respuesta)

    # Acciones del modelo:
    desactivar_rostro_oscuro()
    desactivar_ojos_oscuros()