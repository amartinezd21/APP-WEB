def auditar_evento(nivel, *etiquetas, **metadatos):
    registro = f"[{nivel.upper()}]"

    if etiquetas:
        registro += " tags: " + ", ".join(f"#{etiqueta}" for etiqueta in etiquetas)

    if metadatos:
        registro += " / metadatos -> " + ", ".join(
            f"{clave}={valor}" for clave, valor in metadatos.items()
        )

    print(registro)

    return registro

auditar_evento(
    "error",
    "seguridad",
    "auth",
    usuario="admin",
    ip="192.168.1.50",
    intento=3
)