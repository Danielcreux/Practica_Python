"""Ahora vamos a mejorar algo importante: si el usuario se equivoca, en
lugar de terminar el programa, queremos que vuelva a pedir la edad.

Ahí vamos a introducir:

while

La idea será que esto:

¿Cuántos años tienes? hola
Debes introducir un número
¿Cuántos años tienes? -5
Edad no válida
¿Cuántos años tienes? 24
Joshué es mayor de edad

siga preguntando hasta recibir un dato correcto"""

nombre = input("¿Cuál es tu nombre?").strip().title()

while True:
    try:
        edad = int(input("¿Cuántos años tienes?"))

        if edad < 0:
            print("La edad no puede ser negativa")
        else:
            break

    except ValueError:
        print("Error: debes introducir un número")


if edad < 18:
    print(f"{nombre} es menor de edad ")       
else:
    print(f"{nombre} es mayor de edad")

    
