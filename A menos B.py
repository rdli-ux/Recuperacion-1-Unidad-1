"""
Nombre: Ricardo Daniel Lazo
Ejercicio: 25490. A menos B
Descripción: Imprime todos los valores de un arreglo que sean distintos a tres números específicos dados al inicio.
"""

# Leer los tres números prohibidos (b1, b2, b3)
prohibidos = input().split()
b1 = int(prohibidos[0])
b2 = int(prohibidos[1])
b3 = int(prohibidos[2])

# Leer la cantidad de elementos
n = int(input())

# Leer los elementos del arreglo
arreglo = input().split()

# Imprimir solo los elementos que no coincidan con b1, b2 o b3
for i in range(n):
    num = int(arreglo[i])
    if num != b1 and num != b2 and num != b3:
        print(num, end=" ")
print()
