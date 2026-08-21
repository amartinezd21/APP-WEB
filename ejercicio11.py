numero = int(input("Digite un número de tres cifras: "))

centena = numero // 100
unidad = numero % 10

if centena == unidad:
    print("El número es capicúa")
else:
    print("El número no es capicúa")
