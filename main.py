# Importaciones:
import speech_recognition as sr

# Variables:
listener = sr.Recognizer() # Reconocer la voz

# Bucle para reconocer palabras:
while True:

    # Activar microfono:
    with sr.Microphone() as source:
        print('Escuchando...')

        # Escuchar la voz:
        audio = listener.listen(source, phrase_time_limit = 5)

        try:
            # Decodificar audio a texto:
            print('Reconociendo...')
            text = listener.recognize_google(audio, language = 'es-US')
            print(text)
        
        except Exception as e:
            print('No se entendio el mensaje')
            print(e) # Imprimir error


