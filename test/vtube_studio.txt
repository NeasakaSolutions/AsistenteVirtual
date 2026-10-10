# Importaciones:
import asyncio
import json
import websockets
from config import URL_VTS, VTS_AUTH_TOKEN

# Promesa para conectar con y auntenticar con el modelo en vtube studio:
async def conectar_vtube():

    if not VTS_AUTH_TOKEN:
        raise RuntimeError(
            "Falta agregar el valor de VTS_AUTH_TOKEN en config o en .env"
        )

    websocket = await websockets.connect(URL_VTS, open_timeout = 5)

    solicitud = { "apiName": "VTubeStudioPublicAPI",
                 "apiVersion": "1.0",
                "requestID": "MeowcheleAuthentication",
                "messageType": "AuthenticationRequest",
                "data": { 
                    "pluginName": "Meowchele",
                    "pluginDeveloper": "Meowchele Project",
                    "authenticationToken": VTS_AUTH_TOKEN 
                    } 
                }

    await websocket.send(json.dumps(solicitud))
    respuesta = json.loads(await websocket.recv())

    if respuesta.get("messageType") == "APIError":
        await websocket.close()
        raise RuntimeError(respuesta["data"].get("message", "Error de autenticación"))

    datos = respuesta.get("data", {})

    if not datos.get("authenticated", False):
        await websocket.close()
        raise RuntimeError( "VTube Studio no autenticó a Meowchele." )
    return websocket

# Funcion para consultar los atajos para el modelo actual:
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

        hotkeys = respuesta.get("data", {}).get("availableHotkeys", [])

        print("\nHotkeys del modelo actual:")

        for hotkey in hotkeys:
            print( f"Nombre: {hotkey.get('name', 'Sin nombre')} | " f"ID: {hotkey.get('hotkeyID', 'Sin ID')}" )

        if not hotkeys:
            print("No se encontraron hotkeys.")

        return hotkeys

    finally:
        await websocket.close()

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

# Permite activar una expresion desde codigo asincrono:
def activar_hotkey(hotkey_id):
    asyncio.run(_activar_hotkey(hotkey_id))

# Consulta atajos desde codigo asincrono:
def listar_hotkeys():
    return asyncio.run(consultar_hotkeys())