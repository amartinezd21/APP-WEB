import math 

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
            print(f"Calificación {calificacion} agregada correctamente para {self.nombre}.")
        else:
            print("Calificación inválida. Por favor, ingrese un valor entre 0 y 100.")

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0

        promedio = sum(self.calificaciones) / len(self.calificaciones)
        return math.ceil(promedio)

    def estado_final(self):
        promedio = self.calcular_promedio()
        if promedio >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

nombre = input("Ingrese el nombre del estudiante: ")
estudiante = Estudiante(nombre)
cantidad = int(input("Ingrese la cantidad de calificaciones a agregar: "))

for i in range(cantidad):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    estudiante.agregar_calificacion(calificacion)

    print ("Resultados:")
    print ("estudiante:", estudiante.nombre)
    print ("calificaciones:", estudiante.calificaciones)
    print ("Promedio:", estudiante.calcular_promedio())
    print ("Estado Final:", estudiante.estado_final())






