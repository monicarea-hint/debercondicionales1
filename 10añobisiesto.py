def es_bisiesto():
    print("Comprobador de años bisiestos")
    
    # Solicitar el año al usuario
    try:
        año = int(input("Introduce un año: "))
    except ValueError:
        print("Por favor, introduce un valor numérico válido.")
        return
    
    # Determinar si es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")

# Ejecutar la función
es_bisiesto()
