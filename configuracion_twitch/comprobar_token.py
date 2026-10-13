# Importaciones:
import os
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TWITCH_TOKEN", "").strip()

# TwitchIO debe recibir el token sin el prefijo "oauth:"
token = token.removeprefix("oauth:").strip()

if not token:
    print("No se encontró TWITCH_TOKEN en .env")
    raise SystemExit(1)

solicitud = Request(
    "https://id.twitch.tv/oauth2/validate",
    headers={"Authorization": f"OAuth {token}"},
)

try:
    with urlopen(solicitud, timeout=15) as respuesta:
        datos = json.loads(respuesta.read())

    print("Token válido")
    print("Cuenta:", datos.get("login"))
    print("Permisos:", datos.get("scopes"))
    print("Expira en segundos:", datos.get("expires_in"))

except HTTPError as error:
    print("Twitch rechazó el token. Código:", error.code)
    print(error.read().decode("utf-8", errors="replace"))
except Exception as error:
    print("No se pudo comprobar el token:", error)