def buscar_clave_profunda(estructura, clave_objetivo):
    for clave, valor in estructura.items():

        if clave == clave_objetivo:
            return valor

        if isinstance(valor, dict):
            resultado = buscar_clave_profunda(valor, clave_objetivo)

            if resultado is not None:
                return resultado

    return None


datos = {
    "usuario": {
        "nombre": "Carlos",
        "configuracion": {
            "tema": "oscuro",
            "preferencias": {
                "idioma": "es",
                "notificaciones": True
            }
        }
    },
    "servidor": {
        "host": "localhost",
        "puerto": 5432
    }
}


print(buscar_clave_profunda(datos, "idioma"))
print(buscar_clave_profunda(datos, "puerto"))
print(buscar_clave_profunda(datos, "direccion"))