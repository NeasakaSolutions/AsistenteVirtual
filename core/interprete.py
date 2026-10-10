# Importaciones:
from comandos.hora import decir_hora
from comandos.sistema import salir
from comandos.clima import consultar_clima
from comandos.comida import buscar_comida
from comandos.dia import decir_dia
from comandos.wikipedia import busqueda_wikipedia
from comandos.google import busqueda_google
from comandos.youtube import busqueda_youtube
from comandos.chistes import chiste
from comandos.captura import captura_pantalla
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

# Reconocer las palabras clave para las funciones:
def ejecutar_comando(texto):

    #print(f"[DEBUG] Comando recibido: {texto}") # Debugin

    # Wikipedia
    if "busca en wikipedia" in texto:
        # Ejecutar antes de la busqueda:
        desactivar_baguette()
        ojos_estrella()
        activar_audifonos()

        # Busqueda en wikipedia:
        busqueda_wikipedia(texto)

        # Ejecutar despues de la busqueda:
        activar_baguette()
        desactivar_ojos_estrella()
        desactivar_audifonos()

    # Google:
    elif "busca en google" in texto:
        # Ejecutar antes de la busqueda:

        # Realizar busqueda:
        busqueda_google(texto)

    # Youtube
    elif "busca en youtube" in texto:

        busqueda_youtube(texto)

    # Captura de pantalla:
    elif "captura de pantalla" in texto or "screenshot" in texto:

        captura_pantalla()

    # Chistes:
    elif "chiste" in texto or "chascarrillo" in texto:

        chiste()

    # Hora
    elif "hora" in texto:

        decir_hora()

    # Despedida
    elif "salir" in texto or "voy" in texto:

        return salir()

    # Dia:
    elif "día" in texto or "dia" in texto:

        decir_dia()

    # Clima:
    elif "clima" in texto or "tiempo" in texto:

        consultar_clima()

    # Comida
    elif "comida" in texto:

        buscar_comida()

    # En caso de no tener comando alguno:
    else:
        # Acciones del modelo:
        mareo()
        activar_rostro_oscuro()
        desactivar_baguette()

        # Respuesta:
        hablar("¡Oye! ¿Me viste cara de bola de cristal? No tengo esa función programada. "
               "Revisa bien tus comandos antes de pedirme cosas imposibles.")

        # Acciones del modelo:
        desactivar_mareo()
        desactivar_rostro_oscuro()
        activar_baguette()

    return True