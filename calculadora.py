nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
vip = input("¿Eres miembro VIP? (si/no): ")

subtotal = precio * cantidad

if vip == "si" and cantidad >= 5:
    descuento = 0.25
elif vip == "si" or cantidad >= 5:
    descuento = 0.15
else:
    descuento = 0.0

total_descuento = subtotal * descuento
total_pagar = subtotal - total_descuento

print("Factura")
print("Nombre:", nombre)
print("Subtotal:", subtotal)
print("Descuento:", total_descuento)
print("Total a pagar:", total_pagar)
print ("Miembro vip:", vip)