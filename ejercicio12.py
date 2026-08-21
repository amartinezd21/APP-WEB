llantas = int(input("Digite la cantidad de llantas: "))

if llantas < 5:
    precio = 30000
elif llantas <= 10:
    precio = 25000
else:
    precio = 20000

total = llantas * precio

print("Precio por cada llanta:", precio)
print("Total a pagar:", total)