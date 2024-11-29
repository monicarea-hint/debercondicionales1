import random

def juego_de_numeros():
    print("¡Bienvenido a un Juego de Números!")
    
    # Generar un número aleatorio entre 1 y 10
    numero_secreto = random.randint(1, 10)
    
    try:
        # Solicitar un número al usuario
        numero_usuario = int(input("Adivina un número entre 1 y 10: "))
        
        # Verificar si acertó
        if numero_usuario == numero_secreto:
            print("¡Felicidades, acertaste!")
        else:
            print(f"Intenta de nuevo. El número era {numero_secreto}.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Ejecutar el juego
juego_de_numeros()
