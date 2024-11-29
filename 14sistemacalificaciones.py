def sistema_calificaciones():
    print("Sistema de Calificaciones")
    
    # Solicitar la calificación numérica
    try:
        calificacion = float(input("Introduce tu calificación (0-100): "))
    except ValueError:
        print("Por favor, introduce un valor numérico válido.")
        return
    
    # Validar y asignar la calificación en letra
    if 90 <= calificacion <= 100:
        letra = "A"
    elif 80 <= calificacion < 90:
        letra = "B"
    elif 70 <= calificacion < 80:
        letra = "C"
    elif 60 <= calificacion < 70:
        letra = "D"
    elif 0 <= calificacion < 60:
        letra = "F"
    else:
        print("Por favor, introduce una calificación entre 0 y 100.")
        return
    
    # Mostrar la calificación en letra
    print(f"Tu calificación es {letra}.")

# Ejecutar el sistema
sistema_calificaciones()
