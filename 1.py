from collections import OrderedDict

def crear_perfil_usuarios(nombre, email, rol):
    if "@" not in email:
        return "error: el email debe contener el simbolo '@'."

    perfil = OrderedDict([
        ("nombre", nombre),
        ("email", email),
        ("rol", rol)
    ])

    return perfil

usuario = crear_perfil_usuarios("Alejandro", "alejandro@gmail.com", "Administrador")
print(usuario)