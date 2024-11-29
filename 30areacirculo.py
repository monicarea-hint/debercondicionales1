import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return round(math.pi * radio ** 2, 2)

# Ejemplo de uso
radio = float(input("Introduce el radio del círculo: "))
print(f"Entrada: {radio} → Salida: {calcular_area_circulo(radio)}")
