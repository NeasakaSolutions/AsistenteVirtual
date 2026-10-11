from config import NAME_USER
from voz.escuchar import escuchar
from voz.hablar import hablar
from core.interprete import ejecutar_comando
from integraciones.vtube_studio import cerrar_control_boca
from comandos.avatar import (
    eliminar_toggles,
    quitar_marca_de_agua,
    cambiar_ropa,
    ojos_corazon,
    desactivar_ojos_corazon
)


def welcome():
    # Preparar el modelo
    eliminar_toggles()
    quitar_marca_de_agua()
    cambiar_ropa()
    ojos_corazon()

    try:
        hablar(
            f"¡Oha-teto, {NAME_USER}! ¡Dejemos el pan a un lado "
            "por un segundo. ¿Qué se te ofrece? "
            "¿Quieres escuchar buena música o necesitas "
            "que busque algo por ti?"
        )
    finally:
        desactivar_ojos_corazon()


def ejecutar_asistente(detener_evento=None):
    try:
        welcome()

        while (
            detener_evento is None
            or not detener_evento.is_set()
        ):
            texto = escuchar(detener_evento)

            if detener_evento and detener_evento.is_set():
                break

            if not texto:
                continue

            continuar = ejecutar_comando(texto)

            if not continuar:
                break

    except KeyboardInterrupt:
        print("\nKasane Teto se detuvo.")

    finally:
        cerrar_control_boca()


def main():
    ejecutar_asistente()


if __name__ == "__main__":
    main()