"""Modifica tu programa para que clasifique la nota así:

0 - 4.99   → Suspendido
5 - 6.99   → Aprobado
7 - 8.99   → Notable
9 - 10     → Sobresaliente

Y además, si alguien introduce:

11

o:

-3

debe mostrar:

Nota no válida"""

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

if nota_examen < 0 or nota_examen > 10: #si ocurre una condición o la otra.
    print("Nota no válida")
elif nota_examen >= 9:
    print(f"{nombre} Sobresaliente")
elif nota_examen >= 7:
    print(f"{nombre} Notable")
elif nota_examen >= 5:
    print(f"{nombre} Aprobado")
else:
    print(f"{nombre} Suspendido")
    
