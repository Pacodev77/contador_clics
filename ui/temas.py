# Módulo temas.py
#ui/temas.py

from PyQt5.QtWidgets import QApplication

def aplicar_estilo(ruta_estilo: str):
    try:
        with open(ruta_estilo, "r") as archivo_estilo:
            estilo = archivo_estilo.read()
            QApplication.instance().setStyleSheet(estilo)
    except FileNotFoundError:
        print("Archivo no encontrado.")
