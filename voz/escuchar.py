# Importaciones:
import speech_recognition as sr
from config import (IDIOMA, TIEMPO_ESCUCHA, PAUSE_THRESHOLD)
from voz.hablar import hablar

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

            print("No entendí el mensaje")
            hablar("No entendí el mensaje")

        except sr.RequestError as error:

            print("Error con el reconocimiento:", error)
            hablar("Hay un problema con el reconocimiento")