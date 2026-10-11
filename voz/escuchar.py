import speech_recognition as sr

from config import IDIOMA, TIEMPO_ESCUCHA, PAUSE_THRESHOLD


# Inicializar el reconocedor de voz
listener = sr.Recognizer()
listener.pause_threshold = PAUSE_THRESHOLD
listener.dynamic_energy_threshold = True


def escuchar():
    while True:
        try:
            with sr.Microphone() as source:
                print("Escuchando...")

                # Ajustar el reconocimiento al ruido ambiente
                listener.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = listener.listen(
                    source,
                    phrase_time_limit=TIEMPO_ESCUCHA
                )

            print("Reconociendo...")

            texto = listener.recognize_google(
                audio,
                language=IDIOMA
            )

            texto = texto.lower().strip()

            if texto:
                print("Tú:", texto)
                return texto

        except sr.UnknownValueError:
            # No se entendió el audio.
            # No activar expresiones ni responder en voz alta.
            print("No se reconoció ninguna frase clara.")

        except sr.RequestError as error:
            print(f"Error con el reconocimiento: {error}")
            return ""

        except OSError as error:
            print(f"Error al acceder al micrófono: {error}")
            return ""