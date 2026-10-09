# Importaciones:
import os
from dotenv import load_dotenv

load_dotenv()

# Reconocimiento de voz:
IDIOMA = "es-US"
#VELOCIDAD_VOZ = 200
TIEMPO_ESCUCHA = 4
PAUSE_THRESHOLD = 0.5

# Fish Audio:
FISH_API_KEY = os.getenv("FISH_API_KEY")
FISH_VOICE_ID = os.getenv("FISH_VOICE_ID")
FISH_MODEL = "s2.1-pro-free"

# Clima:
WEATHER_API_KEY = os.getenv("WHEATHER_API_KEY")

# Datos de usuario:
NAME_USER = "Meowchele-san"
LAT = os.getenv("LAT_LOCATION")
LON = os.getenv("LON_LOCATION")
