# Importaciones:
import pyautogui
import datetime
from config import CARPETA_CAPTURAS
from pathlib import Path
from config import NAME_USER
from comandos.avatar import ojos_estrella,desactivar_ojos_estrella
from voz.hablar import hablar

# Funcion para realizar captura de pantalla:
def captura_pantalla():

    try:
        # Carpeta a guardar las capturas realizadas por el asistente:
        carpeta = Path.home() / "Pictures" / f"{CARPETA_CAPTURAS}"

        # En caso de que no exista la carpeta:
        carpeta.mkdir(parents = True, exist_ok = True)

        # Obtener fecha y hora actual para nombrar la captura:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

        # Capturar nombre de la imagen:
        nombre_captura = f"{fecha_hora}.png"
        ruta_captura = carpeta / nombre_captura

        #Tomar y guardar la captura:
        captura = pyautogui.screenshot()
        captura.save(ruta_captura)

        # Acciones del modelo:
        ojos_estrella()

        # Asistente aviso:
        hablar(
            "¡Click! Teto-sama ha congelado tu pantalla con éxito."
            " ¡Que ni se te ocurra usar el arte de la grandiosa Teto para andar haciendo memes!"
        )

        # Debug:
        print(f"Captura guardada con exito en: {ruta_captura}")

        # Acciones del modelo:
        desactivar_ojos_estrella()

    except Exception as error:

        # Debug:
        print(f"Error al tomar la captura: {error}")

        hablar(
            f"¡Ayyy, {NAME_USER}! Falló el disparo... "
            "La pantalla se congeló y no pude tomar la captura. ¡Seguro fue un sabotaje de Miku!"
        )

    
    



