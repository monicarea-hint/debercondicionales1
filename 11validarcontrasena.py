def validar_contraseña():
    # Contraseña fija
    contraseña_fija = "12345"
    
    print("Validador de contraseña")
    
    # Solicitar contraseña al usuario
    contraseña_ingresada = input("Introduce la contraseña: ")
    
    # Validar contraseña
    if contraseña_ingresada == contraseña_fija:
        print("Acceso concedido")
    else:
        print("Acceso denegado")

# Ejecutar la función
validar_contraseña()
