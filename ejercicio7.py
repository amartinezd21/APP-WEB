dia = int(input("digite el dia: "))
mes = int(input("digite el mes:"))
año = int(input("digite el año:"))

if mes == 2:
    if dia >= 1 and dia <= 28:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta porque no es año bisiesto")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta")

elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 31:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta")

else:
    print ("la fecha es incorrecta")
