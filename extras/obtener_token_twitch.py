import os
import secrets
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlencode, urlparse, parse_qs
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID", "").strip()
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET", "").strip()
REDIRECT_URI = "http://localhost:3000"
SCOPES = ["chat:read"]

estado = secrets.token_urlsafe(24)
codigo_autorizacion = None
error_oauth = None


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global codigo_autorizacion, error_oauth

        parametros = parse_qs(urlparse(self.path).query)

        if parametros.get("state", [""])[0] != estado:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid OAuth state.")
            return

        if "error" in parametros:
            error_oauth = parametros["error"][0]
        else:
            codigo_autorizacion = parametros.get("code", [None])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            "<h2>Autorización recibida.</h2>"
            "<p>Ya puedes cerrar esta pestaña y volver a Kasane Teto.</p>"
            .encode("utf-8")
        )

    def log_message(self, *args):
        pass


def main():
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Falta TWITCH_CLIENT_ID o TWITCH_CLIENT_SECRET en .env")
        return

    servidor = HTTPServer(("localhost", 3000), CallbackHandler)

    parametros = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "state": estado,
    }

    url = "https://id.twitch.tv/oauth2/authorize?" + urlencode(parametros)

    print("Abriendo Twitch para autorizar Kasane Teto...")
    print("Si no se abre automáticamente, visita esta dirección:")
    print(url)

    threading.Thread(target=webbrowser.open, args=(url,), daemon=True).start()

    try:
        servidor.handle_request()
    finally:
        servidor.server_close()

    if error_oauth:
        print(f"Autorización cancelada o rechazada: {error_oauth}")
        return

    if not codigo_autorizacion:
        print("No se recibió el código de autorización.")
        return

    datos = urlencode({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": codigo_autorizacion,
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
            resultado = __import__("json").loads(respuesta.read())

        token = resultado["access_token"]

        print("\n¡Token generado!")
        print("Copia el valor siguiente en TWITCH_TOKEN dentro de .env:\n")
        print(token)
        print("\nNo compartas este token.")

    except HTTPError as error:
        print("Twitch rechazó la solicitud:", error.read().decode())


if __name__ == "__main__":
    main()