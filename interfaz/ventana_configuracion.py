# Importaciones:
import os
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox,
    QScrollArea,
)
from configuracion import (
    obtener_valor,
    obtener_secreto,
    guardar_valores,
    guardar_secretos,
)


CAMPOS_SERVICIOS = {
    "NAME_USER": "Nombre con el que Kasane te llama",
    "FISH_VOICE_ID": "ID de voz de Fish Audio",
    "FISH_MODEL": "Modelo de Fish Audio",
    "URL_VTS": "Dirección de VTube Studio",
    "IDIOMA": "Idioma del reconocimiento",
    "TIEMPO_ESCUCHA": "Duración máxima de escucha (segundos)",
    "PAUSE_THRESHOLD": "Umbral de pausa",
    "LAT": "Latitud para el clima",
    "LON": "Longitud para el clima",
    "CARPETA_CAPTURAS": "Carpeta de capturas",
}

CAMPOS_SECRETOS = {
    "FISH_API_KEY": "Clave de Fish Audio",
    "WEATHER_API_KEY": "Clave de la API del clima",
    "VTS_AUTH_TOKEN": "Token de VTube Studio",
}

CAMPOS_HOTKEYS = {
    "VTS_HK_ELIMINAR_TODOS_LOS_TOGGLES": "Eliminar toggles",
    "VTS_HK_QUITAR_MARCA_DE_AGUA": "Quitar marca de agua",
    "VTS_HK_BAGUETTE": "Baguette",
    "VTS_HK_VARIANTE_SV_UTAU": "Cambiar ropa",
    "VTS_HK_MICROFONO": "Micrófono",
    "VTS_HK_AURICULARES": "Audífonos",
    "VTS_HK_CARA_OSCURA": "Cara oscura",
    "VTS_HK_OJOS_OSCUROS": "Ojos oscuros",
    "VTS_HK_MAQUILLAJE_ROJIZO": "Sonrojar",
    "VTS_HK_OJOS_CORAZON": "Ojos de corazón",
    "VTS_HK_OJOS_ESTRELLA": "Ojos de estrella",
    "VTS_HK_OJOS_ENTRECERRADOS": "Ojos entrecerrados",
    "VTS_HK_MODO_CHIBI": "Modo chibi",
    "VTS_HK_LLORAR": "Llorar",
    "VTS_HK_OJOS_MAREADOS": "Mareo",
}


class VentanaConfiguracion(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Configuración de Kasane Teto")
        self.resize(540, 650)

        self.campos = {}
        self.campos_secretos = {}

        principal = QVBoxLayout(self)
        principal.addWidget(
            QLabel(
                "Configura los servicios y el modelo de Kasane. "
                "Los cambios se guardan para este usuario."
            )
        )

        pestañas = QTabWidget()
        principal.addWidget(pestañas)

        # Pestaña de servicios
        servicios = QWidget()
        formulario_servicios = QFormLayout(servicios)

        for clave, etiqueta in CAMPOS_SERVICIOS.items():
            campo = QLineEdit()
            campo.setText(
                obtener_valor(clave, os.getenv(clave, ""))
            )
            self.campos[clave] = campo
            formulario_servicios.addRow(etiqueta, campo)

        for clave, etiqueta in CAMPOS_SECRETOS.items():
            campo = QLineEdit()
            campo.setEchoMode(QLineEdit.EchoMode.Password)
            campo.setPlaceholderText(
                "Deja vacío para conservar la clave guardada"
            )
            self.campos_secretos[clave] = campo
            formulario_servicios.addRow(etiqueta, campo)

        pestañas.addTab(servicios, "Servicios")

        # Pestaña de VTube Studio
        hotkeys = QWidget()
        formulario_hotkeys = QFormLayout(hotkeys)

        for clave, etiqueta in CAMPOS_HOTKEYS.items():
            campo = QLineEdit()
            campo.setText(obtener_valor(clave, os.getenv(clave, "")))
            self.campos[clave] = campo
            formulario_hotkeys.addRow(etiqueta, campo)

        aviso = QLabel(
            "Los IDs de las hotkeys deben corresponder a las "
            "acciones disponibles en el modelo de VTube Studio."
        )
        aviso.setWordWrap(True)
        formulario_hotkeys.addRow(aviso)

        desplazamiento = QScrollArea()
        desplazamiento.setWidgetResizable(True)
        desplazamiento.setWidget(hotkeys)

        pestañas.addTab(desplazamiento, "VTube Studio")

        # Botón para guardar
        boton_guardar = QPushButton("Guardar configuración")
        boton_guardar.clicked.connect(self.guardar)
        principal.addWidget(boton_guardar)

    def guardar(self):
        try:
            valores = {
                clave: campo.text().strip()
                for clave, campo in self.campos.items()
            }

            # Validaciones básicas
            try:
                segundos = int(valores["TIEMPO_ESCUCHA"])
                pausa = float(valores["PAUSE_THRESHOLD"])
            except ValueError:
                QMessageBox.warning(
                    self,
                    "Configuración inválida",
                    "La duración de escucha debe ser un entero "
                    "y el umbral de pausa debe ser numérico."
                )
                return

            if segundos <= 0 or pausa <= 0:
                QMessageBox.warning(
                    self,
                    "Configuración inválida",
                    "La duración y el umbral deben ser mayores que cero."
                )
                return

            valores["TIEMPO_ESCUCHA"] = segundos
            valores["PAUSE_THRESHOLD"] = pausa

            secretos = {
                clave: campo.text().strip()
                for clave, campo in self.campos_secretos.items()
            }

            # Guardar ajustes y credenciales
            guardar_valores(valores)
            guardar_secretos(secretos)

            QMessageBox.information(
                self,
                "Configuración guardada",
                "Los ajustes se guardaron correctamente. "
                "Algunos cambios pueden requerir reiniciar Kasane."
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Error al guardar",
                str(error)
            )