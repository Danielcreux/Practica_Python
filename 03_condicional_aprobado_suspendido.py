"""Haz un programa que pida:

nombre
edad
nota de examen

Y que diga:

si es menor de edad
si es mayor de edad
si ha aprobado o suspendido

Reglas:

nota >= 5 → Aprobado
nota < 5 → Suspendido

Pista: la nota puede tener decimales, así que esta vez no uses int()"""

nombre = input("¿Cuál es tu nombre? ").strip().title()
# Quita espacios y pone en mayúscula la primera letra de cada palabra
edad = int(input("¿Cuántos años tienes? "))
nota_examen = float(input("¿Cuál es la nota de examen? "))

print(f"Tu nombre es {nombre}")
print(f"Tu edad es {edad}")
print(f"Tu nota de examen es {nota_examen}")
      
if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")

if nota_examen >= 5:
    print(f"{nombre} ha aprobado")
else:
    print(f"{nombre} ha suspendido")
