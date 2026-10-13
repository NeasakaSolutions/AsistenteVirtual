# Importaciones:
import asyncio
import time
from twitchio.ext import commands
from config import TWITCH_TOKEN, TWITCH_CHANNEL, TWITCH_LEER_CHAT
from voz.hablar import hablar
from comandos_twitch.hora import decir_hora
from comandos_twitch.chibi import cambiar_escala
from comandos_twitch.pan import dar_pan, quitar_pan
from comandos_twitch.traje import cambiar_traje
from integraciones.youtube_music import gestor_musica
from comandos_twitch.chistes import (
    chiste,
    chiste_negro
)
from comandos_twitch.albur import (
    responder_albur,
    responder_alv,
)
from comandos_twitch.insultos import (
    insultar_kotori,
    insultar_rox,
    insultar_meowchele,
)
from comandos.avatar import (
    ojos_corazon,
    desactivar_ojos_corazon,
    activar_microfono,
    desactivar_microfono,
    activar_audifonos,
    desactivar_audifonos,
    sonrojar,
    desactivar_sonrojar,
    ojos_estrella,
    desactivar_ojos_estrella,
    mareo,
    desactivar_mareo
)

# Clase de kasane para leer el chat:
class KasaneTwitchBot(commands.Bot):

    # Validar el token disponible:
    def __init__(self):
        if not TWITCH_TOKEN or not TWITCH_CHANNEL:
            raise RuntimeError(
                "Configura TWITCH_TOKEN y TWITCH_CHANNEL en .env"
            )

        super().__init__(
            token=TWITCH_TOKEN,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL],
        )

        self.leer_chat = TWITCH_LEER_CHAT
        self.bloqueo_voz = asyncio.Lock()
        self.ultima_lectura = 0.0
        self.ultimo_comando = 0.0

        self.intervalo_lectura = 3.0
        self.intervalo_comando = 3.0

        # Comando disponibles:
        self.comandos = {
            # !music nombre de la cancion
            # !queu [muestra la cola de las canciones]
            # !skip [skipea una cancion]
            "!alv": responder_alv,
            "!huevos": responder_albur,
            "!meowchele": insultar_meowchele,
            "!kotori": insultar_kotori,
            "!rox": insultar_rox,
            "!traje": cambiar_traje,
            "!hora": decir_hora,
            "!chiste": chiste,
            "!chisten": chiste_negro,
            "!chibi": cambiar_escala,
            "!pan": dar_pan,
            "!quitarpan": quitar_pan,
            "!corazones": ojos_corazon,
            "!quitarcorazones": desactivar_ojos_corazon,
            "!microfono": activar_microfono,
            "!quitarmicrofono": desactivar_microfono,
            "!audifonos": activar_audifonos,
            "!quitaraudifonos": desactivar_audifonos,
            "!sonrojar": sonrojar,
            "!quitarsonrojo": desactivar_sonrojar,
            "!estrella": ojos_estrella,
            "!quitarestrella": desactivar_ojos_estrella,
            "!mareo": mareo,
            "!quitarmareo": desactivar_mareo,
        }

    async def event_ready(self):
        print(f"Kasane conectada a Twitch como: {self.nick}")
        print(f"Canal: {TWITCH_CHANNEL}")

    async def event_message(self, message):
        if message.echo or not message.author:
            return

        texto = message.content.strip()

        if not texto:
            return

        usuario = message.author.name
        print(f"[Twitch] {usuario}: {texto}")

        # Los mensajes que empiezan con ! son comandos.
        if texto.startswith("!"):
            await self.procesar_comando(texto, usuario)
            return

        # Leer mensajes normales con una pausa entre lecturas.
        if not self.leer_chat:
            return

        if len(texto) > 150:
            texto = texto[:150]
            print("[Twitch] Mensaje demasiado largo; se omite.")
            return

        ahora = time.monotonic()

        if ahora - self.ultima_lectura < self.intervalo_lectura:
            return

        self.ultima_lectura = ahora

        await self.hablar_en_cola(f"{usuario} dice: {texto}")

    async def hablar_en_cola(self, texto):
        async with self.bloqueo_voz:
            await asyncio.to_thread(hablar, texto)

    async def procesar_comando(self, texto, usuario):
        
        partes = texto.split(maxsplit=1)
        nombre = partes[0].lower()
        argumento = partes[1].strip() if len(partes) > 1 else ""

        # Solicitar una cancion:
        if nombre == "!music":

            if not argumento or len(argumento) > 120:
                return

            respuesta = await asyncio.to_thread(gestor_musica.agregar, argumento, usuario)

            print(f"[Youtube music] {respuesta}")
            return

        # Consultar la cola:
        if nombre == "!queue":

            respuesta = await asyncio.to_thread(gestor_musica.ver_cola)

            print(f"[Youtube Music] {respuesta}")

            return

        if nombre == "!skip":

            if usuario.lower() != TWITCH_CHANNEL.lower():
                return

            respuesta = gestor_musica.saltar()

            print(f"[Youtube music] {respuesta}")

            return

        ahora = time.monotonic()

        if ahora - self.ultimo_comando < self.intervalo_comando:
            return

        if nombre == "!habla":
            if not argumento or len(argumento) > 150:
                return

            self.ultimo_comando = ahora
            await self.hablar_en_cola(f"{usuario} dice: {argumento}")
            return

        funcion = self.comandos.get(nombre)

        if funcion is None:
            return

        self.ultimo_comando = ahora

        # Serializar acciones para evitar que el chat
        # interrumpa la reproduccion de voz.
        async with self.bloqueo_voz:
            if nombre in (
                "!pan", 
                "!quitarpan", 
                "!huevos", 
                "!alv", 
                "!chibi", 
                "!chiste",
                "!traje",
                "!chisten",
                ):
                await asyncio.to_thread(funcion, usuario)

            else:

                await asyncio.to_thread(funcion)


def iniciar_twitch():
    bot = KasaneTwitchBot()
    bot.run()
