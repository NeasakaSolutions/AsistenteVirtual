# Importaciones:
import asyncio
import json
import websockets
from config import URL_VTS

async def probar_conexion():

    try:
        async with websockets.connect(URL_VTS) as websocket:
            print("La conexion con VTube Studio es correcta. ")

            solicitud = { 
                "apiName": "VTubeStudioPublicAPI", 
                "apiVersion": "1.0", 
                "requestID": "MeowcheleAuth", 
                "messageType": "AuthenticationTokenRequest", 
                "data": { 
                    "pluginName": "Meowchele", 
                    "pluginDeveloper": "Meowchele Project" 
                    } 
            }

            await websocket.send(json.dumps(solicitud))

            respuesta = json.loads(await websocket.recv())

            print("Respuesta de VTube Studio:")
            print(json.dumps(respuesta, indent=4, ensure_ascii=False))

    except Exception as error:
        print(f"Error durante la conexión: {error}")

if __name__ == "__main__":
    asyncio.run(probar_conexion())