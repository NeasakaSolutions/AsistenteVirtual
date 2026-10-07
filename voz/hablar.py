# Importaciones:
import tempfile
import httpx
import pygame
from config import(FISH_API_KEY, FISH_VOICE_ID, FISH_MODEL)

pygame.mixer.init()

def hablar(texto):
    print("Kasane Teto: ", texto)

    # Manejo de errores:
    if not FISH_API_KEY:
        print("Error: No se encontro la API")
        return

    if not FISH_VOICE_ID:
        print("Error: no se esncuentro la voz")

    try:
        response = httpx.post("https://api.fish.audio/v1/tts", 
                              headers = {
                                "Authorization": f"Bearer {FISH_API_KEY}",
                                "Content-Type": "application/json",
                                "model": FISH_MODEL
                              }, json = {
                                "text": texto,
                                "reference_id": FISH_VOICE_ID,
                                "format": "mp3"
                              }, timeout = 20)
        
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(suffix = ".mp3", delete = False) as archivo:

            archivo.write(response.content)
            ruta_audio = archivo.name

        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except httpx.HTTPError as error:
        print(f"Error con Fish Audio: {error}")

    except Exception as error:
        print(f"Error reproduciendo la voz: {error}")



#import pyttsx3
#from config import VELOCIDAD_VOZ

# Variables de inicializacion:
#engine = pyttsx3.init()
#engine.setProperty("rate", VELOCIDAD_VOZ)

# Funcion para que el asistente hable:
#def hablar(texto):
    #print("Asistente:", texto)

    #engine.say(texto)
    #engine.runAndWait() # Esto va despues de cada say