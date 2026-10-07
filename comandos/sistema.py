# Importaciones:
from config import NAME_USER
from voz.hablar import hablar

# Funcion principal:
def salir():

    # Mensaje que leera el asistente:
    hablar(f"¿Ya te vas, {NAME_USER}? Hmph... ¡no es como si fuera a extrañarte o algo así! Pero vuelve pronto, ¿vale? ¡Maaane-ne!")

    # Se pone False para cerrar el ciclo principal:
    return False