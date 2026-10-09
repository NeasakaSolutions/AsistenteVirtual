# Importaciones:
from integraciones.vtube_studio import activar_hotkey
from config import (
    VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES,
    VTS_HK_QUITAR_MARCA_DE_AGUA,
    VTS_HK_BAGUETTE,
    VTS_HK_VARIANTE_SV_UTAU,
    VTS_HK_MICROFONO
    )

# Funcion para activar los movimientos del modelo vtuber
def activar_accion(hotkey_id, nombre):

    # Validaciones:
    if not hotkey_id:

        print(f"No se configuro el atajo: {nombre}")
        return False

    try:

        # Realizar accion:
        activar_hotkey(hotkey_id)
        print(f"Accion activada: {nombre}")

    except Exception as error:

        print(f"Error al activar: {nombre}")
        return False

""" CONFIGURACION INICIAL DEL MODELO VTUBER """

# Eliminar acciones anteriores:
def eliminar_toggles():

    return activar_accion(VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES, "Eliminar todos los toggles")

# Eliminar la marca de agua:
def quitar_marca_de_agua():

    return activar_accion(VTS_HK_QUITAR_MARCA_DE_AGUA, "Eliminar marca de agua")

""" ACCESORIOS DEL MODELO VTBER """

# Activar baguette:
def activar_baguette():
    return activar_accion(VTS_HK_BAGUETTE, "Activar baguette")

# Desactivar baguette:
def desactivar_baguette():

    return activar_accion(VTS_HK_BAGUETTE, "Desactivar baguette")

# Funcion para cambiar de traje:
def cambiar_ropa():

    return activar_accion(VTS_HK_VARIANTE_SV_UTAU, "Cambiar traje")

# Activar microfono:
def activar_microfono():

    return activar_microfono(VTS_HK_MICROFONO, "Activar microfono")

# Desactivar microfono
def desactivar_microfono():

    return desactivar_microfono(VTS_HK_MICROFONO, "Desactivar microfono")

