"""Haz que el programa pregunte los datos al usuario con input() en vez de
tenerlos escritos directamente."""

nombre = input("¿Cuál es tu nombre? ").strip().title() ##mayuscula a lo que esté en minúscula
edad = int(input("¿Cuántos años tienes? "))
lenguaje_favorito = input("¿Cuál es tu lenguaje favorito? ").strip().capitalize()

print(f"Tu nombre es {nombre}")
print(f"Tu edad es {edad}")
print(f"Tu lenguaje favorito es {lenguaje_favorito}")
      
if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")
