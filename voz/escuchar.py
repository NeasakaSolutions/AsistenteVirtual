# Importaciones:
import speech_recognition as sr

from config import IDIOMA, TIEMPO_ESCUCHA, PAUSE_THRESHOLD

# Inicializar el reconocedor de voz
listener = sr.Recognizer()
listener.pause_threshold = PAUSE_THRESHOLD
listener.dynamic_energy_threshold = True


def escuchar(detener_evento=None):
    while detener_evento is None or not detener_evento.is_set():
        try:
            with sr.Microphone() as source:
                print("Escuchando...")

                listener.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = listener.listen(
                    source,
                    timeout=1,
                    phrase_time_limit=TIEMPO_ESCUCHA
                )

            # No procesar audio si se solicito detener
            if detener_evento and detener_evento.is_set():
                return ""

            print("Reconociendo...")

            texto = listener.recognize_google(
                audio,
                language=IDIOMA
            )

            texto = texto.lower().strip()

            if texto:
                print("Tú:", texto)
                return texto

        except sr.WaitTimeoutError:
            # No se empezo a hablar durante el tiempo de espera
            continue

        except sr.UnknownValueError:
            print("No se reconoció ninguna frase clara.")

        except sr.RequestError as error:
            print(f"Error con el reconocimiento: {error}")
            return ""

        except OSError as error:
            print(f"Error al acceder al micrófono: {error}")
            return ""

    return ""