# Importaciones:
from voz.hablar import hablar
from config import NAME_USER
from comandos.avatar import (
    modo_chibi,
    ojos_estrella,
    desactivar_ojos_estrella
)

# Funcion principal
def cambiar_escala():

    # Acciones del modelo:
    modo_chibi()
    ojos_estrella()
    

    hablar(f"¡Ta-daah! ¿Qué tal mi nueva escala, {NAME_USER}? "
           "Sea grande o pequeñita, ¡sigo siendo la grandiosa Teto-sama! Más te vale adorar esta forma.")

    # Acciones del modelo:
    desactivar_ojos_estrella()



