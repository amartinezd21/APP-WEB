compra = float(input("Digite el valor de la compra: "))

if compra > 300000:
    compra = compra - (compra * 0.20)

print("Total a pagar:", compra)