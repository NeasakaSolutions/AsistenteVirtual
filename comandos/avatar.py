# Importaciones:
import time
from integraciones.vtube_studio import activar_hotkey
from config import (
    VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES,
    VTS_HK_QUITAR_MARCA_DE_AGUA,
    VTS_HK_BAGUETTE,
    VTS_HK_VARIANTE_SV_UTAU,
    VTS_HK_MICROFONO,
    VTS_HK_AURICULARES,
    VTS_HK_CARA_OSCURA,
    VTS_HK_OJOS_OSCUROS,
    VTS_HK_MAQUILLAJE_ROJIZO,
    VTS_HK_OJOS_CORAZON,
    VTS_HK_OJOS_ESTRELLA,
    VTS_HK_OJOS_ENTRECERRADOS,
    VTS_HK_MODO_CHIBI,
    VTS_HK_LLORAR,
    VTS_HK_OJOS_MAREADOS
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
        return True

    except Exception as error:

        print(f"Error al activar: {error}")
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

    return activar_accion(VTS_HK_MICROFONO, "Activar microfono")

# Desactivar microfono
def desactivar_microfono():

    return activar_accion(VTS_HK_MICROFONO, "Desactivar microfono")

# Activar audifonos:
def activar_audifonos():

    return activar_accion(VTS_HK_AURICULARES, "Activar audifonos.")

# Desactivar audifonos:
def desactivar_audifonos():

    return activar_accion(VTS_HK_AURICULARES, "Desactivar audifonos")

""" EXPRESIONES DEL MODELO """

# Activar cara oscura:
def activar_rostro_oscuro():

    return activar_accion(VTS_HK_CARA_OSCURA, "Activar rostro oscuro.")

# Desactivar cara oscura:
def desactivar_rostro_oscuro():

    return activar_accion(VTS_HK_CARA_OSCURA, "Desactivar rostro oscuro.")

# Activar ojos oscuros:
def ojos_oscuros():

    return activar_accion(VTS_HK_OJOS_OSCUROS, "Activar ojos oscuros.")

# Activar ojos oscuros:
def desactivar_ojos_oscuros():

    return activar_accion(VTS_HK_OJOS_OSCUROS, "Desactivar ojos oscuros.")

# Sonrojar:
def sonrojar():

    return activar_accion(VTS_HK_MAQUILLAJE_ROJIZO, "Activar sonrojo")

# Desactivar el sonrojo:
def desactivar_sonrojar():

    return activar_accion(VTS_HK_MAQUILLAJE_ROJIZO, "Desactivar sonrojo")


# Activar ojos de cogeme:
def ojos_corazon():

    return activar_accion(VTS_HK_OJOS_CORAZON, "Activar ojos de corazon")

# Desactivar ojos de cogeme:
def desactivar_ojos_corazon():

    return activar_accion(VTS_HK_OJOS_CORAZON, "Desactivar ojos de corazon")

# Activar ojos de estrella:
def ojos_estrella():

    return activar_accion(VTS_HK_OJOS_ESTRELLA, "Activar ojos de estrella")

# Desactivar ojos de estrella:
def desactivar_ojos_estrella():

    return activar_accion(VTS_HK_OJOS_ESTRELLA, "Desactivar ojos de estrella")

# Activar ojos entrecerrados:
def ojos_entrecerrados():

    return activar_accion(VTS_HK_OJOS_ENTRECERRADOS, "Activar ojos entrecerrados")

# Desactivar ojos entrecerrados:
def desactivar_ojos_entrecerrados():

    return activar_accion(VTS_HK_OJOS_ENTRECERRADOS, "Desactivar ojos entrecerrados")

# Activar modo chibi:
def modo_chibi():

    return activar_accion(VTS_HK_MODO_CHIBI, "Activar modo chibi")

# Desactivar modo chibi
def desactivar_modo_chibi():

    return activar_accion(VTS_HK_MODO_CHIBI, "Desactivar modo chibi")

# Activar llorar:
def llorar():

    return activar_accion(VTS_HK_LLORAR, "Activar llorar")

# Desactivar llorar:
def desactivar_llorar():

    return activar_accion(VTS_HK_LLORAR, "Desactivar llorar")


# Activar mareo:
def mareo():

    return activar_accion(VTS_HK_OJOS_MAREADOS, "Activar mareo")

# Desactivar mareo:
def desactivar_mareo():

    return activar_accion(VTS_HK_OJOS_MAREADOS, "Desactivar mareo")



