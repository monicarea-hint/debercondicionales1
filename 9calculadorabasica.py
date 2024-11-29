def calculadora():
    print("Calculadora básica en Python")
    
    # Solicitar números al usuario
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Por favor, introduce valores numéricos.")
        return
    
    # Solicitar la operación
    operacion = input("Introduce la operación (+, -, *, /): ")
    
    # Realizar la operación
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Error: No se puede dividir entre cero.")
            return
    else:
        print("Operación no válida.")
        return
    
    # Mostrar el resultado
    print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()
