dia = int(input("Digite el día: "))
mes = int(input("Digite el mes: "))
año = int(input("Digite el año: "))

if mes >= 1 and mes <= 12:
    if dia >= 1 and dia <= 30:
        print("La fecha es correcta")

        
        if dia < 30:
            dia += 1
        else:
            dia = 1
            if mes < 12:
                mes += 1
            else:
                mes = 1
                año += 1

        print("El día siguiente es:", dia, "/", mes, "/", año)

    else:
        print("La fecha es incorrecta")


