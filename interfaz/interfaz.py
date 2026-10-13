# Importaciones:
import sys
import threading
from ventana_configuracion import VentanaConfiguracion
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
from main import ejecutar_asistente


class HiloAsistente(QThread):
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.detener_evento = threading.Event()

    def run(self):
        try:
            ejecutar_asistente(self.detener_evento)
        except Exception as error:
            self.error.emit(str(error))

    def detener(self):
        self.detener_evento.set()


class VentanaKasane(QWidget):


    def abrir_configuracion(self):
        self.ventana_config = VentanaConfiguracion()
        self.ventana_config.show()


    def __init__(self):
        super().__init__()

        self.hilo = None

        self.setWindowTitle("Kasane Teto")
        self.setMinimumWidth(350)

        self.estado = QLabel("Kasane está detenida.")
        self.estado.setWordWrap(True)

        self.boton_iniciar = QPushButton("Iniciar asistente")
        self.boton_detener = QPushButton("Detener asistente")
        self.boton_configuracion = QPushButton("Configuración")

        self.boton_detener.setEnabled(False)

        diseño = QVBoxLayout()
        diseño.addWidget(self.estado)
        diseño.addWidget(self.boton_iniciar)
        diseño.addWidget(self.boton_detener)
        diseño.addWidget(self.boton_configuracion)

        self.setLayout(diseño)

        self.boton_iniciar.clicked.connect(self.iniciar)
        self.boton_detener.clicked.connect(self.detener)
        self.boton_configuracion.clicked.connect(self.abrir_configuracion)

    def iniciar(self):
        if self.hilo is not None and self.hilo.isRunning():
            return

        self.hilo = HiloAsistente()
        self.hilo.finished.connect(self.asistente_terminado)
        self.hilo.error.connect(self.mostrar_error)

        self.estado.setText("Kasane está iniciando...")
        self.boton_iniciar.setEnabled(False)
        self.boton_detener.setEnabled(True)

        self.hilo.start()

    def detener(self):
        if self.hilo is not None and self.hilo.isRunning():
            self.estado.setText(
                "Deteniendo a Kasane... "
                "Puede terminar de hablar antes de detenerse."
            )
            self.boton_detener.setEnabled(False)
            self.hilo.detener()

    def asistente_terminado(self):
        self.estado.setText("Kasane está detenida.")
        self.boton_iniciar.setEnabled(True)
        self.boton_detener.setEnabled(False)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(
            self,
            "Error del asistente",
            mensaje
        )

    def closeEvent(self, evento):
        if self.hilo is not None and self.hilo.isRunning():
            self.hilo.detener()
            self.estado.setText("Esperando a que Kasane se detenga...")
            self.hilo.wait()

        evento.accept()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)

    ventana = VentanaKasane()
    ventana.show()

    sys.exit(aplicacion.exec())