# Módulo logica.py

# Inicializamos las variables.

contador = 0
historial = []

# Función para incrementar el clic de 1 en 1.
def incrementar():
    global contador
    contador += 1
    historial.append(f"+1 → {contador}")
    return contador

# Función para decrementar el clic de 1 en 1.
def decrementar():
    global contador
    if contador > 0:
        contador -= 1
    historial.append(f"-1 → {contador}")
    return contador

# Función para limpiar o reiniciar el contador desde 0.
def reiniciar():
    global contador
    contador = 0
    historial.clear()
    return contador

# Función para obtener el historial.
def obtener_historial():
    return historial