def obtener_signo_zodiaco():
    print("Determinador de Signo Zodiacal")
    
    # Solicitar día y mes de nacimiento
    try:
        dia = int(input("Introduce el día de nacimiento: "))
        mes = input("Introduce el mes de nacimiento (ejemplo: marzo): ").lower()
    except ValueError:
        print("Por favor, introduce un día válido.")
        return
    
    # Diccionario para convertir el mes a número
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    
    if mes not in meses:
        print("Mes no válido. Asegúrate de escribirlo correctamente.")
        return
    
    mes_num = meses[mes]
    
    # Determinar el signo zodiacal
    if (mes_num == 1 and 20 <= dia <= 31) or (mes_num == 2 and 1 <= dia <= 18):
        signo = "Acuario"
    elif (mes_num == 2 and 19 <= dia <= 29) or (mes_num == 3 and 1 <= dia <= 20):
        signo = "Piscis"
    elif (mes_num == 3 and 21 <= dia <= 31) or (mes_num == 4 and 1 <= dia <= 19):
        signo = "Aries"
    elif (mes_num == 4 and 20 <= dia <= 30) or (mes_num == 5 and 1 <= dia <= 20):
        signo = "Tauro"
    elif (mes_num == 5 and 21 <= dia <= 31) or (mes_num == 6 and 1 <= dia <= 20):
        signo = "Géminis"
    elif (mes_num == 6 and 21 <= dia <= 30) or (mes_num == 7 and 1 <= dia <= 22):
        signo = "Cáncer"
    elif (mes_num == 7 and 23 <= dia <= 31) or (mes_num == 8 and 1 <= dia <= 22):
        signo = "Leo"
    elif (mes_num == 8 and 23 <= dia <= 31) or (mes_num == 9 and 1 <= dia <= 22):
        signo = "Virgo"
    elif (mes_num == 9 and 23 <= dia <= 30) or (mes_num == 10 and 1 <= dia <= 22):
        signo = "Libra"
    elif (mes_num == 10 and 23 <= dia <= 31) or (mes_num == 11 and 1 <= dia <= 21):
        signo = "Escorpio"
    elif (mes_num == 11 and 22 <= dia <= 30) or (mes_num == 12 and 1 <= dia <= 21):
        signo = "Sagitario"
    elif (mes_num == 12 and 22 <= dia <= 31) or (mes_num == 1 and 1 <= dia <= 19):
        signo = "Capricornio"
    else:
        print("Fecha no válida.")
        return
    
    # Mostrar el signo zodiacal
    print(f"Tu signo es {signo}.")

# Ejecutar el programa
obtener_signo_zodiaco()
