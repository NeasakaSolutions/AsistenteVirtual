#Importaciones:
import speech_recognition as sr
import pyttsx3
import datetime

# Variables:
listener = sr.Recognizer() # Reconocer la voz
listener.pause_threshold = 0.5 # Hacer que el asistente termine de escuchar mas rapido

# Hacer que  el asistente hable:
def hablar(texto):
    print("Asistente:", texto) # Muestra el texto que debe de leer

    # Configuracion de la voz
    engine = pyttsx3.init() # Hacer que hable el asistente
    engine.setProperty("rate", 200) # Velocidad con la que hablara
    engine.say(texto)
    engine.runAndWait() # Siempre va despues de un say
    engine.stop()

    del engine

# Funcion de bienvenida:
def welcome():
    hablar(
        "¡Meowchele-san! ¡Bienvenido! "
        "¿Qué necesitas? ¿Información, música o comida? "
        "Bueno, si es comida, yo me encargo."
    )

# Funcion para que el asistente escuche:
def escuchar():
    # Repetir la escucha del asistente:
    while True:

        # Activar microfono:
        with sr.Microphone() as source:

            print("Escuchando...")
            audio = listener.listen(source, phrase_time_limit=5) # Velocidad con la que hablara
            

        try:

            # Decodificar audio a texto:
            print("Reconociendo...")
            text = listener.recognize_google(audio, language="es-US")

            print("Tú:", text) # Debugin BORRAR

            return text.lower()

        except sr.UnknownValueError:

            print("No entendí el mensaje")
            hablar("No entendí el mensaje")

        except sr.RequestError as e:

            print("Error con el reconocimiento:", e)
            hablar("Hay un problema con el reconocimiento")

# Iniciar asistente:
welcome()

while True:
    text = escuchar()

    # Preguntar hora:
    if 'hora' in text:

        hora = datetime.datetime.now().strftime("%H:%M")
        hablar(f"Son las {hora}.")

    # Salir del asistente:
    elif "salir" in text:
        hablar("Alli nos vidrios Meowchele-san.")

        break



