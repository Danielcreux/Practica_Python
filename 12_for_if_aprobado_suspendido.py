"""Ahora vamos a mezclar for con números.

Crea esta lista:

notas = [8, 4, 7, 10, 3, 6]

Recórrela con un for y muestra para cada nota:

8 → Aprobado
4 → Suspendido
7 → Aprobado
10 → Aprobado
3 → Suspendido
6 → Aprobado"""

notas = [8, 4, 7, 10, 3, 6]

for nota in notas:
    if nota >= 5:
        print(f"{nota} → Aprobado")
    else:
        print(f"{nota} → Suspendido")

    
