# Importaciones:
from comandos.hora import decir_hora
from comandos.sistema import salir
from comandos.musica import reproducir_musica
from comandos.clima import consultar_clima
from comandos.comida import buscar_comida
from comandos.dia import decir_dia
from voz.hablar import hablar

# Reconocer las palabras clave para las funciones:
def ejecutar_comando(texto):

    # Hora
    if "hora" in texto:

        decir_hora()

    # Despedida
    elif "salir" in texto or "voy" in texto:

        return salir()

    # Musica
    elif "música" in texto or "musica" in texto:

        reproducir_musica()

    # Dia:
    elif "día" in texto:
        decir_dia()

    # Clima:
    elif "clima" in texto:

        consultar_clima()

    # Comida
    elif "comida" in texto:

        buscar_comida()

    # En caso de no tener comando alguno:
    else:

        hablar("No conozco ese comando todavía.")

    return True