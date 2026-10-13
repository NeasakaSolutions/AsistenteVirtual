# Importaciones:
import os
import secrets
import threading
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from dotenv import load_dotenv

load_dotenv()

# Cargar variables de entorno:
CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPES = ["chat:read"]

# Variables extras:
estado_esperado = secrets.token_urlsafe(24)
resultado = {}


# Clase para solicitar el token:
class ManejadorCallback(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parametros = parse_qs(urlparse(self.path).query)

        if parametros.get("state", [""])[0] != estado_esperado:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Estado OAuth invalido.")
            return

        if "error" in parametros:
            resultado["error"] = parametros.get("error_description", parametros["error"])[0]
        else:
            resultado["code"] = parametros.get("code", [None])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            "Autorizacion recibida. Puedes cerrar esta ventana."
            .encode("utf-8")
        )

    def log_message(self, format, *args):
        pass


def main():
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Faltan TWITCH_CLIENT_ID o TWITCH_CLIENT_SECRET en .env")
        return

    servidor = HTTPServer(("localhost", 3000), ManejadorCallback)
    servidor.timeout = 180

    parametros = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "state": estado_esperado,
    }

    url = (
        "https://id.twitch.tv/oauth2/authorize?"
        + urlencode(parametros)
    )

    print("Abriendo Twitch para autorizar la aplicacion...")
    webbrowser.open(url)
    print("Esperando la autorizacion (maximo 3 minutos)...")

    try:
        servidor.handle_request()
    finally:
        servidor.server_close()

    if resultado.get("error"):
        print("Error de autorizacion:", resultado["error"])
        return

    codigo = resultado.get("code")
    if not codigo:
        print("No se recibio el codigo de autorizacion.")
        return

    datos = urlencode({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": codigo,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    }).encode()

    solicitud = Request(
        "https://id.twitch.tv/oauth2/token",
        data=datos,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )

    try:
        with urlopen(solicitud, timeout=20) as respuesta:
            tokens = __import__("json").loads(respuesta.read())

        print("\nAutorizacion completada.")
        print("Access token:")
        print(tokens["access_token"])
        print("\nTiempo de validez (segundos):", tokens.get("expires_in"))
        print("Permisos:", tokens.get("scope", []))

        if tokens.get("refresh_token"):
            print("\nRefresh token:")
            print(tokens["refresh_token"])
            print("\nGuarda ambos tokens en un lugar seguro.")

    except HTTPError as error:
        print("Twitch rechazo la solicitud:", error.code)
        print(error.read().decode("utf-8", errors="replace"))
    except Exception as error:
        print("No se pudo obtener el token:", error)


if __name__ == "__main__":
    main()
