# Módulo ventana.py

# Importamos las librerías
from PyQt5.QtWidgets import QApplication, QWidget

#Función para centrar la ventana de la app.
def centrar_ventana(ventana: QWidget):
    """ 
    Esta Función es una función reutilizable, de manera que se puede usar
    en otras aplicaciones. Su función aunque es sencilla es poderosa
    nos permite centrar una ventana, o moverla a algún otro lado según el gusto del
    programador.
    """
    pantalla = QApplication.primaryScreen()
    t_pantalla = pantalla.availableGeometry()
    t_ventana = ventana.frameGeometry()
    c_pantalla = t_pantalla.center()
    t_ventana.moveCenter(c_pantalla)
    ventana.move(t_ventana.topLeft())