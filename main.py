# Importaciones:
from config import NAME_USER
from voz.escuchar import escuchar
from voz.hablar import hablar
from core.interprete import ejecutar_comando

# Inicializar el asistente:
def welcome():

    hablar(
        f"¡Oha-teto, {NAME_USER}! ¡Dejemos el pan a un lado por un segundo! "
        " ¿Qué se te ofrece? ¿Quieres escuchar buena música o necesitas que busque algo por ti?"
    )
    #hablar(f"Muy buenos días a todas y a todos. Saludo con mucho afecto a {NAME_USER}. "
           #"Hoy informamos que este asistente se encuentra operando a toda su capacidad, "
           #f"con austeridad republicana y al servicio del pueblo. {NAME_USER}, "
           #"¿qué consulta, información o música requerimos atender el día de hoy?")

# Funcion principal:
def main():

    welcome()

    # Repetir para que el asistente siga escuchando:
    while True:

        texto = escuchar()

        continuar = ejecutar_comando(texto)

        if not continuar:
            break


if __name__ == "__main__":
    main()



