# Importaciones:
from voz.hablar import hablar
from config import NAME_USER
from comandos.avatar import (
     cambiar_ropa, 
     ojos_estrella,
     desactivar_ojos_estrella
)

# Funcion principal
def cambiar_traje():

    # Acciones del modelo:
    cambiar_ropa()
    ojos_estrella()
    
    hablar(f"¡Luces, cámara y cambio de look! "
           "Dejé mi atuendo habitual un segundo para lucir este outfit increíble... "
           f"A ver, {NAME_USER}, dinos la verdad: ¿A que a Teto-sama todo le queda perfecto?")

    # Acciones del modelo:
    desactivar_ojos_estrella()