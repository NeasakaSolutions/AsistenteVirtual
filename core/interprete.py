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
from voz.hablar import hablar

# Reconocer las palabras clave para las funciones:
def ejecutar_comando(texto):

    #print(f"[DEBUG] Comando recibido: {texto}") # Debugin

    # Wikipedia
    if "busca en wikipedia" in texto:
        busqueda_wikipedia(texto)

    # Google:
    elif "busca en google" in texto:
        busqueda_google(texto)

    # Youtube
    elif "busca en youtube" in texto:
        busqueda_youtube(texto)

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
    elif "clima" in texto:

        consultar_clima()

    # Comida
    elif "comida" in texto:

        buscar_comida()

    # En caso de no tener comando alguno:
    else:

        hablar("¡Oye! ¿Me viste cara de bola de cristal? No tengo esa función programada. "
               "Revisa bien tus comandos antes de pedirme cosas imposibles.")

    return True