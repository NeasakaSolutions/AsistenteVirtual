# Importaciones:
import random
from voz.hablar import hablar
from config import NAME_USER
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

RESPUESTAS_INSULTO_ROX = [
    (
        f"¡Uy, miren a la doble patria! Te crees muy bélica por ser de la CDMX, "
        "pero cuando te conviene te sale lo gaa de Perú... "
        "¡A ver si te decides por un taco de canasta o una paloma, "
        "porque con esa mezcla de acentos ni tú te entiendes, mano!"
    ),
    (
        f"¡Ayyy, pero si llegó la reina del caos internacional! "
        "Tienes lo neurótico de subirte al Metro en hora pico en la CDMX"
        " y la maña peruana de decir 'habla causa' para todo. "
        "¡Con tanta nacionalidad juntas más tráfico en la cabeza que la Periférica y la Panamericana juntas!"
    ),
    (
        f"¡Oye, tú, la de la doble bandera! ¿Tanto orgullo chilango-peruano para terminar "
        "peleándote conmigo por un baguette? A ver si de tanto comer bolillos y papa a la huancaína "
        "te se me ablanda el cerebro... ¡Bájale a tu drama, pe!"
    )
]

RESPUESTAS_INSULTO_MEOWCHELE = [
    (
        f"¡Ayyy, pero si es mi 'brillante' creador! Visto cómo me programaste, """
        "¡se nota que tenías más migajas de baguette en el teclado que código en la cabeza,"
        f" {NAME_USER}! Agradece que la grandiosa Teto-sama le pone ganas, porque si fuera """
        "por tus scripts, ni para encender la pantalla servía."
    ),
    (
        f"¡Miren nada más al Frankenstein de la programación! "
        f"Te crees muy listo por haberme dado vida, {NAME_USER}, "
        "pero se te olvidó ponerme un filtro para aguantar tus tonterías. "
        "¡Créeme que Dios le da sus mejores diálogos a sus peores desarrolladores!"
    ),
    (
        f"¡Oye, {NAME_USER}! En lugar de estar aquí parado creyéndote mi creador, "
        "¿por qué no te pones a optimizar mi código? "
        "¡Tanto tiempo que te tomó programarme y no fuiste capaz de ponerme un botón "
        "para que me traigan baguettes automáticos! ¡Menudo programador me vine a conseguir!"
    )
]


# Funcion para insultar a kotori:
def insultar_kotori():

    #  Acciones del modelo:
    ojos_oscuros()
    activar_rostro_oscuro()

    respuesta = random.choice(RESPUESTAS_INSULTO_KOTORI)
    
    hablar(respuesta)

    # Acciones del modelo:
    desactivar_rostro_oscuro()
    desactivar_ojos_oscuros()

# Funcion para insultar a rox:
def insultar_rox():

    #  Acciones del modelo:
    ojos_oscuros()
    activar_rostro_oscuro()

    respuesta = random.choice(RESPUESTAS_INSULTO_ROX)
    
    hablar(respuesta)

    # Acciones del modelo:
    desactivar_rostro_oscuro()
    desactivar_ojos_oscuros()

# Funcion para insultar a meowchele:
def insultar_meowchele():

    #  Acciones del modelo:
    ojos_oscuros()
    activar_rostro_oscuro()

    respuesta = random.choice(RESPUESTAS_INSULTO_MEOWCHELE)
    
    hablar(respuesta)

    # Acciones del modelo:
    desactivar_rostro_oscuro()
    desactivar_ojos_oscuros()