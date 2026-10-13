
import queue
import threading
import time
import webbrowser

from ytmusicapi import YTMusic


class GestorYouTubeMusic:
    def __init__(self):
        self.api = YTMusic()
        self.cola = queue.Queue()
        self.cooldown_por_usuario = 300  # 5 minutos
        self.ultimas_solicitudes = {}
        self.canciones_en_cola = set()
        self.lock = threading.Lock()
        self.cancion_actual = None

    def agregar(self, consulta, usuario):
        consulta = consulta.strip()
        usuario_id = usuario.lower()
        ahora = time.monotonic()

        if not consulta:
            return "Escribe el nombre de una canción después de !music."

        with self.lock:
            ultima = self.ultimas_solicitudes.get(usuario_id)

            if ultima is not None:
                restante = self.cooldown_por_usuario - (ahora - ultima)

                if restante > 0:
                    minutos = int(restante // 60)
                    segundos = int(restante % 60)
                    return (
                        f"{usuario}, debes esperar "
                        f"{minutos} min y {segundos} s "
                        "para pedir otra canción."
                    )

        try:
            resultados = self.api.search(
                consulta,
                filter="songs",
                limit=5,
            )
        except Exception as error:
            print(f"[YouTube Music] Error de búsqueda: {error}")
            return "No pude buscar esa canción. Inténtalo más tarde."

        if not resultados:
            return "No encontré esa canción."

        cancion = next(
            (
                resultado for resultado in resultados
                if resultado.get("videoId")
                and resultado.get("isAvailable", True)
            ),
            None,
        )

        if not cancion:
            return "No encontré una versión disponible de esa canción."

        video_id = cancion["videoId"]
        artistas = cancion.get("artists") or []
        artista = ", ".join(
            a.get("name", "")
            for a in artistas
            if a.get("name")
        )

        item = {
            "titulo": cancion.get("title", "Canción desconocida"),
            "artista": artista,
            "video_id": video_id,
            "usuario": usuario,
        }

        with self.lock:
            if video_id in self.canciones_en_cola:
                return "Esa canción ya está en la cola."

            self.canciones_en_cola.add(video_id)
            self.ultimas_solicitudes[usuario_id] = time.monotonic()

        self.cola.put(item)

        # Si no hay una canción actual, iniciar la reproducción.
        if self.cancion_actual is None:
            self._abrir_siguiente()

        return (
            f"Agregué a la cola: {item['titulo']} — "
            f"{artista or 'artista desconocido'} "
            f"(solicitada por {usuario})."
        )

    def ver_cola(self):
        with self.cola.mutex:
            canciones = list(self.cola.queue)

        lineas = []

        if self.cancion_actual:
            actual = self.cancion_actual
            lineas.append(
                f"Abierta: {actual['titulo']} — {actual['artista']}"
            )

        if not canciones:
            lineas.append("No hay canciones pendientes.")
            return "\n".join(lineas)

        lineas.append("Próximas canciones:")

        for posicion, item in enumerate(canciones[:8], start=1):
            lineas.append(
                f"{posicion}. {item['titulo']} — "
                f"{item['artista']} (por {item['usuario']})"
            )

        if len(canciones) > 8:
            lineas.append(f"Y {len(canciones) - 8} canciones más.")

        return "\n".join(lineas)

    def saltar(self):
        if self.cancion_actual:
            print(
                "[YouTube Music] Pasando de: "
                f"{self.cancion_actual['titulo']}"
            )

        self.cancion_actual = None
        self._abrir_siguiente()
        return "Se solicitó abrir la siguiente canción."

    def _abrir_siguiente(self):
        try:
            item = self.cola.get_nowait()
        except queue.Empty:
            self.cancion_actual = None
            return

        self.cancion_actual = item
        url = f"https://music.youtube.com/watch?v={item['video_id']}"

        try:
            webbrowser.open(url)
            print(
                f"[YouTube Music] Abriendo: "
                f"{item['titulo']} — {item['artista']}"
            )
        except Exception as error:
            print(f"[YouTube Music] No se pudo abrir Edge: {error}")
            self.cancion_actual = None
            with self.lock:
                self.canciones_en_cola.discard(item["video_id"])
            return

        with self.lock:
            self.canciones_en_cola.discard(item["video_id"])

        self.cola.task_done()


gestor_musica = GestorYouTubeMusic()
