este es el codigo defectuoso  

def agregar_bitacora(mensaje, historial=[]):
    historial.append(mensaje)
    return historial

Refactorización usando None

def agregar_bitacora(mensaje, historial=None):
    if historial is None:
        historial = []

    historial.append(mensaje)
    return historial

print(agregar_bitacora("primer mensaje"))
print(agregar_bitacora("segundo mensaje"))

