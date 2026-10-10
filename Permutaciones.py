"""
Nombre: Ricardo Daniel Lazo
Ejercicio: 25469. Permutaciones
Descripción: Genera e imprime todas las permutaciones posibles de los números {1, 2, 3, 4} en orden lexicográfico usando ciclos anidados.
"""

# Ciclos for anidados del 1 al 4 para generar combinaciones
for i in range(1, 5):
    for j in range(1, 5):
        # Evitar repetir el número i
        if j == i:
            continue
        for k in range(1, 5):
            # Evitar repetir los números i, j
            if k == i or k == j:
                continue
            for l in range(1, 5):
                # Evitar repetir los números i, j, k
                if l == i or l == j or l == k:
                    continue
                # Imprimir la permutación válida
                print(i, j, k, l)
                