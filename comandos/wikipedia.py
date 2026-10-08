# Importaciones:
import wikipedia
from voz.hablar import hablar
from config import NAME_USER

#Configuracion para la api de wikipedia:
wikipedia.set_lang("es")
wikipedia.set_user_agent(
    "Kasane_Teto/1.0 (Asistente de voz educativo)"
)

# Funcion para que no arroje tantos caracteres
def limitar_texto(texto, max_caracteres=400):
    # Limita la respuesta para evitar que el asistente hable demasiado.
    if len(texto) <= max_caracteres:
        return texto

    return texto[:max_caracteres].rsplit(" ", 1)[0] + "..."

# Funcion para que el asistente busque en wikipedia:
def busqueda_wikipedia(busca):

    # Variables:
    busca = busca.replace("busca en wikipedia", "").strip() # Formatear busqueda:

    # Comprobar si el usuario no especificó qué buscar 
    if not busca: 
        hablar( f"¿Qué quieres que busque en Wikipedia, {NAME_USER}? "
                "¡No puedo leer tu mente todavía!" ) 
        return
    
    try:
        resultado = wikipedia.summary(busca, sentences = 2)
        resultado = limitar_texto(resultado)

        hablar(
            f"¡Atención, {NAME_USER}! Dejé mi baguette un segundo para investigar esto... "
            f"Según Wikipedia: '{resultado}'. "
            f"¡Aprende algo de la grandiosa Teto-sama!"
        )

    except wikipedia.exceptions.DisambiguationError:
        hablar(
            f"¡Ayyy, {NAME_USER}! Encontré demasiadas cosas sobre '{busca}'. "
            f"¡No me hagas adivinar! Sé más específico con lo que buscas."
        )

    except wikipedia.exceptions.PageError:
        hablar(
            f"¿Eh? Busqué por todos lados y no encontré nada sobre '{busca}'. "
            f"¡Seguro ni existe o lo dijiste mal, {NAME_USER}!"
        )

    except wikipedia.exceptions.HTTPTimeoutError:
        hablar(
            "¡Aaaah, qué lentitud! Wikipedia se tardó un siglo en responder. "
            "¡Mi paciencia y mi baguette tienen límite! Inténtalo otra vez."
        )

    except Exception as error:
        print(f"Error con Wikipedia: {error}")

        hablar(
            "¡Oye, ocurrió un error rarísimo! Algo falló en la búsqueda... "
            "¡Seguro fue culpa de Miku o de mi conexión!"
        )
    
