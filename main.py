# Módulo main.py
""" Este será el cerebro de nuestro programa y nuestra app."""

# Importamos las librerías.
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

# Importamos los módulos
from ui.ventana import centrar_ventana
from ui.botones import crear_boton, mostrar_historial
from ui.temas import aplicar_estilo
from logica.logica import incrementar, decrementar, reiniciar

# Creamos la clase principal usando POO
class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana principal.
        self.setWindowTitle("Contador Clics")
        self.setGeometry(150, 150, 250, 260)
        centrar_ventana(self)

        # --- Layout Principal ---
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # --- Etiquetas de la app ---
        self.etiqueta = QLabel("Clics: 0")
        self.etiqueta.setStyleSheet("font-size: 20px; padding: 8px;")
        self.etiqueta.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.etiqueta)

        # --- Botones ---
        btn_sumar = crear_boton("+1", self.sumar)
        btn_restar = crear_boton("-1", self.restar)
        btn_reiniciar = crear_boton("Reiniciar", self.reiniciar)
        btn_historial = crear_boton("Historial", mostrar_historial)
        
        # --- Añadir botones a la app ---
        self.layout.addWidget(btn_sumar)
        self.layout.addWidget(btn_restar)
        self.layout.addWidget(btn_reiniciar)
        self.layout.addWidget(btn_historial)

    # *** Funciones para conectar los botones de la app ***
    def sumar(self):
        nuevo_valor = incrementar()
        self.etiqueta.setText(f"Clics: {nuevo_valor}")
    
    def restar(self):
        nuevo_valor = decrementar()
        self.etiqueta.setText(f"Clics: {nuevo_valor}")
    
    def reiniciar(self):
        nuevo_valor = reiniciar()
        self.etiqueta.setText(f"Clics: {nuevo_valor}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicar_estilo("ui/estilo_claro.qss")
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
