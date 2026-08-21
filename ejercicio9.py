nota = int(input("Digite una nota entre 0 y 10: "))

if nota == 0:
    print("cero")
if nota == 1:
    print("uno")
if nota == 2:
    print("dos")
if nota == 3:
    print("tres")
if nota == 4:
    print("cuatro")
if nota == 5:
    print("cinco")
if nota == 6:
    print("seis")
if nota == 7:
    print("siete")
if nota == 8:
    print("ocho")
if nota == 9:
    print("nueve")
if nota == 10:
    print("diez")

if nota < 0 or nota > 10:
    print("La nota no es válida.")