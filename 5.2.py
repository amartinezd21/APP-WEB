def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):
    try:
        print(f"Ejecutando misión: {nombre_tarea}")

        if nombre_tarea == "Misión fallida":
            raise ValueError("La operación no pudo completarse.")

        resultado = f"Resultado de la tarea '{nombre_tarea}'"

        if al_exito is not None:
            al_exito(nombre_tarea, resultado)

        return resultado

    except Exception as error:
        if al_error is not None:
            al_error(nombre_tarea, str(error))

        return None


def mostrar_exito(nombre_tarea, resultado):
    print(f" Éxito: {nombre_tarea}")
    print(f"Resultado: {resultado}")


def mostrar_error(nombre_tarea, mensaje_error):
    print(f" Error en: {nombre_tarea}")
    print(f"Mensaje: {mensaje_error}")


ejecutar_mision(
    "Procesar datos",
    al_exito=mostrar_exito,
    al_error=mostrar_error
)

print()

ejecutar_mision(
    "Misión exitosa",
    al_exito=mostrar_exito,
    al_error=mostrar_error
)