dia = int(input("digita el dia:"))
mes = int(input("digita el mes:"))
año = int(input("digita el año:"))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 30:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta")