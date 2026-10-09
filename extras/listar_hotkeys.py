# Importaciones:
from integraciones.vtube_studio import listar_hotkeys

if __name__ == "__main__":

    try:
        listar_hotkeys()

    except Exception as error:
        print(f"No se pudieron consultar las expresiones: {error}")
