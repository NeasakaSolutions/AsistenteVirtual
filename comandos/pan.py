# Importaciones:
from voz.hablar import hablar
from config import NAME_USER
from comandos.avatar import (
     llorar,
     desactivar_llorar,
     activar_baguette,
     desactivar_baguette,
     ojos_estrella,
     desactivar_ojos_estrella
)

# Funcion para quitar pan:
def quitar_pan():

    # Acciones del modelo:
    desactivar_baguette()
    llorar()
    
    hablar(f"¡¡NOOOO! ¡¿POR QUÉ ERES ASÍ?! ¡Devuélvemelo, {NAME_USER}!"
           " ¡Le quitaste el pan de la boca a Teto-sama! ¡Eres un monstruo sin corazón, snif...!")

    # Acciones del modelo:
    desactivar_llorar()


# Funcion darpan:
def dar_pan():

    # Acciones del modelo:
    activar_baguette()
    ojos_estrella()

    hablar(f"¡¿Para mí?! ¡N-No pienses que con esto me vas a comprar, {NAME_USER}! "
           "...Pero no voy a rechazar un pan de tan buena calidad. ¡G-Gracias!")

    # Acciones del modelo:
    desactivar_ojos_estrella()