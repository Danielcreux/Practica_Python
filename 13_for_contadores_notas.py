"""Ahora quiero que además cuentes cuántos aprobados y suspendidos hay.

Con esas notas deberías terminar mostrando:

Aprobados: 4
Suspendidos: 2

Pista: antes del for, crea dos variables:

aprobados = 0
suspendidos = 0

Y dentro del if tendrás que aumentar una de ellas con:

aprobados += 1"""

notas = [8, 4, 7, 10, 3, 6]

aprobados = 0
suspendidos = 0

for nota in notas:
    if nota >= 5:
        aprobados += 1
        print(f"{nota} → Aprobado")
    else:
        suspendidos +- 1
        print(f"{nota} → Suspendido")

print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")
    
