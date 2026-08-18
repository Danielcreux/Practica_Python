"""Pide:

nombre
edad
pais
esta_bloqueado

Para esta_bloqueado, pregunta:

¿Está bloqueado? (si/no):

El usuario solo podrá entrar si:

tiene 18 años o más
vive en España
NO está bloqueado"""

nombre = input("¿Cuál es tu nombre? ").strip().title()
edad = int(input("¿Cuántos años tienes? "))
pais = input("¿Cuál es tu país? ").strip().title()

bloqueado = input("¿Está bloqueado? (si/no): ").strip().lower()
esta_bloqueado = bloqueado == "si"

if edad >= 18 and pais == "España" and not esta_bloqueado:
    print(f"{nombre}, tienes acceso")
else:
    print(f"{nombre}, no tienes acceso")
   
    
    
