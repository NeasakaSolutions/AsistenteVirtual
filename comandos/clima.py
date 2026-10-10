# Importaciones:
import requests
from config import WEATHER_API_KEY, LAT, LON, NAME_USER
from voz.hablar import hablar
from comandos.avatar import (
     activar_audifonos,
     desactivar_audifonos,
     ojos_estrella,
     desactivar_ojos_estrella,
     mareo,
     desactivar_mareo,
     activar_rostro_oscuro,
     desactivar_rostro_oscuro
)

# Funcion principal:
def consultar_clima():

     hablar(f"¡Espérame ahí, {NAME_USER}! Sacando mis sensores de chimera para ver el clima... "
           "¡A ver si hoy ocupas paraguas o si nos derretimos!")

     url = "https://api.openweathermap.org/data/2.5/weather"

     parametros = {
        "lat": LAT,
        "lon": LON,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "es"
     }

     try:
          respuesta = requests.get(url, params = parametros, timeout = 10)

          respuesta.raise_for_status()
          datos = respuesta.json()

          temperatura = datos["main"]["temp"]
          sensacion = datos["main"]["feels_like"]
          clima = datos["weather"][0]["description"]

          temperatura_voz = f"{temperatura:.1f}".replace(".", " punto ")
          sensacion_voz = f"{sensacion:.1f}".replace(".", " punto ")

          mensaje = (
         f"¡Sintonizando el canal meteorológico de Teto-sama, {NAME_USER}!"
         f" El termómetro marca {temperatura_voz} grados Celsius, el cielo está {clima}"
         f" y la sensación térmica es de {sensacion_voz} grados. "
         "¡Agradece que la Diva Teto te mantiene informado!"
          )

          # Acciones del modelo:
          ojos_estrella()
          activar_audifonos()

          # Respuesta del modelo:
          hablar(mensaje)

          # Acciones del modelo:
          desactivar_ojos_estrella()
          desactivar_audifonos()

     except requests.exceptions.Timeout:

          # Debug:
          print("Error : La consulta excedio el tiempo de espera.")

          # Acciones del modelo:
          activar_audifonos()
          mareo()
          activar_rostro_oscuro()

          hablar("¡Oye, esto no avanza! La consulta se congeló... "
             f"¡Seguro Miku nos saturó la red! Dame un segundo e inténtalo otra vez, {NAME_USER}.")

          # Acciones del modelo:
          desactivar_audifonos()
          desactivar_mareo()
          desactivar_rostro_oscuro()

     except requests.exceptions.RequestException as error:

          print(f"Error al consultar el clima: {error}")

          # Acciones del modelo:
          activar_audifonos()
          mareo()
          activar_rostro_oscuro()
          
          hablar(
               "¡Agh! Sin conexión con el servicio meteorológico... "
               "¡El clima le tiene miedo a Teto-sama o seguro el servidor se cayó por culpa de Miku! "\
               f"No pude conseguir nada, {NAME_USER}."
          )

          # Acciones del modelo:
          desactivar_audifonos()
          desactivar_mareo()
          desactivar_rostro_oscuro()

     except (KeyError, IndexError, ValueError) as error:

          # Debug:
          print(f"Error al interpretar los datos del clima: {error}")

          # Acciones del modelo:
          activar_audifonos()
          mareo()
          activar_rostro_oscuro()

          hablar(
               "¡Ayyy, qué código tan extraño!"
               " El reporte del tiempo viene en un idioma extraterrestre y no pude procesarlo. "
               f"¡Prueba otra vez, {NAME_USER}!"
          )

          # Acciones del modelo:
          desactivar_audifonos()
          desactivar_mareo()
          desactivar_rostro_oscuro()


