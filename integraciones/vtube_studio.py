# Importaciones
import asyncio
import json
import threading
import time
import math
import websockets

from config import URL_VTS, VTS_AUTH_TOKEN


# Conectar y autenticar con VTube Studio
async def conectar_vtube():
    if not VTS_AUTH_TOKEN:
        raise RuntimeError(
            "Falta configurar VTS_AUTH_TOKEN en el archivo .env"
        )

    websocket = await websockets.connect(
        URL_VTS,
        open_timeout=5
    )

    solicitud = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "MeowcheleAuthentication",
        "messageType": "AuthenticationRequest",
        "data": {
            "pluginName": "Meowchele",
            "pluginDeveloper": "Meowchele Project",
            "authenticationToken": VTS_AUTH_TOKEN
        }
    }

    try:
        await websocket.send(json.dumps(solicitud))
        respuesta = json.loads(await websocket.recv())

        if respuesta.get("messageType") == "APIError":
            raise RuntimeError(
                respuesta["data"].get(
                    "message", "Error de autenticación"
                )
            )

        if not respuesta.get("data", {}).get("authenticated", False):
            raise RuntimeError(
                "VTube Studio no autenticó a Meowchele."
            )

        return websocket

    except Exception:
        await websocket.close()
        raise


# Consultar hotkeys del modelo
async def consultar_hotkeys():
    websocket = await conectar_vtube()

    try:
        solicitud = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "MeowcheleListHotkeys",
            "messageType": "HotkeysInCurrentModelRequest",
            "data": {}
        }

        await websocket.send(json.dumps(solicitud))
        respuesta = json.loads(await websocket.recv())

        if respuesta.get("messageType") == "APIError":
            raise RuntimeError(respuesta["data"]["message"])

        hotkeys = respuesta.get("data", {}).get(
            "availableHotkeys", []
        )

        for hotkey in hotkeys:
            print(
                f"Nombre: {hotkey.get('name', 'Sin nombre')} | "
                f"ID: {hotkey.get('hotkeyID', 'Sin ID')}"
            )

        return hotkeys

    finally:
        await websocket.close()


# Activar una hotkey
async def _activar_hotkey(hotkey_id):
    websocket = await conectar_vtube()

    try:
        solicitud = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "MeowcheleTriggerHotkey",
            "messageType": "HotkeyTriggerRequest",
            "data": {
                "hotkeyID": hotkey_id
            }
        }

        await websocket.send(json.dumps(solicitud))
        respuesta = json.loads(await websocket.recv())

        if respuesta.get("messageType") == "APIError":
            raise RuntimeError(respuesta["data"]["message"])

        print("Hotkey activado correctamente.")

    finally:
        await websocket.close()


def activar_hotkey(hotkey_id):
    asyncio.run(_activar_hotkey(hotkey_id))


def listar_hotkeys():
    return asyncio.run(consultar_hotkeys())



# Control persistente del movimiento de boca

_evento_hablar = threading.Event()
_evento_cerrar_boca = threading.Event()
_hilo_boca = None


async def _inyectar_boca(websocket, valor):
    solicitud = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "MeowcheleMouthMovement",
        "messageType": "InjectParameterDataRequest",
        "data": {
            "faceFound": True,
            "mode": "set",
            "parameterValues": [
                {
                    "id": "MouthOpen",
                    "value": valor,
                    "weight": 1.0
                }
            ]
        }
    }

    await websocket.send(json.dumps(solicitud))
    respuesta = json.loads(await websocket.recv())

    if respuesta.get("messageType") == "APIError":
        raise RuntimeError(
            respuesta["data"].get(
                "message",
                "Error al controlar la boca"
            )
        )


async def _animar_boca():
    websocket = None

    try:
        # Abrir y autenticar una conexion que se reutilizara.
        websocket = await conectar_vtube()

        inicio = time.monotonic()
        estaba_hablando = False

        while not _evento_cerrar_boca.is_set():
            hablando = _evento_hablar.is_set()

            if hablando:
                tiempo = time.monotonic() - inicio

                # Oscilacion suave de apertura y cierre.
                valor = 0.15 + 0.65 * (
                    (1 + math.sin(2 * math.pi * 3 * tiempo)) / 2
                )

                await _inyectar_boca(websocket, valor)
                estaba_hablando = True

            elif estaba_hablando:
                # Cerrar la boca una sola vez al terminar.
                await _inyectar_boca(websocket, 0.0)
                estaba_hablando = False

            await asyncio.sleep(0.05)

    except Exception as error:
        print(f"Error en el movimiento de boca: {error}")

    finally:
        if websocket is not None:
            await websocket.close()


def _ejecutar_animacion_boca():
    asyncio.run(_animar_boca())


def iniciar_movimiento_boca():
    global _hilo_boca

    # Si el controlador ya esta conectado solo activa el movimiento.
    if _hilo_boca is not None and _hilo_boca.is_alive():
        _evento_hablar.set()
        return

    _evento_cerrar_boca.clear()
    _evento_hablar.set()

    _hilo_boca = threading.Thread(
        target=_ejecutar_animacion_boca,
        daemon=True
    )
    _hilo_boca.start()


def detener_movimiento_boca():
    # Detiene la animacion pero conserva la conexion.
    _evento_hablar.clear()


def cerrar_control_boca():
    # Llamar al cerrar modelo para liberar la conexion.
    global _hilo_boca

    _evento_hablar.clear()
    _evento_cerrar_boca.set()

    if _hilo_boca is not None:
        _hilo_boca.join(timeout=3)

    _hilo_boca = None
