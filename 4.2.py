def generar_reporte(titulo, *secciones, **firmas):
    print(f"REPORTE: {titulo}")

    for seccion in secciones:
        print(f"- {seccion}")

    for nombre, firma in firmas.items():
        print(f"{nombre}: {firma}")


secciones_basicas = (
    "Introducción",
    "Resultados",
    "Conclusiones"
)

secciones_adicionales = [
    "Anexos",
    "Bibliografía"
]

firmas = {
    "autor": "Juan Pérez",
    "revisor": "Ana García"
}

generar_reporte(
    "Informe anual",
    *secciones_basicas,
    *secciones_adicionales,
    **firmas
)