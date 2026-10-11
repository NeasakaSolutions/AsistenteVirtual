import keyring
from PySide6.QtCore import QSettings

ORGANIZACION = "KasaneTeto"
APLICACION = "KasaneTeto"
SERVICIO_SECRETOS = "KasaneTeto"

ajustes = QSettings(ORGANIZACION, APLICACION)

CLAVES_SECRETAS = {
    "FISH_API_KEY",
    "WEATHER_API_KEY",
    "VTS_AUTH_TOKEN",
}


def obtener_valor(clave, predeterminado=""):
    valor = ajustes.value(clave, predeterminado)
    return str(valor) if valor is not None else predeterminado


def guardar_valores(valores):
    for clave, valor in valores.items():
        ajustes.setValue(clave, valor)

    ajustes.sync()

    if ajustes.status() != QSettings.Status.NoError:
        raise RuntimeError("No se pudieron guardar los ajustes.")


def obtener_secreto(clave):
    try:
        return keyring.get_password(SERVICIO_SECRETOS, clave) or ""
    except Exception as error:
        raise RuntimeError(
            "No se pudo acceder al almacén de credenciales."
        ) from error


def guardar_secretos(secretos):
    for clave, valor in secretos.items():
        if clave not in CLAVES_SECRETAS:
            raise ValueError(f"Clave secreta no permitida: {clave}")

        if valor:
            keyring.set_password(
                SERVICIO_SECRETOS,
                clave,
                valor
            )