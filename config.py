# Importaciones:
import os
from dotenv import load_dotenv

load_dotenv()

# Datos de usuario:
NAME_USER = "Meowchele-san"
LAT = os.getenv("LAT_LOCATION")
LON = os.getenv("LON_LOCATION")
CARPETA_CAPTURAS="CapturasTeto"

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

# VTUBER:
URL_VTS = os.getenv("URL_VTS")
VTS_AUTH_TOKEN = os.getenv("VTS_AUTH_TOKEN")

# Configuracion inicial de vtuber:
VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES = os.getenv("VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES")
VTS_HK_QUITAR_MARCA_DE_AGUA = os.getenv("VTS_HK_QUITAR_MARCA_DE_AGUA")

# Accesorios:
VTS_HK_BAGUETTE = os.getenv("VTS_HK_BAGUETTE")
VTS_HK_VARIANTE_SV_UTAU = os.getenv("VTS_HK_VARIANTE_SV_UTAU") # Cambia la ropa del modelo
VTS_HK_MICROFONO = os.getenv("VTS_HK_MICROFONO")
VTS_HK_AURICULARES = os.getenv("VTS_HK_AURICULARES")

