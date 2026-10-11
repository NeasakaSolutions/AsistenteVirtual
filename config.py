# Importaciones:
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

if getattr(sys, "frozen", False):
    CARPETA_BASE = Path(sys.executable).resolve().parent
else:
    CARPETA_BASE = Path(__file__).resolve().parent

load_dotenv(CARPETA_BASE / ".env")

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

# Expresiones:
VTS_HK_CARA_OSCURA = os.getenv("VTS_HK_CARA_OSCURA")
VTS_HK_OJOS_OSCUROS = os.getenv("VTS_HK_OJOS_OSCUROS")
VTS_HK_MAQUILLAJE_ROJIZO = os.getenv("VTS_HK_MAQUILLAJE_ROJIZO")
VTS_HK_OJOS_CORAZON = os.getenv("VTS_HK_OJOS_CORAZON")
VTS_HK_OJOS_ESTRELLA = os.getenv("VTS_HK_OJOS_ESTRELLA")
VTS_HK_OJOS_ENTRECERRADOS = os.getenv("VTS_HK_OJOS_ENTRECERRADOS")
VTS_HK_MODO_CHIBI = os.getenv("VTS_HK_MODO_CHIBI")
VTS_HK_LLORAR = os.getenv("VTS_HK_LLORAR")
VTS_HK_OJOS_MAREADOS = os.getenv("VTS_HK_OJOS_MAREADOS")

