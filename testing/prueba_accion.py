import time

from config import VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES, VTS_HK_QUITAR_MARCA_DE_AGUA, VTS_HK_VARIANTE_SV_UTAU, VTS_HK_BAGUETTE
from integraciones.vtube_studio import activar_hotkey


if __name__ == "__main__":
    try:
        # Primera accion:
        print("Teto esta saludando")
        activar_hotkey(VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES)

        # Esperar a que termine la animación
        time.sleep(2)

        # Segunda accion
        print("Quitando marca de agua: ")
        activar_hotkey(VTS_HK_QUITAR_MARCA_DE_AGUA)

        time.sleep(2)

        print("Cambiando la ropa: ")
        activar_hotkey(VTS_HK_VARIANTE_SV_UTAU)

        time.sleep(2)

        print("Mandando baguette: ")
        activar_hotkey(VTS_HK_BAGUETTE)

        print("¡Prueba terminada!")

    except Exception as error:
        print(f"Error al activar la acción: {error}")
