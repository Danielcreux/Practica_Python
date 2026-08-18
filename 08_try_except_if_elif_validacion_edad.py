"""Perfecto. Siguiente ejercicio: validar una edad correctamente con try, except y condiciones.

Tu programa debe:

Pedir el nombre.
Pedir la edad.
Si el usuario escribe letras, mostrar Debes introducir un número.
Si la edad es menor que 0, mostrar Edad no válida.
Si la edad está entre 0 y 17, mostrar que es menor de edad.
Si tiene 18 o más, mostrar que es mayor de edad."""

nombre = input("¿Cuál es tu nombre?").strip().title()

try:
    edad = int(input("¿Cuántos años tienes?"))

    if edad < 0:
        print("La edad no puede ser negativa")
    elif edad < 18:
        print(f"{nombre} es menor de edad ")       
    else:
        print(f"{nombre} es mayor de edad")

except ValueError:
    print("Error: debes introducir un número")
    
    
