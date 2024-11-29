def es_par(numero):
    return True if numero % 2 == 0 else False

# Ejemplo de uso
entrada = int(input("Introduce un número: "))
print(f"Entrada: {entrada} → Salida: {es_par(entrada)}")
