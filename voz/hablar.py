# Importaciones:
import os
import tempfile
import pygame
from fishaudio import FishAudio
from fishaudio.utils import save
from config import FISH_API_KEY, FISH_VOICE_ID, FISH_MODEL

# Inicializar Fish Audio una sola vez:
cliente = FishAudio(api_key = FISH_API_KEY)

# Inicializar el reproductor una sola vez:
pygame.mixer.init()

# Funcion para que el asistente hable:
def hablar(texto):
    print("Kasane Teto: ", texto)

    # Manejo de errores respecto a Fish Audio
    if not FISH_API_KEY:
        print("Error: no se encontró FISH_API_KEY")
        return

    if not FISH_VOICE_ID:
        print("Error: no se encontró FISH_VOICE_ID")
        return

    ruta_audio = None

    try:
        # Crear archivo temporal
        archivo_temporal = tempfile.NamedTemporaryFile(suffix = ".mp3", delete = False)

        ruta_audio = archivo_temporal.name
        archivo_temporal.close()

        # Generar audio con Fish Audio
        audio = cliente.tts.convert(text = texto, reference_id = FISH_VOICE_ID, model = FISH_MODEL,)

        # Guardar el audio
        save(audio, ruta_audio)

        # Reproducir
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play()

        # Esperar mientras se reproduce
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as error:
        print(f"Error con Fish Audio: {error}")

    finally:

        # Limpiar el archivo temporal
        if ruta_audio and os.path.exists(ruta_audio):
            try:
                os.remove(ruta_audio)
            except OSError:
                pass

