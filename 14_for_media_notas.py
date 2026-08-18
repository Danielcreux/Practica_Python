"""además de contar aprobados y suspendidos, calcula la media de todas
las notas. Por ejemplo, tendrás que ir acumulando las notas en una
variable como:

suma = 0

y luego dividir entre la cantidad de notas"""

notas = [8, 4, 7, 10, 3, 6]

aprobados = 0
suspendidos = 0
suma = 0

for nota in notas:
    suma += nota

    if nota >= 5:
        aprobados += 1
        print(f"{nota} → Aprobado")
    else:
        suspendidos += 1
        print(f"{nota} → Suspendido")

media = suma / len(notas)

print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")
print(f"Media: {media}")
    
