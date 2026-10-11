"""
Nombre: Ricardo Daniel Lazo 
Ejercicio: 25488. Encuentra los repetidos
Descripción: Lee n números enteros y determina si hay algún elemento repetido en la lista imprimiendo YES o NO.
"""

# Leer la cantidad de elementos
n = int(input())

# Leer los números
numeros = input().split()
repetido = False

# Comparar cada número con los demás
for i in range(n):
    for j in range(i + 1, n):
        if numeros[i] == numeros[j]:
            repetido = True
# Imprimir el resultado según lo encontrado
if repetido == True:
    print("YES")
else:
    print("NO")
    