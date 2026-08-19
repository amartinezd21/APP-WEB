def calcular_metricas(*numeros, **opciones):
    operacion = opciones.get("operacion", "suma")
    redondear = opciones.get("redondear", False)

    if not numeros:
        return 0

    if operacion == "suma":
        resultados = sum(numeros)

    elif operacion == "promedio":
        resultados = sum(numeros) / len(numeros)

    else:
        raise ValueError("La operacion debe ser 'suma' o 'promedio'")

    if redondear is not False:
        if redondear is True:
            redondear = 2

        resultados = round(resultados, redondear)

    return resultados


print(calcular_metricas(10, 20, 25, operacion="promedio", redondear=True))


