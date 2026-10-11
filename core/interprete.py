# Importaciones:
from comandos.hora import decir_hora
from comandos.sistema import salir
from comandos.clima import consultar_clima
from comandos.dia import decir_dia
from comandos.wikipedia import busqueda_wikipedia
from comandos.google import busqueda_google
from comandos.youtube import busqueda_youtube
from comandos.chistes import chiste
from comandos.captura import captura_pantalla
from comandos.chibi import cambiar_escala
from comandos.traje import cambiar_traje
from comandos.albur import responder_albur
from comandos.pan import quitar_pan, dar_pan
from voz.hablar import hablar
from comandos.avatar import (
    activar_baguette,
    desactivar_baguette,
    cambiar_ropa,
    activar_microfono,
    desactivar_microfono,
    activar_audifonos,
    desactivar_audifonos,
    activar_rostro_oscuro,
    desactivar_rostro_oscuro,
    ojos_oscuros,
    desactivar_ojos_oscuros,
    sonrojar,
    desactivar_sonrojar,
    ojos_corazon,
    desactivar_ojos_corazon,
    ojos_estrella,
    desactivar_ojos_estrella,
    ojos_entrecerrados,
    desactivar_ojos_entrecerrados,
    modo_chibi,
    desactivar_modo_chibi,
    llorar,
    desactivar_llorar,
    mareo,
    desactivar_mareo
    )

# Comandos de voz
def ejecutar_comando(texto):
    if not texto:
        return True

    texto = texto.lower().strip()

    # Comprobar si mencionaron a Kasane.
    nombres = ("kasane", "casane", "casani", "kasani")

    if not any(nombre in texto for nombre in nombres):
        return True

    # Wikipedia
    if "busca en wikipedia" in texto:
        ojos_estrella()
        activar_audifonos()

        try:
            busqueda_wikipedia(texto)
        finally:
            desactivar_ojos_estrella()
            desactivar_audifonos()

    # Google
    elif "busca en google" in texto:
        busqueda_google(texto)

    # YouTube
    elif "busca en youtube" in texto:
        busqueda_youtube(texto)

    # Captura de pantalla
    elif "captura de pantalla" in texto or "screenshot" in texto:
        captura_pantalla()

    # Chistes
    elif "chiste" in texto or "chascarrillo" in texto:
        chiste()

    # Hora
    elif "hora" in texto:
        decir_hora()

    # Despedida
    elif any(frase in texto for frase in (
        "me voy",
        "ya me voy",
        "adios",
        "adiós",
        "hasta luego",
        "nos vemos",
        "termina",
        "detente",
        "salir",
    )) or texto.endswith("salir") or texto.endswith("nos vemos"):
        return salir()

    # Día
    elif "día" in texto or "dia" in texto:
        decir_dia()

    # Clima
    elif "clima" in texto or "tiempo" in texto:
        consultar_clima()

    # Modo chibi
    elif "modo chibi" in texto:
        cambiar_escala()

    # Cambiar traje
    elif "ropa" in texto or "cambia de traje" in texto:
        cambiar_traje()

    # Responder albur
    elif "huevos" in texto:
        responder_albur()

    # Quitar el pan
    elif "quitar pan" in texto or "dame el pan" in texto:
        quitar_pan()

    # Dar pan
    elif any(frase in texto for frase in (
        "ten un pan",
        "dar un pan",
        "devolver el pan",
        "dar pan",
    )):
        dar_pan()

    # Comando no reconocido
    else:
        mareo()
        activar_rostro_oscuro()

        try:
            hablar(
                "¡Oye! ¿Me viste cara de bola de cristal? "
                "No tengo esa función programada. "
                "Revisa bien tus comandos antes de pedirme cosas imposibles."
            )
        finally:
            desactivar_mareo()
            desactivar_rostro_oscuro()

    return True
