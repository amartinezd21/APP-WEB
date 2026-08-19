def procesar_coleccion(lista_datos, funcion_transformacion, funcion_filtro):
    resultado = []

    for dato in lista_datos:
        if funcion_filtro(dato):
            resultado.append(funcion_transformacion(dato))

    return resultado


def es_par(numero):
    return numero % 2 == 0


def duplicar(numero):
    return numero * 2


numeros = [1, 2, 3, 4, 5, 6, 7, 8]

resultado = procesar_coleccion(numeros, duplicar, es_par)

print("Resultado:", resultado)