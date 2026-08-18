"""Quiero que hagas un programa que tenga:

nombre
edad
lenguaje_favorito

Y que imprima:

Hola, soy Valentina
Tengo 24 años
Mi lenguaje favorito es Python

Después añade:

if edad >= 18:"""

nombre = "Valentina"
edad = 24
lenguaje_favorito = "python"

print(f"Hola, soy{nombre}")
print(f"Tengo{edad}")
print(f"Mi lenguaje favorito es{lenguaje_favorito}")

if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")
