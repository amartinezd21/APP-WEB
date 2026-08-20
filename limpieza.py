ventas_dia = ["Electronica", "Ropa", "Electronica", "Hogar", "Ropa", "Electronica", "Juguetes", "Hogar"]

categorias_unicas = set(ventas_dia)

print("Categorías únicas vendidas hoy:", categorias_unicas)

conteo = {}
for categoria in ventas_dia:
    if categoria in conteo:
        conteo[categoria] += 1
    else:
        conteo[categoria] = 1

print("Cantidad de ventas por categoría:")
for categoria, cantidad in conteo.items():
    print(f"{categoria}: {cantidad}")

categoria_mas_vendida = max(conteo, key=conteo.get)
print("Categoría más vendida hoy:", categoria_mas_vendida)
print("Cantidad de ventas de la categoría más vendida:", conteo[categoria_mas_vendida])
print("Cantidad de ventas de la categoría menos vendida:", min(conteo.values()))

