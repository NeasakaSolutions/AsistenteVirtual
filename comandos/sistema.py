# Importaciones:
import time
from config import NAME_USER
from voz.hablar import hablar

# Funcion principal:
def salir():

    # Mensaje que leera el asistente:
    hablar(f"¿Ya te vas, {NAME_USER}? Hmph... ¡no es como si fuera a extrañarte o algo así! Pero vuelve pronto, ¿vale? ¡Maaane-ne!")
    #hablar(f"Nos retiramos por el momento, {NAME_USER}. Recuerda que con honestidad y trabajo los resultados continúan. Quedamos a la orden para la próxima jornada. ¡Hasta pronto!")
    time.sleep(5)
    # Se pone False para cerrar el ciclo principal:
    return False