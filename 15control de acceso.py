intentos = 3
usuario_correcto = "admin"
contraseña_correcta = "1234"

while intentos > 0:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print(f"Bienvenido, {usuario}.")
        break
    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos}")
if intentos == 0:
    print("Acceso bloqueado.")
