"""quiero que hagamos validación de datos, por ejemplo impedir que
alguien introduzca una edad negativa o escriba "hola" como edad. Ahí
empezaremos con try y except"""

try:
    edad = int(input("¿Cuántos años tienes?"))

    if edad < 0:
        print("La edad no puede ser negativa")
    else:
        print(f"Tienes {edad} años")

except ValueError:
    print("Error:debes introducir un número")
    
    
