calificaciones = []
while True:
    calificacion = float(input("Introduce una calificación (-1 para terminar): "))
    if calificacion == -1:
        break
    calificaciones.append(calificacion)

if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
