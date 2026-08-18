"""Haz un programa que pida:

nombre
edad
país

Y que permita acceder solo si:

tiene 18 años o más
y vive en España

Si no cumple ambas condiciones:

Acceso denegado"""

nombre = input("¿Cuál es tu nombre?").strip().title()
edad = int(input("¿Cuántos años tienes?"))
pais = input("¿Cuál es tu pais?").strip().title() ## puedo probar con .lower

print(f"Tu nombre es {nombre}")
print(f"Tu edad es {edad}")
print(f"Tu pais es {pais}")

if edad >= 18 and pais == "España":
    print("Tienes acceso a la pagina")
else:
    print("No tienes acceso")
    
    
    
