# Importaciones:
from config import NAME_USER
from voz.escuchar import escuchar
from voz.hablar import hablar
from core.interprete import ejecutar_comando
from integraciones.vtube_studio import cerrar_control_boca
from comandos.avatar import (
    eliminar_toggles,
    quitar_marca_de_agua,
    activar_baguette,
    cambiar_ropa,
    ojos_corazon,
    desactivar_ojos_corazon
)

# Inicializar el asistente:
def welcome():

    # Preparar modelo:
    eliminar_toggles()
    quitar_marca_de_agua()
    cambiar_ropa()
    ojos_corazon()

    hablar(
        f"¡Oha-teto, {NAME_USER}! ¡Dejemos el pan a un lado por un segundo! "
        " ¿Qué se te ofrece? ¿Quieres escuchar buena música o necesitas que busque algo por ti?"
    )

    # Acciones del modelo:
    desactivar_ojos_corazon()

# Funcion principal:
def main():

    try:

        welcome()

        # Repetir para que el asistente siga escuchando:
        while True:

            texto = escuchar()

            continuar = ejecutar_comando(texto)

            if not continuar:
                break

    except KeyboardInterrupt:

        print("\nTeto se detuvo")

    finally:

        # Liberar conexion:
        cerrar_control_boca()
    


if __name__ == "__main__":
    main()



