# Importaciones:
import speech_recognition as sr
from config import (IDIOMA, TIEMPO_ESCUCHA, PAUSE_THRESHOLD)
from voz.hablar import hablar
from comandos.avatar import (
    mareo,
    desactivar_mareo,
    activar_rostro_oscuro,
    desactivar_rostro_oscuro
)

# Variables de inicializacion:
listener = sr.Recognizer()
listener.pause_threshold = PAUSE_THRESHOLD

# Funcion para que el asistente decodifique el audio a texto:
def escuchar():

    while True:

        with sr.Microphone() as source:

            print("Escuchando...")

            audio = listener.listen(source, phrase_time_limit=TIEMPO_ESCUCHA) # Velocidad con la que hablara

        try:
            # Decodificar audio a texto
            print("Reconociendo...")

            texto = listener.recognize_google(audio, language=IDIOMA) # Idioma del asistente

            print("Tú:", texto) # Debugin

            return texto.lower()

        except sr.UnknownValueError:

            # Acciones del modelo:
            activar_rostro_oscuro()
            mareo()

            print("No entendí el mensaje")
            hablar("Eh... ¿eso era idioma humano o qué? "
                   " No te entendí nada. ¡A ver, dímelo otra vez, pero despacio!")

            # Acciones del modelo:
            desactivar_rostro_oscuro()
            desactivar_mareo()

        except sr.RequestError as error:

             # Acciones del modelo:
            activar_rostro_oscuro()
            mareo()

            print("Error con el reconocimiento:", error)
            hablar("Hay un problema con el reconocimiento")

            # Acciones del modelo:
            desactivar_rostro_oscuro()
            desactivar_mareo()