numero = int(input("Introduce un número: "))
suma_digitos = sum(int(digito) for digito in str(numero))
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
