# Módulo botones.py

# Importamos las librerías.
from PyQt5.QtWidgets import QPushButton, QMessageBox
from logica.logica import obtener_historial

# Función crear botones.
def crear_boton(texto, funcion):
    """ Esta función añadirá los botones a la app con su respectivo texto"""
    boton = QPushButton(texto)
    boton.clicked.connect(funcion)
    return boton

# Función para mostrar el historial de clics.
def mostrar_historial():
    historial = obtener_historial()
    mensaje = "\n".join(historial) if historial else "Sin clics aún."

    msg = QMessageBox()
    msg.setWindowTitle("Historial de Clics")
    msg.setText(mensaje)
    msg.exec_()